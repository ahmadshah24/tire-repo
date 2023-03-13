from odoo import models, fields, api


class SaleLine(models.Model):
    _name = 'atlas.sale.line'
    _description = 'new tire sale line '
    _rec_name ='product_id'

    quantity = fields.Integer("Quantity")
    price = fields.Float("Unit Price")
    total = fields.Float(string='Total', compute='_total_amount')
    product_id =fields.Many2one("atlas.product")
    sale_id=fields.Many2one("atlas.sale")
    active = fields.Boolean('Active', default=True)


    product_ids=fields.One2many("atlas.product","sale_id")


    @api.depends('quantity','price')
    def _total_amount(self):
            for line in self:
                line.total = line.quantity * line.price

    



