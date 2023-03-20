from odoo import models, fields, api


class Return(models.Model):
    _name = 'return.return'
    _description = 'new tire return '
    _rec_name ='billNo'

    no = fields.Char("NO ")
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
    quantity = fields.Integer("Quantity")
    price = fields.Float("Unit Price")
    total = fields.Float(string='Total', compute='_total_amount', store=True)

    sale_id =fields.Many2one("new.new")
    costumer_id=fields.Many2one("costumerinfo.costumerinfo")
    product_id=fields.Many2one("atlas.product")

    





    @api.depends('quantity', 'price')
    def _total_amount(self):

        for rec in self:

            rec.update({

                'total': rec.quantity*rec.price,

            })