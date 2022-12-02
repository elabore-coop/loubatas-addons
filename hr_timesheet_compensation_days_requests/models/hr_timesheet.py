# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountAnalyticLine(models.Model):
    _name = "account.analytic.line"
    _inherit = "account.analytic.line"

    considered_for_compensation_days = fields.Boolean()

    @api.multi
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update(
            considered_for_compensation_days=False)
        return super(AccountAnalyticLine, self).copy(default)