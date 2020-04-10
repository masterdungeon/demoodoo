# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################

from odoo import api, fields, models, tools
from odoo.tools import pycompat


class ProductTemplate(models.Model):
    _inherit = "product.template"

    custom_option_ids = fields.One2many(
        'product.custom.options', 'prod_tmpl_id',
        string='Custom Options')

    # @api.multi
    def _get_suitable_price_rule(self, pricelistId):
        self.ensure_one()
        rules = {}
        pricelistEnv = self.env['product.pricelist']
        if pricelistId:
            pricelist = None
            partner = self._context.get('partner', False)
            quantity = self._context.get('quantity', 1.0)

            pricelist = pricelistEnv.browse(pricelistId)
            quantities = [quantity] * len(self)
            partners = [partner] * len(self)

            rules = {
                product_id: res_tuple[1]
                for product_id, res_tuple in pricelist._compute_price_rule(
                    list(pycompat.izip(self, quantities, partners))
                ).items()
            }
        return rules.get(self.id, False)

    @api.model
    def _get_pricelist_based_price(self, ruleId, price):
        rule = self.env['product.pricelist.item'].browse(ruleId)
        if rule.compute_price == 'fixed':
            price = 0.00
        elif rule.compute_price == 'percentage':
            price = (price - (price * (rule.percent_price / 100))) or 0.0
        else:
            # complete formula
            price_limit = price
            price = (price - (price * (rule.price_discount / 100))) or 0.0
            if rule.price_round:
                price = tools.float_round(price, precision_rounding=rule.price_round)
        return price

    # @api.multi
    def _get_pricelist_based_price_data(self, priceData, pricelistId):
        self.ensure_one()
        ruleId = self._get_suitable_price_rule(pricelistId)
        newPriceData = priceData.copy()
        if ruleId:
            for optionId, optionPrice in priceData.items():
                if optionPrice is not False:
                    optionPrice = self._get_pricelist_based_price(ruleId, optionPrice)
                newPriceData.update({optionId: optionPrice})
        return newPriceData

    def fetch_taxed_price(self, price, qty=1, company=False):
        partner = self.env.user.partner_id

        ret = self.env.user.has_group('sale.group_show_price_subtotal') and 'total_excluded' or 'total_included'
        taxes = partner.property_account_position_id.map_tax(self.sudo().taxes_id.filtered(lambda x: x.company_id == company))
        newPrice = taxes.compute_all(price, quantity=qty, partner=partner)[ret]

        return newPrice

    # @api.multi
    def get_option_data(self, pricelist, company, price_with_pricelist=True):
        self.ensure_one()
        pricelistId = pricelist.id
        toCurrency = pricelist.currency_id

        optionData = {}
        for option in self.custom_option_ids:
            if toCurrency != self.currency_id:
                price = self.currency_id.compute(option.price, toCurrency)
            else:
                price = option.price
            price = self.fetch_taxed_price(price=price, company=company)
            optionData.update({option.id:price})

        optionValueData = {}
        for optionValue in self.custom_option_ids.mapped('custom_options_value_ids'):
            if toCurrency != self.currency_id:
                price = self.currency_id.compute(optionValue.price, toCurrency)
            else:
                price = optionValue.price
            price = self.fetch_taxed_price(price=price, company=company)
            optionValueData.update({optionValue.id:price})

        if price_with_pricelist:
            optionData = self._get_pricelist_based_price_data(optionData, pricelistId)
            optionValueData = self._get_pricelist_based_price_data(optionValueData, pricelistId)

        return [optionData,optionValueData]
