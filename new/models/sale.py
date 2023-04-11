# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Sale(models.Model):
    _name = 'atlas.sale'
    _description = 'new tire '

    name=fields.Char()
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    Cname = fields.Char("Name")
    amount=fields.Float("Amount")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
 
    line_ids =fields.One2many('atlas.sale.line','sale_id')

    costumer_id=fields.Many2one("costumerinfo.costumerinfo")

    state = fields.Selection(
        [('draft', 'Draft'),
         ('approved', 'Approved'),
        ], 'Status', default='draft', readonly=True,
        help='Choose whether the investment is still approved or not')

 

    def action_approved(self):
        for line in self.line_ids:
            current_onhand = line.product_id.quantity_onhand

            line.product_id.write({'quantity_onhand': current_onhand-line.quantity})
        if not any(self.line_ids):
            raise ValidationError("Sorry! you have not enterded any item to sale")
        self.write({"state":"approved"})
        

    @api.constrains('line_ids')
    def _total_bill(self):
        if any(self.line_ids):
            total = 0
            for line in self.line_ids:
                total = total + line.total
            self.amount = total


    @api.constrains('amount')
    def calculate_costumer_sale(self):
        self.env['atlas.sale'].costumer_calculations(self.costumer_id)
    product_id=fields.Many2one("atlas.product")
 
    @api.constrains('amount')
    def check_quantity_onhand(self):
        for rec in self:
            product_obj = self.env['atlas.product'].search([('id', '=', rec.product_id.id)])
            current_quantity_onhand = product_obj.quantity_onhand
            if product_obj.quantity_onhand < self.amount:
                    raise UserError('Not enough quantity of product!')

    
    @api.constrains('amount')
    def calc_costumer_calculations(self):
        for rec in self:
            self.costumer_calculations(self.costumer_id) 
    

    def costumer_calculations(self, costumer_id=False):
        domain = [('costumer_id', '=', costumer_id.id)]
        total_sales = 0
        total_rasids = 0
        total_returns = 0
        sale_ids = self.env['atlas.sale'].search(domain)
        rasid_ids = self.env['crasidat.crasidat'].search(domain)
        return_ids = self.env['return.return'].search(domain)
        for sale_rec in sale_ids:
            total_sales += (sale_rec.amount)     
        for rasid_rec in rasid_ids:
            total_rasids += rasid_rec.amount
        for return_rec in return_ids:
            total_returns += return_rec.total
        

        costumer_id.update({
            'sale':total_sales,
            'rasid':total_rasids,
            'returns':total_returns,
        })
    
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
     
    @api.depends('quantity', 'price')
    def _total_amount(self):
        for rec in self:
            rec.update({
                'total': rec.quantity*rec.price,
            })
 