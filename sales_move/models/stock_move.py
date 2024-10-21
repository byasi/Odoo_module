from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class StockMove(models.Model):
    _inherit = 'stock.move'

    product_quality = fields.Float(string="Product Quality")

