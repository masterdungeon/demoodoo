# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    nutrition = fields.Boolean(string="Nutrition", related="product_variant_ids.nutrition")
    country_of_origin = fields.Char(string="Country of Origin", related="product_variant_ids.country_of_origin")
    directions_of_use = fields.Text(string="Directions of Use and Storage", related="product_variant_ids.directions_of_use")
    ingredients = fields.Text(string="Ingredients", related="product_variant_ids.ingredients")
    allergen_info = fields.Text(string="Allergen Information", related="product_variant_ids.allergen_info")
    servings_per_package = fields.Float(string="Servings Per Package", related="product_variant_ids.servings_per_package")
    serving_size = fields.Char(string="Serving Size (g)", related="product_variant_ids.serving_size")
    energy_per_serve = fields.Float(string="Energy Per Serve (kJ)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.energy_per_serve")
    protein_per_serve = fields.Float(string="Protein Per Serve (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.protein_per_serve")
    fat_per_serve = fields.Float(string="Fat Per Serve (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.fat_per_serve")
    saturated_per_serve = fields.Float(string="Saturated Fat Per Serve (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.saturated_per_serve")
    carbohydrate_per_serve = fields.Float(string="Carbohydrate Per Serve (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.carbohydrate_per_serve")
    sugar_per_serve = fields.Float(string="Sugar Per Serve (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.sugar_per_serve")
    sodium_per_serve = fields.Float(string="Sodium Per Serve (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.sodium_per_serve")
    energy_per_100g = fields.Float(string="Energy Per 100g (kJ)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.energy_per_100g")
    protein_per_100g = fields.Float(string="Protein Per 100g (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.protein_per_100g")
    fat_per_100g = fields.Float(string="Fat Per 100g (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.fat_per_100g")
    saturated_per_100g = fields.Float(string="Saturated Fat Per 100g (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.saturated_per_100g")
    carbohydrate_per_100g = fields.Float(string="Carbohydrate Per 100g (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.carbohydrate_per_100g")
    sugar_per_100g = fields.Float(string="Sugar Per 100g (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.sugar_per_100g")
    sodium_per_100g = fields.Float(string="Sodium Per 100g (g)", digits=dp.get_precision('Stock Weight'), related="product_variant_ids.sodium_per_100g")


    

class ProductProduct(models.Model):
    _inherit = 'product.product'

    nutrition = fields.Boolean(string="Nutrition")
    country_of_origin = fields.Char(string="Country of Origin")
    directions_of_use = fields.Text(string="Directions of Use and Storage")
    ingredients = fields.Text(string="Ingredients")
    allergen_info = fields.Text(string="Allergen Information")
    servings_per_package = fields.Float(string="Servings Per Package")
    serving_size = fields.Char(string="Serving Size (g)")
    energy_per_serve = fields.Float(string="Energy Per Serve (kJ)", digits=dp.get_precision('Stock Weight'))
    protein_per_serve = fields.Float(string="Protein Per Serve (g)", digits=dp.get_precision('Stock Weight'))
    fat_per_serve = fields.Float(string="Fat Per Serve (g)", digits=dp.get_precision('Stock Weight'))
    saturated_per_serve = fields.Float(string="Saturated Fat Per Serve (g)", digits=dp.get_precision('Stock Weight'))
    carbohydrate_per_serve = fields.Float(string="Carbohydrate Per Serve (g)", digits=dp.get_precision('Stock Weight'))
    sugar_per_serve = fields.Float(string="Sugar Per Serve (g)", digits=dp.get_precision('Stock Weight'))
    sodium_per_serve = fields.Float(string="Sodium Per Serve (g)", digits=dp.get_precision('Stock Weight'))
    energy_per_100g = fields.Float(string="Energy Per 100g (kJ)", digits=dp.get_precision('Stock Weight'))
    protein_per_100g = fields.Float(string="Protein Per 100g (g)", digits=dp.get_precision('Stock Weight'))
    fat_per_100g = fields.Float(string="Fat Per 100g (g)", digits=dp.get_precision('Stock Weight'))
    saturated_per_100g = fields.Float(string="Saturated Fat Per 100g (g)", digits=dp.get_precision('Stock Weight'))
    carbohydrate_per_100g = fields.Float(string="Carbohydrate Per 100g (g)", digits=dp.get_precision('Stock Weight'))
    sugar_per_100g = fields.Float(string="Sugar Per 100g (g)", digits=dp.get_precision('Stock Weight'))
    sodium_per_100g = fields.Float(string="Sodium Per 100g (g)", digits=dp.get_precision('Stock Weight'))
    

    
