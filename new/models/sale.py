# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Sale(models.Model):
    _name = 'atlas.sale'
    _description = 'new tire '
    _rec_name ='billNo'

    no = fields.Char("NO ")
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    Cname = fields.Char("Name")
    total = fields.Integer("Total")
    active = fields.Boolean('Active', default=True)




    return_id =fields.One2many("return.return","sale_id")

    costumer_id=fields.Many2one("costumerinfo.costumerinfo")


    