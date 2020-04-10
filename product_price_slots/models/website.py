# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# License URL : https://store.webkul.com/license.html/
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################

from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = 'website'

    @api.model
    def check_partner_country_eligiblity_for_pricelist(self, partner, pricelist):
        if not partner:
            partner = self.env.user.partner_id
        if not pricelist:
            return False
        partner_country = partner.country_id
        if pricelist.country_group_ids:
            if partner_country:
                for country_group in pricelist.country_group_ids:
                    if not partner_country.id in country_group.country_ids.ids:
                        return False
        return True

    @api.model
    def get_all_child_category(self, product):
        categ_ids = {}
        if product:
            categ = product.categ_id
            while categ:
                categ_ids[categ.id] = True
                categ = categ.parent_id
        categ_ids = categ_ids.keys()
        return categ_ids

    @api.model
    def is_valid_pli(self, pricelist_item):
        if not pricelist_item:
            return False
        start_date = fields.Date.from_string(pricelist_item.date_start) if pricelist_item.date_start else False
        end_date = fields.Date.from_string(pricelist_item.date_end) if pricelist_item.date_end else False
        today_date = fields.Date.from_string(fields.Date.today())
        if start_date and end_date and start_date <= today_date <= end_date:
            return True
        elif not start_date and not end_date:
            return True
        elif start_date and not end_date and start_date <= today_date:
            return True
        elif not start_date and end_date and today_date <= end_date:
            return True
        else:
            return False

    @api.model
    def get_pli_for_product(self, pricelist_obj, product_tmpl_obj, product_id):
        pli_obj_list = []
        # if not pricelist_obj or not product_tmpl_obj or not product_id :
        #     return pli_obj_list
        for pli in pricelist_obj.item_ids.sorted(key=lambda p: p.min_quantity):
            if ((pli.applied_on == '3_global') or (pli.applied_on == '2_product_category' and pli.categ_id.id in self.get_all_child_category(product_tmpl_obj)) or (pli.applied_on == '1_product' and pli.product_tmpl_id == product_tmpl_obj) or (pli.applied_on == '0_product_variant' and pli.product_id.id == int(product_id))) and self.is_valid_pli(pli):
                pli_obj_list.append(pli)
        return pli_obj_list

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    show_price_per_100g = fields.Boolean("Show price per 100g",default=False)
