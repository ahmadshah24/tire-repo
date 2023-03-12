from odoo import models, fields, api


class Return(models.Model):
    _name = 'return.return'
    _description = 'new tire return '
    _rec_name ='billNo'

    no = fields.Char("NO ")
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    Cname = fields.Char("Costumer Name")
    total = fields.Integer("Total")


    sale_id =fields.Many2one("new.new")

    