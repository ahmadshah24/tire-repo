from odoo import models, fields, api


class Rasidat(models.Model):
    _name = 'rasidat.rasidat'
    _description = 'new tire rasidat '
    _rec_name ='costumer_id'

    no = fields.Char("NO ")
    check = fields.Char("Check No")
    date = fields.Date("Date")
    amount = fields.Integer("Amount")
    to = fields.Char("Reciver")
    through = fields.Char("Through")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")


    costumer_id=fields.Many2one("costumerinfo.costumerinfo")


    
