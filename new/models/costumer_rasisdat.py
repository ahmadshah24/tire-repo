from odoo import models, fields, api


class CostumerRasidat(models.Model):
    _name = 'crasidat.crasidat'
    _description = 'new tire rasidat '

    no = fields.Char("NO")
    name = fields.Char("name")
    date = fields.Date("Date")
    check = fields.Date("Check No")
    amount = fields.Integer("Amount")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
    


    costumer_id=fields.Many2one("costumerinfo.costumerinfo")


    
