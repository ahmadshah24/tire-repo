from odoo import models, fields, api


class Rasidat(models.Model):
    _name = 'rasidat.rasidat'
    _description = 'new tire rasidat '
    _rec_name ='Cname'

    no = fields.Char("NO ")
    Cname = fields.Char("Costumer Name")
    date = fields.Date("Date")
    amount = fields.Integer("Amount")
    to = fields.Char("Reciver")


    
