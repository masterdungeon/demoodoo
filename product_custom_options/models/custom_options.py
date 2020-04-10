# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################


from odoo import _, api, fields, models
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError


class ProductCustomOptions(models.Model):
    _name = "product.custom.options"
    _description = "Product Custom Options"
    _order = 'prod_tmpl_id, sequence, id'

    def _get_input_type(self):
        return [
            ('field', 'Text Field'),
            ('area', 'Text Area'),
            ('date', 'Date'),
            ('date_time', 'Date & Time'),
            ('time', 'Time'),
            ('radio', 'Radio Button'),
            ('multiple', 'Multiple Select'),
            ('checkbox', 'Checkbox'),
            ('drop_down', 'Dropdown'),
            ('file', 'File'),
        ]

    name = fields.Char(string="Title", help="Title for the custom option.", required=True, translate=True)
    input_type = fields.Selection(_get_input_type,
        string="Input Type", help="Input type for the custom option.", required=True)
    is_required = fields.Boolean(string="Required", help="Is this a requierd option for this product.")
    prod_tmpl_id = fields.Many2one(
        'product.template', string='Product Template', required=True, ondelete='cascade')
    active = fields.Boolean(
        'Active', default=True,
        help="If unchecked, it will allow you to hide the option without removing it.")
    sequence = fields.Integer(string='Sequence', default=10)

    price = fields.Float(string="Price", digits=dp.get_precision('Product Price'),
        help="Price for the custom option.")
    custom_options_value_ids = fields.One2many(
        'product.custom.options.value', 'custom_option_id', string="Custom Options Values")

    # File related info
    allowed_file_extension = fields.Char(string="Allowed File Extensions", help="Comma separated file extensions like jpeg,png.")
    image_size_length = fields.Integer(string="Image Length", help="Maximum length allowed for Image.")
    image_size_width = fields.Integer(string="Image Width", help="Maximum width allowed for Image.")

    _sql_constraints = [
        ('name_tmpl_uniq', 'unique(name, prod_tmpl_id, input_type)', 'Custom option names must be unique per product & option type !'),
    ]

class ProductCustomOptionsValue(models.Model):
    _name = "product.custom.options.value"
    _description = "Product Custom Option Values"
    _order = 'custom_option_id, sequence, id'

    name = fields.Char(string="Title", help="Title for the custom option value.", required=True, translate=True)
    price = fields.Float(string="Price", digits=dp.get_precision('Product Price'),
        help="Price for the custom option value.")
    custom_option_id = fields.Many2one('product.custom.options',
        string="Custom Option", required=True, ondelete='cascade')
    is_default = fields.Boolean(string="Default Value", help="Is this a default option for this product.")
    sequence = fields.Integer(string='Sequence', default=10)

    _sql_constraints = [
        ('name_option_uniq', 'unique(name, custom_option_id)', 'Custom option value names must be unique per option !'),
    ]


class SaleCustomOptions(models.Model):
    _name = "sale.custom.options"
    _description = "Sales Custom Option"

    custom_option_id = fields.Many2one(
        'product.custom.options', string="Custom Option", required=True, ondelete='restrict')
    order_line_id = fields.Many2one(
        'sale.order.line', string="Order Line", required=True, ondelete='cascade', index=True)
    price = fields.Float(string="Price", digits=dp.get_precision('Product Price'),
        help="Price for the custom option value.")
    input_data = fields.Text(string="Input")
    file_data = fields.Binary(string="File Uploaded")
    file_preview = fields.Binary(related='file_data', string="File Preview")

    # @api.multi
    def remove(self):
        if self.order_line_id.state in ['cancel','done']:
            raise UserError("You can't remove an option when order is Locked or Cancelled.")
        orderLineId = self.order_line_id.id
        self.unlink()
        return {
            'name': ("Information"),
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'sale.order.line',
            'view_id': self.env.ref('product_custom_options.sale_order_line_custom_options_form').id,
            'res_id': orderLineId,
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'new',
            'domain': '[]',
        }
