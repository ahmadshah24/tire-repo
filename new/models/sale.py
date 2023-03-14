# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sale(models.Model):
    _name = 'atlas.sale'
    _description = 'new tire '

    name=fields.Char()
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    Cname = fields.Char("Name")
    amount=fields.Float("Amount")
    active = fields.Boolean('Active', default=True)
    des = fields.Char("Description")
 
    line_ids =fields.One2many('atlas.sale.line','sale_id')

    costumer_id=fields.Many2one("costumerinfo.costumerinfo")

    


    @api.constrains('line_ids')
    def _total_bill(self):
        if any(self.line_ids):
            total = 0
            for line in self.line_ids:
                total = total + line.total
            self.amount = total


class SaleLine(models.Model):

    _name = 'atlas.sale.line'
    _description = 'new tire sale line '
    _rec_name ='product_id'

    quantity = fields.Integer("Quantity")
    price = fields.Float("Unit Price")
    total = fields.Float(string='Total', compute='_total_amount', store=True)
    active = fields.Boolean('Active', default=True)
    date=fields.Date("Date")

    sale_id=fields.Many2one('atlas.sale')
    product_id =fields.Many2one("atlas.product")
    
    # product_ids=fields.One2many("atlas.product","sale_id")


    @api.depends('quantity', 'price')
    def _total_amount(self):

        for rec in self:

            rec.update({

                'total': rec.quantity*rec.price,

            })
 