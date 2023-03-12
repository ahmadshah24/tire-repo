# -*- coding: utf-8 -*-

from odoo import models, fields, api


class new(models.Model):
    _name = 'new.new'
    _description = 'new tire '
    _rec_name ='billNo'

    no = fields.Char("NO ")
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    Cname = fields.Char("Costumer Name")
    total = fields.Integer("Total")




    return_id =fields.One2many("return.return","sale_id")


    