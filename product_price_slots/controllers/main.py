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

from odoo import http
from odoo.http import request


import logging
_logger = logging.getLogger(__name__)


class ProductPriceSlot(http.Controller):

    @http.route(['/product/price/slot'], type='json', auth="public", website=True)
    def load_product_price_slot(self, product_id=False, **kwargs):
        values = {
            'wk_product_id': product_id,
        }
        return request.env.ref("product_price_slots.wk_product_price_offer").render(values, engine='ir.qweb')

    @http.route(['/product/price/subtotal'], type='json', auth="public", website=True)
    def load_product_price_subtotal(self, product_id=False, add_qty=False, **kwargs):
        values = {}
        if product_id and add_qty > 0:
            values['default_price_subtotal'] = (request.env['product.product'].browse(product_id).website_public_price) * add_qty
            values['price_subtotal'] = request.env['product.product'].with_context({'quantity': add_qty}).browse(product_id).website_price
        return values