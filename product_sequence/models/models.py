# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class ProductProduct(models.Model):
    _inherit = 'product.product'

    sequence = fields.Integer('Sequence', default=1, help="The product variant sequence will determine which is the default variant.")
    _order = 'sequence'


