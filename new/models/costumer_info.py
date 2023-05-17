from odoo import models, fields, api


class CostumerInfo(models.Model):
    _name = 'costumerinfo.costumerinfo'
    _description = 'new tire costumer info'



    no =fields.Char("No")
    name=fields.Char("Name")
    phone = fields.Char("Phone")
    address = fields.Char("Address")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
    reminder = fields.Float("Reminder" ,compute='_reminder', store=True)
    returns = fields.Float("Return" ,readonly="1")
    sale = fields.Float("Sale", readonly="1")
    rasid=fields.Float("Rasidat", readonly="1")



    @api.depends('returns', 'sale','rasid')
    def _reminder(self):

        for rec in self:

            rec.update({

                'reminder': (rec.sale-rec.rasid)-rec.returns

            })


    