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

{
    "name"                 :  "Website: Product Slot Pricing",
    "summary"              :  "Show various product offers on product page.",
    "category"             :  "Website",
    "version"              :  "1.0.0",
    "sequence"             :  1,
    "author"               :  "Webkul Software Pvt. Ltd.",
    "license"              :  "Other proprietary",
    "website"              :  " ",
    "description"          :  """ """,
    "live_test_url"        :  "http://odoodemo.webkul.com/?module=product_price_slots&version=11.0",
    "depends"              :  ['website_sale'],
    "data"                 :  [
                                # 'views/website_template_view.xml', 
                                'views/product_view.xml'
                              ],
    "images"               :  ['static/description/Banner.png'],
    "application"          :  True,
    "installable"          :  True,
    "auto_install"         :  False,
    "price"                :  59,
    "currency"             :  "EUR",
    "pre_init_hook"        :  "pre_init_check",
}
