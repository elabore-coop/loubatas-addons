from datetime import datetime, timedelta
import logging
import time
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class CompensationDaysRequest(models.TransientModel):
    _name = "timesheet.compensation.days.request"
    _description = "Compensation days request"

    def _default_number_hours_per_day(self):
        employee_id = self.env.context.get('default_employee_id') or self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        return employee_id.sudo().resource_id.calendar_id.hours_per_day


    timesheet_entries = fields.Many2many(
        comodel_name = "account.analytic.line", 
        relation = "list_wizard_timesheet")

    holiday_status_id = fields.Many2one(
        "hr.leave.type", 
        string = "Time Off Type", 
        required = True
    )

    from_date = fields.Date(
        string = 'Start date',
        required = True
    )

    to_date = fields.Date(
        string = 'End date',
        required = True
    )

    ##################
    # Read Only fields
    ##################
    nb_working_days = fields.Float(
        string = 'Worked days',
        readonly = True,
        default = '0'
    )

    nb_hours_per_day = fields.Float(
        string = 'Hours worked/day',
        readonly = True,
        default = _default_number_hours_per_day
    )

    expected_worked_hours = fields.Float(
        string = 'Expected hours',
        readonly = True,
        default = '0'
    )

    effective_worked_hours = fields.Float(
        string = 'Worked hours',
        readonly = True,
        default = '0'
    )

    nb_compensation_hours = fields.Float(
        string = 'Hours requested',
        readonly = True,
        default = '0'
    )

    ##################
    # Wizard's methods
    ##################
    def _calculate_nb_compensation_hours(self):        
        if self.effective_worked_hours > self.expected_worked_hours:
            self.nb_compensation_hours = self.effective_worked_hours - self.expected_worked_hours
        else:
            self.nb_compensation_hours = 0


    @api.onchange('holiday_status_id')
    def calculate_compensation_days(self):
        # Get all the timesheet entries in the period selected
        self.timesheet_entries = self.env['account.analytic.line'].search([('date', '>=', self.from_date), ('date', '<=', self.to_date)])
        
        self.effective_worked_hours = 0
        self.nb_working_days = 0
        current_date = datetime(2000, 1, 1).date
        for timesheet_entry in self.timesheet_entries:
            if not timesheet_entry.considered_for_compensation_days:
                # the analytic.account.line has not been considered yet in the compensation days calculations
                self.effective_worked_hours = self.effective_worked_hours + timesheet_entry.unit_amount
                if not(timesheet_entry.date == current_date):
                    # the employee has worked another day
                    self.nb_working_days += 1
                    current_date = timesheet_entry.date
        
        self.expected_worked_hours = self.nb_working_days * self.nb_hours_per_day
        self._calculate_nb_compensation_hours()


    @api.onchange('expected_worked_hours')
    def on_change_expected_worked_hours(self):
        self._calculate_nb_compensation_hours()


    @api.multi
    def compensation_days_request_validate(self):
        # Last check of the compensation hours to be registered
        self.calculate_compensation_days()

        employee_id = self.env.context.get('default_employee_id') or self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
        nb_compensations_days = self.nb_compensation_hours / self.nb_hours_per_day

        self.env['hr.leave.allocation'].create({
            'name': 'request for compensation hours due to extra hours',
            'employee_id': employee_id.id,
            'holiday_status_id': self.holiday_status_id.id,
            'number_of_days': nb_compensations_days,
        })
        
        # Check the timesheet lines to ensure they won't be considered in the calculation later
        for timesheet_entry in self.timesheet_entries:                                                                         
            timesheet_entry.considered_for_compensation_days = True