
from odoo import models, fields, api


class Purchase(models.Model):
    _name = 'atlas.purchase'
    _description = 'new tire purchase'
    _rec_name="invoice"


    invoice = fields.Char("Invoic No")
    date = fields.Date("Date")
    amount=fields.Float("Amount")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
   

    vender_id = fields.Many2one("vender.vender")
    line_ids=fields.One2many("atlas.purchase.line","purchase_id")

    @api.constrains('line_ids')
    def _total_bill(self):
        if any(self.line_ids):
            total = 0
            for line in self.line_ids:
                total = total + line.total
            self.amount = total




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

    