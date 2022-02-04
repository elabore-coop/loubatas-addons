# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResourceCalendar(models.Model):
    _name = "resource.calendar"
    _inherit = "resource.calendar"

    def get_work_days_expected(self):
        days = []
        for attendance in self.attendance_ids:
            day = int(attendance.dayofweek)
            if not day in days:
                days.append(day)
        return days
