from odoo import models, fields, api


class Stock(models.Model):
    _name = 'stock.stock'
    _description = 'new tire stock'

    name=fields.Char("Tire Name")
    no = fields.Char("NO ")
    cost = fields.Float("Per Cost")
    amount = fields.Integer("Amount")
    total = fields.Float(string='Total', compute='_total_amount')
    date = fields.Date("Date")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")

    costumer_id=fields.Many2one("costumerinfo.costumerinfo")
    product_id=fields.Many2one("atlas.product")
    
    line_ids =fields.One2many('atlas.stock.line','stock_id')

    @api.depends('amount','cost')
    def _total_amount(self):
            for line in self:
                line.total = line.amount * line.cost

 
class StockLine(models.Model):

    _name = 'atlas.stock.line'
    _description = 'new tire stock line '
    _rec_name ='product_id'

    billNo = fields.Char("Bill NO")
    cquantity = fields.Integer("Quantity")
    cprice = fields.Float("Unit Price")
    ctotal = fields.Float(string='Total', compute='_total_amount', store=True)
    date=fields.Date("Date")

    costumer_id=fields.Many2one("costumerinfo.costumerinfo")
    product_id =fields.Many2one("atlas.product")
    stock_id =fields.Many2one("stock.stock")
    

    @api.depends('cquantity', 'cprice')
    def _total_amount(self):

        for rec in self:

            rec.update({

                'ctotal': rec.cquantity*rec.cprice,

            })
 