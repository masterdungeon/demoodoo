# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
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
  "name"                 :  "Product Custom Options",
  "summary"              :  "Odoo Product Custom Options facilitates you to set manage variants for your products without making their variants through custom options.",
  "category"             :  "Sales",
  "version"              :  "1.1.4",
  "sequence"             :  "1",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-Product-Custom-Options.html",
  "description"          :  """Manage variants
Create product variants
Product Custom Options in Odoo
Odoo Product Custom options
Custom options for product
Customization for products in Odoo
Odoo product customization option
Website custom options
Set variants in Odoo
Option for product customization
Odoo website customization option
Marketplace custom options
Odoo Marketplace custom options
Options for customized products in Odoo
How to customize products in Odoo
""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=product_custom_options",
  "depends"              :  ['sale_management'],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'views/custom_options_views.xml',
                             'views/product_template_views.xml',
                             'views/sale_views.xml',
                             'wizard/option_selection_wizard_views.xml',
                            ],
  "demo"                 :  ['data/custom_options_demo.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "price"                :  45,
  "currency"             :  "EUR",
  "pre_init_hook"        :  "pre_init_check",
}