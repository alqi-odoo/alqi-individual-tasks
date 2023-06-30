from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    site_address = fields.Many2one(comodel_name='res.partner')

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['site_address'] = self.site_address.id
        return invoice_vals
