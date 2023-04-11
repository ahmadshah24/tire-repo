from odoo import models, fields, api


class Return(models.Model):
    _name = 'return.return'
    _description = 'new tire return '
    _rec_name ='billNo'

    no = fields.Char("NO ")
    billNo = fields.Char("Bill No")
    date = fields.Date("Date")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
    quantity = fields.Integer("Quantity")
    price = fields.Float("Unit Price")
    total = fields.Float(string='Total', compute='_total_amount', store=True)

    sale_id =fields.Many2one("new.new")
    costumer_id=fields.Many2one("costumerinfo.costumerinfo")
    product_id=fields.Many2one("atlas.product")
    

    @api.constrains('total')
    def calculate_costumer_return(self):
        self.env['atlas.sale'].costumer_calculations(self.costumer_id)


    @api.constrains('quantity')
    def calc_return_quantity_onhand(self):
        
        for rec in self:
            product_obj = self.env['atlas.product'].search([('id', '=', rec.product_id.id)])
            current_quantity_onhand = product_obj.quantity_onhand
            product_obj.write({'quantity_onhand': current_quantity_onhand + rec.quantity})



    @api.depends('quantity', 'price')
    def _total_amount(self):

        for rec in self:

            rec.update({

                'total': rec.quantity*rec.price,

            })