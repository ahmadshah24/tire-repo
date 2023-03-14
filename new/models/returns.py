from odoo import models, fields, api


class Return(models.Model):
    _name = 'return.return'
    _description = 'new tire return '
    _rec_name ='billNo'

    no = fields.Char("NO ")
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    total = fields.Integer("Total")
    active = fields.Boolean('Active', default=True)
    des = fields.Char("Description")

    sale_id =fields.Many2one("new.new")
    costumer_id=fields.Many2one("costumerinfo.costumerinfo")

    