from datetime import datetime, timedelta
import time
from odoo import api, fields, models

class CompensationDaysRequest(models.TransientModel):
    _name = "timesheet.compensation.days.request"
    _description = "Compensation days request"

    holiday_status_id = fields.Many2one(
        "hr.leave.type", 
        string = "Time Off Type", 
        required = True
    )

    nb_working_days = fields.Float(
        string = 'Worked days',
        required = False,
        default = '0'
    )

    nb_hours_per_day = fields.Float(
        string = 'Hours worked per day',
        required = False,
        default = '7'
    )

    expected_worked_hours = fields.Float(
        string = 'Expected worked hours on the selected lines',
        required = True,
        default = '0'
    )

    effective_worked_hour = fields.Float(
        string = 'Worked hours on the selected lines',
        readonly=True
    )

    nb_compensation_hours = fields.Float(
        readonly=True,
        default='0'
    )


    def _calculate_nb_compensation_hours(self):
        if self.effective_worked_hour > self.expected_worked_hours:
            self.nb_compensation_hours = self.effective_worked_hour - self.expected_worked_hours
        else:
            self.nb_compensation_hours = 0

    @api.onchange('holiday_status_id')
    def compensation_days_addition_request(self):
        # Get all the timesheet entries selected
        timesheet_entries = self.env['account.analytic.line'].search(["active_ids"])

        self.effective_worked_hour = 0
        for timesheet_entry in timesheet_entries:
            if not timesheet_entry.considered_for_compensation_days:
                self.effective_worked_hour = self.effective_worked_hour + timesheet_entry.unit_amount


    @api.onchange('nb_working_days', 'nb_hours_per_day')
    def on_change_work_data(self):
        """ This function calculate a proposed expected_worked_hours"""
        self.expected_worked_hours = self.nb_working_days * self.nb_hours_per_day
        self._calculate_nb_compensation_hours()


    @api.onchange('expected_worked_hours')
    def on_change_expected_worked_hours(self):
        self._calculate_nb_compensation_hours()


    @api.multi
    def compensation_days_request_validate(self):
        # Increment the remaining hours/days in the leave.type selected


        # Check the timesheet lines to ensure they won't be considered in the calculation later
        timesheet_entries = self.env['account.analytic.line'].context.get("active_ids")
        for timesheet_entry in timesheet_entries:
            timesheet_entry.considered_for_compensation_days = True