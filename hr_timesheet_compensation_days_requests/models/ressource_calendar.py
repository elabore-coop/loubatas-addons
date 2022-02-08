# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResourceCalendar(models.Model):
    _name = "resource.calendar"
    _inherit = "resource.calendar"

    total_hours_per_week = fields.Float(compute="_compute_total_hours_per_week")

    @api.depends("attendance_ids")
    def _compute_total_hours_per_week(self):
        for record in self:
            self.total_hours_per_week = 0
            for attendance in record.attendance_ids:
                self.total_hours_per_week = self.total_hours_per_week + (
                    attendance.hour_to - attendance.hour_from
                )

    def get_work_days_expected(self):
        days = []
        for attendance in self.attendance_ids:
            day = int(attendance.dayofweek)
            if not day in days:
                days.append(day)
        return days
