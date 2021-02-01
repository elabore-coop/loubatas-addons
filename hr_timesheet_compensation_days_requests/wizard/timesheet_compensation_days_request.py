from datetime import datetime, timedelta
import time
from odoo import api, fields, models

class CompensationDaysRequest(models.TransientModel):
    _name = "timesheet.compensation.days.request"
    _description = "Compensation days request"

    holiday_status_id = fields.Many2one(
        "hr.leave.type", 
        string="Time Off Type", 
        required=True
    )

    from_date = fields.Date(
        string = 'Period start',
        required = True
    )

    to_date = fields.Date(
        string = 'Period end',
        required = True
    )

    nb_working_days = fields.Float(
        string = 'Number of working days',
        required = True
    )

    @api.onchange('from_date')
    def on_change_from_date(self):
        """ This function update the to_date field if it is before the new from_date """
        if self.to_date and self.from_date: 
            if self.to_date < self.from_date:
                self.to_date = self.from_date

    @api.onchange('to_date')
    def on_change_to_date(self):
        """ This function prevent the to_date to be before the from_date """
        # if isinstance(self.to_date, Date) and isinstance(self.from_date, Date): 
        if self.to_date and self.from_date:
            if self.to_date < self.from_date:
                self.to_date = self.from_date

    @api.multi
    def compensation_days_request_validate(self):
        nb_days_considered = (self.to_date - self.from_date) - timedelta(days=self.nb_working_days)
        
        # Get all the timesheet entries between from_date and to_date
        timesheet_entries = self.env['account.analytic.line'].search((['user_id', '=', self.env.user.id]),
                                                                     (['date', '>=', self.from_date]),
                                                                     (['date', '<=', self.to_date]))

        # Calculation of the number of hours worked
        nb_worked_hours = 0
        for timesheet_entry in timesheet_entries:
            nb_worked_hours = nb_worked_hours + timesheet_entry.unit_amount

        # Determine number of hours to request
        hours_per_day = 7
        if nb_worked_hours > (nb_days_considered * hours_per_day):
            nb_hours_to_request = (nb_days_considered * hours_per_day) - nb_worked_hours

            if self:
                datas = {
                    'accrual' : True,
                    'date_from' : self.from_date,
                    'date_to' : self.to_date,
                    'number_of_days' : nb_of_hours_to_request / hours_per_day,
                    'holiday_status_id' : self.holiday_status_id
                }

            componsation_days_requests_list = self.env['hr.leave.allocation'].browse(self._context.get('active_ids')).create(values=datas)

            search_view_ref = self.env.ref('hr_holidays.view_hr_leave_allocation_filter', False)
            form_view_ref = self.env.ref('hr_holidays.hr_leave_allocation_view_form', False)
            tree_view_ref = self.env.ref('hr_holidays.hr_leave_allocation_view_tree', False)

            return  {
                'domain': [('id', 'in', componsation_days_requests_list)],
                'name': 'Compensation days requests',
                'res_model': 'hr.leave.allocation',
                'type': 'ir.actions.act_window',
                'views': [(tree_view_ref.id, 'tree'), (form_view_ref.id, 'form')],
                'search_view_id': search_view_ref and search_view_ref.id,
            }

        # else: # error message "No compensation days on that period"