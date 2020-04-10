# -*- coding: utf-8 -*-
#################################################################################/home/amine/Documents/positech-tests/.gitignore
from odoo import api, fields, models, _


class PricelistItem(models.Model):
    _inherit = "product.pricelist.item"
    _description = "Pricelist Item"

    @api.depends('pricelist_id')
    def _compute_product_list(self):
        for object in self:
            cr = self._cr
            product_list = []
            product_tmpl_id=False
            if object.product_tmpl_id:
                product_tmpl_id=object.product_tmpl_id.id
                if not isinstance(product_tmpl_id, int):
                    product_tmpl_id = False

            if not product_tmpl_id:
                product_tmpl_id = self._context.get('default_product_tmpl_id')

            if product_tmpl_id:
                query = 'SELECT id FROM product_product WHERE product_tmpl_id=%s'
                cr.execute(query, (product_tmpl_id,))
                for row in cr.fetchall():
                    product_list.append(row[0])
                object.product_list = [(6, 0, product_list)]

    @api.depends('pricelist_id')
    def _compute_is_product_list(self):
        for object in self:
            if object.product_list and len(object.product_list.ids) == 1:
                object.is_product_list = True
            else:
                object.is_product_list = False

    @api.depends('pricelist_id')
    def _compute_is_price_list_required(self):
        for object in self:
            if not self._context.get('show_price_list'):
                object.is_price_list_required = False
            else:
                object.is_price_list_required = True

    product_list = fields.Many2many('product.product', string="Products", compute='_compute_product_list',
                                    store=False)
    is_product_list = fields.Boolean('is_product_list', default=False, compute='_compute_is_product_list')
    is_price_list_required = fields.Boolean('is_price_list_required', default=False, compute='_compute_is_price_list_required')


    @api.onchange('pricelist_id')
    def _onchange_pricelist_id(self):
        domain={}
        if self.product_list:
            #product_tmpl_id=self.product_list[0].product_tmpl_id.id
            domain['product_id'] = [('id', '=', self.product_list.ids)]
            return {'domain': domain}
