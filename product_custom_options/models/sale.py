# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################


from odoo import _, api, fields, models
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    is_custom_product = fields.Boolean("Have custom options")

    sale_options_ids = fields.One2many(
        'sale.custom.options', 'order_line_id',string="Custom Options")
    sale_options_price = fields.Float(string="Price",
        compute='_compute_options_price',
        digits=dp.get_precision('Product Price'),
        help="Price for the custom option.")

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id.custom_option_ids:
            self.is_custom_product = True
        else:
            self.is_custom_product = False

    # @api.multi
    def _compute_options_price(self):
        for line in self:
            line.sale_options_price = sum(line.sale_options_ids.mapped('price'))

    # @api.multi
    def configure_product(self):
        productObj = self.product_id
        if productObj.custom_option_ids:
            return {
                'name': ("Information"),
                'view_mode': 'form',
                'view_type': 'form',
                'res_model': 'sale.order.line',
                'view_id': self.env.ref('product_custom_options.sale_order_line_custom_options_form').id,
                'res_id': self.id,
                'type': 'ir.actions.act_window',
                'nodestroy': True,
                'target': 'new',
                'domain': '[]',
            }

    # @api.multi
    def add_option(self):
        productObj = self.product_id
        if productObj.custom_option_ids:
            wizardObj = self.env['sale.option.selection.wizard'].create({'order_line_id': self.id})
            return {
                'name': ("Information"),
                'view_mode': 'form',
                'view_type': 'form',
                'src_model': 'sale.order.line',
                'res_model': 'sale.option.selection.wizard',
                'view_id': self.env.ref('product_custom_options.sale_option_selection_wizard_form').id,
                'res_id': wizardObj.id,
                'type': 'ir.actions.act_window',
                'nodestroy': True,
                'target': 'new',
            }

    # @api.multi
    def save_option(self):
        price_unit = 0.00
        product = self.product_id.with_context(
            lang=self.order_id.partner_id.lang,
            partner=self.order_id.partner_id.id,
            quantity=self.product_uom_qty,
            date=self.order_id.date_order,
            pricelist=self.order_id.pricelist_id.id,
            uom=self.product_uom.id
        )
        name = product.name_get()[0][1]
        if product.description_sale:
            name += '\n' + product.description_sale
        if self.order_id.pricelist_id and self.order_id.partner_id:
            if self.order_id.pricelist_id.discount_policy == 'with_discount'  or 'wk_source' not in self._context:
                price_unit = self.env['account.tax']._fix_tax_included_price_company(self._get_display_price(product), product.taxes_id, self.tax_id, self.company_id)
            else:
                price_unit = self.env['account.tax']._fix_tax_included_price_company(product.price, product.taxes_id, self.tax_id, self.company_id)
        if self.sale_options_ids:
            from_currency = self.order_id.company_id.currency_id
            sale_options_price = self.sale_options_price
            if self.order_id.pricelist_id.discount_policy == 'with_discount' or 'wk_source' in self._context:
                pricelistId = self.order_id.pricelist_id.id
                ruleId = self.product_id.product_tmpl_id._get_suitable_price_rule(pricelistId)
                sale_options_price = self.env['product.template']._get_pricelist_based_price(
                    ruleId, sale_options_price)
            tmp = from_currency.compute(
                sale_options_price, self.order_id.pricelist_id.currency_id)
            price_unit += tmp
            description = self.sale_options_ids.mapped(
                lambda option: option.custom_option_id.name+': '+option.input_data)
            if description:
                name +='\n'+'\n'.join(description)
        self.name = name
        self.price_unit = price_unit
