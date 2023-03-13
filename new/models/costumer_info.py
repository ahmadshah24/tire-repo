from odoo import models, fields, api


class CostumerInfo(models.Model):
    _name = 'costumerinfo.costumerinfo'
    _description = 'new tire costumer info'



    name=fields.Char("Name")
    phone = fields.Char("Phone")
    address = fields.Char("Address")
    active = fields.Boolean('Active', default=True)
    