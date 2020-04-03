# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_bin_location_ids = fields.Many2many('bin.location', 'product_bin_location_rel', string='Bin Locations')