from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # Add new selection to `detailed_type` called `shoes`.
    detailed_type = fields.Selection(
        selection_add=[("shoes", "Shoes")],
        ondelete={"shoes": "set product"},
    )

    pairs_per_case = fields.Integer(string="Pairs per Case", default=0)
    price_per_pair = fields.Monetary(string="Price per Pair", default=0.0)

    list_price = fields.Float(
        compute="_compute_list_price",
        inverse="_inverse_list_price",
        store=True,
    )

    @api.constrains("pairs_per_case")
    def _check_pairs_per_case(self):
        for record in self:
            if record.pairs_per_case < 0:
                raise ValidationError("Pairs per case must be non-negative.")

    @api.constrains("price_per_pair")
    def _check_price_per_pair(self):
        for record in self:
            if record.price_per_pair < 0:
                raise ValidationError("Price per pair must be non-negative.")

    @api.depends("pairs_per_case", "price_per_pair")
    def _compute_list_price(self):
        for record in self:
            if record.pairs_per_case or record.price_per_pair:
                record.list_price = record.pairs_per_case * record.price_per_pair

    def _inverse_list_price(self):
        for record in self:
            if record.list_price:
                record.pairs_per_case, record.price_per_pair = 1, record.list_price

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping["shoes"] = "product"
        return type_mapping
