from odoo import models, fields, api


class Product(models.Model):
    _name = 'atlas.product'
    _description = 'new tire product '

    no=fields.Char("No")
    name = fields.Char("Name")
    type = fields.Char("type")
    size = fields.Char("Size")
    pattern = fields.Char("Pattern")
    pr = fields.Char("PR")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
    quantity_onhand = fields.Integer("On Hand Quantity")
 
 


    purchase_ids = fields.One2many('atlas.purchase', 'product_id')
    purchase_count = fields.Integer(string='Number of Returns', compute='_compute_purchase_count')
    @api.depends('purchase_ids')
    def _compute_purchase_count(self):
        for product in self:
            product.purchase_count = len(product.purchase_ids)

    def action_show_purchases(self):
        for rec in self:
            return {
                'name': 'purchase to this product',
                'type': 'ir.actions.act_window',
                'view_mode': 'tree,form',
                'res_model': 'atlas.purchase',
                'domain': [('id', 'in', rec.purchase_ids.line_ids.ids)],
            }