
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Purchase(models.Model):
    _name = 'atlas.purchase'
    _description = 'new tire purchase'
    _rec_name="invoice"


    invoice = fields.Char("Invoic No")
    date = fields.Date("Date")
    amount=fields.Float("Amount")
    active = fields.Boolean('Active', default=True)
    des = fields.Text("Description")
   

    vender_id = fields.Many2one("vender.vender")
    line_ids=fields.One2many("atlas.purchase.line","purchase_id")

    @api.constrains('line_ids')
    def _total_bill(self):
        if any(self.line_ids):
            total = 0
            for line in self.line_ids:
                total = total + line.total
            self.amount = total
        elif not any(self.line_ids):
            raise ValidationError("Sorry! you have not enterded any item to purchase")
        self.write({"state":"approved"})

    state = fields.Selection(
        [('draft', 'Draft'),
         ('approved', 'Approved'),
        ], 'Status', default='draft', readonly=True,
        help='Choose whether the investment is still approved or not')
    
    def action_draft(self):
        self.write({'state':'draft'})

    def action_approved(self):
        self.write({'state': 'approved'})

    def action_approved(self):
        for line in self.line_ids:
            current_onhand = line.product_id.quantity_onhand

            line.product_id.write({'quantity_onhand': current_onhand+line.quantity})
        self.write({'state': 'approved'})

class PurchaseLine(models.Model):
    _name = 'atlas.purchase.line'
    _description = 'new tire purchase line'
    _rec_name="product_id"
  
    quantity = fields.Integer("Quantity")
    price = fields.Float("Price")
    total = fields.Float(string='Total', compute='_total_amount')
    active = fields.Boolean('Active', default=True)

    product_id=fields.Many2one("atlas.product")
    purchase_id=fields.Many2one("atlas.purchase")


    @api.depends('quantity','price')
    def _total_amount(self):
            for line in self:
                line.total = line.quantity * line.price

    
 

    