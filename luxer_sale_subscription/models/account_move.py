from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    site_address = fields.Many2one(comodel_name='res.partner')
