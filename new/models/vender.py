from odoo import models, fields, api


class Vender(models.Model):
    _name = 'vender.vender'
    _description = 'new tire take '

    name = fields.Char("Company Name ")
    address = fields.Char("Address")
    phone = fields.Char("phone")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")


