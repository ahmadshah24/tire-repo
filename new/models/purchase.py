
from odoo import models, fields, api


class Purchase(models.Model):
    _name = 'atlas.purchase'
    _description = 'new tire purchase'
    _rec_name="invoice"


    invoice = fields.Char("Invoic No")
    no = fields.Char("NO ")
    date = fields.Date("Date")
    active = fields.Boolean('Active', default=True)
   

    vender_id = fields.Many2one("vender.vender")