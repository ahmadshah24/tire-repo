from odoo import models, fields, api


class Stock(models.Model):
    _name = 'stock.stock'
    _description = 'new tire stock'
    # _rec_name ='tname'

    name=fields.Char("Tire Name")
    no = fields.Char("NO ")
    type = fields.Char("Type")
    cost = fields.Float("Per Cost")
    amount = fields.Integer("Amount")
    total = fields.Float(string='Total', compute='_total_amount')
    cname = fields.Char("Costumer Name")
    billNo = fields.Char("Bill NO")
    date = fields.Date("Date")
    ccost = fields.Float("Per Cost")
    camount = fields.Integer("Amount")
    ctotal = fields.Float(string='Total', compute='_ctotal_amount')
    reminder = fields.Char("Matrail Reminder")
    mreminder = fields.Char("Money Reminder")
    active = fields.Boolean('Active', default=True)

    
    @api.depends('amount','cost')
    def _total_amount(self):
            for line in self:
                line.total = line.amount * line.cost

    @api.depends('camount','ccost')
    def _ctotal_amount(self):
            for line in self:
                line.ctotal = line.camount * line.ccost