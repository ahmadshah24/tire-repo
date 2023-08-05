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
    sales_ids = fields.One2many('atlas.sale', 'costumer_id')
    sale_count = fields.Integer(string='Number of Sales', compute='_compute_sale_count', related='sales_ids.id', store=False)

    @api.depends('sales_ids')
    def _compute_sale_count(self):
        for customer in self:
            customer.sale_count = len(customer.sales_ids)

    def action_show_sales(self):
        for rec in self:
            return {
                'name': 'Sales to this customer',
                'type': 'ir.actions.act_window',
                'view_mode': 'tree,form',
                'res_model': 'atlas.sale',
                'domain': [('id', 'in', rec.sales_ids.ids)],
                'context': {
                'default_costumer_id': rec.sales_ids.id,
                },
            }








    @api.depends('returns', 'sale','rasid')
    def _reminder(self):

        for rec in self:

            rec.update({

                'reminder': (rec.sale-rec.rasid)-rec.returns

            })


    