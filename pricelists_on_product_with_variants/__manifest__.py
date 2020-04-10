# -*- coding: utf-8 -*-
#################################################
{
  "name"                 :  "Pricelists On Product With Variants",
  "category"             :  "Sales Management",
  "version"              :  "1.0",
  "author"               :  "E3K Gestion Globale SENC",
  "website"              :  "https://www.e3k.co",
  "support"              :  "support@e3k.co",
  "summary"              :  "Take control of the pricelists directly from the product view.",
  "description"          : '''
             When using variants with multiple price lists it can be hard to keep track of the pricing of your items. 

This module allows you to have a global view of all your pricing for an item and it's variants. It also lets you use the full detailled item price form directly from the product view so you don't have to go to the settings page to manage the pricing for the product or it's variants.''',
  "depends"              :  ['base','product'],
  "data"                 :  [
                              'views/product_view.xml',
                            ],
  "images"               :  ["static/description/banner.png"],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  19,
  "currency"             : "EUR",
  "license"              : "OPL-1"
}