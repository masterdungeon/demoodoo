# -*- coding: utf-8 -*-

{
  "name"                 :  "Bin Management",
  "summary"              :  "Bin Management.",
  "category"             :  "Inventory",
  "version"              :  "1.0.0",
  "author"               :  "Prolitus Technologies Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "depends"              :  [
                             'stock'
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'views/bin_location_view.xml',
                             'views/product_template_view.xml',
                             'report/report_stock_picking_operations_inherit.xml'
                            ],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}