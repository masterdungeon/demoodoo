# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE URL <https://store.webkul.com/license.html/> for full copyright and licensing details.
#################################################################################
from odoo import models, fields, api, _

class ProductProduct(models.Model):
    _inherit = 'product.product'

    length = fields.Char(
        string='Length',
    )
    width = fields.Char(
        string='Width',
    )
    height = fields.Char(
        string='Height',
    )

class MrpBom(models.Model):
    _inherit = 'mrp.bom'
    @api.constrains('product_id', 'product_tmpl_id', 'bom_line_ids')
    def _check_product_recursion(self):
        if False:
            raise ValidationError(_('BoM line product %s should not be same as BoM product.') % bom.display_name)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    route_ids = fields.Many2many('stock.location.route', 'stock_route_products',
        'product_id', 'route_id', 
        'Routes', domain="[('product_selectable', '=', True)]",
        help="Depending on the modules installed, this will allow you to define the route of the product: whether it will be bought, manufactured, MTO/MTS,...")
