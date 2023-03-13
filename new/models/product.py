from odoo import models, fields, api


class Product(models.Model):
    _name = 'atlas.product'
    _description = 'new tire product '


    name = fields.Char("Name")
    type = fields.Char("type")
    size = fields.Char("Size")
    pattern = fields.Char("Pattern")
    pr = fields.Char("PR")
    active = fields.Boolean('Active', default=True)
 
    # return_id =fields.One2many("return.return","sale_id")

    sale_id=fields.Many2one("atlas.sale")
    


    