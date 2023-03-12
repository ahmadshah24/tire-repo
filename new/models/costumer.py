from odoo import models, fields, api


class Costumer(models.Model):
    _name = 'costumer.costumer'
    _description = 'new tire costumer '



    name=fields.Char("Name")
    no = fields.Char("NO")
    billNo = fields.Char("Bill No")
    tireType = fields.Char("Tire Type")
    tubeType = fields.Char("Tube Type")
    amount = fields.Integer("Amount")
    cost = fields.Float("Per Cost")
    total = fields.Float(string='Total', compute='_total_amount')
    reminder = fields.Float(string='Reminder', compute='_total_reminder')


    rasid_ids = fields.One2many("crasidat.crasidat","costumer_id")
    
    


    @api.depends('amount','cost')
    def _total_amount(self):
            for line in self:
                line.total = line.amount * line.cost


    @api.depends('total')
    def _total_reminder(self):
            for line in self:
                line.reminder = line.total - line.total




# @api.constrains('line_ids')
#     def _total_amount(self):
#             amount = 0
#             for line in self.line_ids:
#                 amount = amount + line.amount
#             self.amount = amount
