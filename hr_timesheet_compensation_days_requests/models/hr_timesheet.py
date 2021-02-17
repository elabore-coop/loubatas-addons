# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class AccountAnalyticLine(models.Model):
    _name = 'account.analytic.line'
    _inherit = 'account.analytic.line'

    considered_for_compensation_days = fields.Boolean(
        readonly=True
    )