from odoo import models, fields, api


class Takes(models.Model):
    _name = 'take.take'
    _description = 'new tire take '
    _rec_name ='no'

    no = fields.Char("NO ")
    check = fields.Char("Check No")
    date = fields.Date("Date")
    amount = fields.Integer("Amount")
    # total = fields.Integer("Total ")
    active = fields.Boolean('Active', default=True)





    # @api.depends('amount')
    # def _total_amount(self):
    #         for line in self:
    #             line.total = line.amount + line.amount
