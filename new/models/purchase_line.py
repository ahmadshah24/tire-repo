

from odoo import models, fields, api


class PurchaseLine(models.Model):
    _name = 'atlas.purchase.line'
    _description = 'new tire purchase line'
    _rec_name="product_id"
  
    quantity = fields.Integer("Quantity")
    price = fields.Float("Price")
    total = fields.Float(string='Total', compute='_total_amount')
    active = fields.Boolean('Active', default=True)

    product_id=fields.Many2one("atlas.product")
    purchase_id=fields.Many2one("atlas.purchase")


    @api.depends('quantity','price')
    def _total_amount(self):
            for line in self:
                line.total = line.quantity * line.price
