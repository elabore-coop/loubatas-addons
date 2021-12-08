# -*- coding: utf-8 -*-

from odoo import tools
from odoo import fields, models, _

class Lead(models.Model):
    _inherit = 'crm.lead'

    start_date = fields.Date(string=_("Arrival date"), index=True)
    end_date = fields.Date(string=_("Departure date"), index=True)
    