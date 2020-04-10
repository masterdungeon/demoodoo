# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# See LICENSE file for full copyright and licensing details.
# License URL : <https://store.webkul.com/license.html/>
##############################################################################


import base64

from odoo import _, api, fields, models
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
from odoo.tools.mimetypes import guess_mimetype


class SaleOptionSelectionWizard(models.TransientModel):
    _name = "sale.option.selection.wizard"
    _description = "Sales Custom Option Selection"

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

    custom_option_id = fields.Many2one(
        'product.custom.options', string="Custom Option")
    order_line_id = fields.Many2one(
        'sale.order.line', string="Order Line")
    prod_tmpl_id = fields.Many2one(
        'product.template',related="order_line_id.product_id.product_tmpl_id", string='Product Template')
    input_type = fields.Selection(_get_input_type, related="custom_option_id.input_type",
        string="Input Type", help="Input type for the custom option.")

    text_input = fields.Char(string="Input (Text)")
    area_input = fields.Text(string="Input (Area)")
    date_input = fields.Date(string="Input (Date)")
    datetime_input = fields.Datetime(string="Input (Datetime)")
    radio_input = fields.Many2one("product.custom.options.value", string="Input (Radio)")
    dropdown_input = fields.Many2one("product.custom.options.value", string="Input (Dropdown)")
    multi_input = fields.Many2many("product.custom.options.value", "product_multi_input_rel", string="Input (Multiple)")
    checkbox_input = fields.Many2many("product.custom.options.value", "product_checkbox_input_rel", string="Input (Checkbox)")
    file_input = fields.Binary(string="Input (File)")

    price = fields.Float(string="Price", digits=dp.get_precision('Product Price'),
        help="Price for the custom option.")


    # @api.multi
    def add_option(self):
        optionObj = self.custom_option_id
        optionType = self.input_type
        price = 0.00
        inputData = ''
        if optionType == 'field':
            inputData = str(self.text_input)
            price = optionObj.price
        elif optionType == 'area':
            inputData = str(self.area_input)
            price = optionObj.price
        elif optionType == 'date':
            inputData = str(self.date_input)
            price = optionObj.price
        elif optionType == 'date_time':
            inputData = str(self.datetime_input)
            price = optionObj.price
        elif optionType == 'radio':
            inputData = self.radio_input.name
            price = self.radio_input.price
        elif optionType == 'drop_down':
            inputData = self.dropdown_input.name
            price = self.dropdown_input.price
        elif optionType == 'multiple':
            inputData = ', '.join(self.multi_input.mapped('name'))
            price = sum(self.multi_input.mapped('price'))
        elif optionType == 'checkbox':
            inputData = ', '.join(self.checkbox_input.mapped('name'))
            price = sum(self.checkbox_input.mapped('price'))
        elif optionType == 'file':
            inputData = "File Input"
            price = optionObj.price
            # mimetype = guess_mimetype(base64.b64decode(self.file_input))
            # allowed_file_extention = optionObj.allowed_file_extention
            # if mimetype not in allowed_file_extention.split(','):
            #     raise UserError("File is not valid...!!! \nOnly files with extension {} are allowed.".format(allowed_file_extention))

        description_ids = self.order_line_id.sale_options_ids.filtered(
            lambda r: r.custom_option_id == optionObj)
        if description_ids:
            description_id = description_ids[0]
            description_id.update({
                'input_data': inputData,
                'file_data': self.file_input,
                'price': price,
            })
        else:
            newId = self.order_line_id.sale_options_ids.new({
                'custom_option_id': optionObj.id,
                'order_line_id': self.order_line_id.id,
                'input_data': inputData,
                'price': price,
                'file_data': self.file_input,
            })
            self.order_line_id.sale_options_ids += newId

        return {
            'name': ("Information"),
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'sale.order.line',
            'view_id': self.env.ref('product_custom_options.sale_order_line_custom_options_form').id,
            'res_id': self.order_line_id.id,
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'new',
            'domain': '[]',
        }

    # @api.multi
    def cancel_action(self):
        return {
            'name': ("Information"),
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'sale.order.line',
            'view_id': self.env.ref('product_custom_options.sale_order_line_custom_options_form').id,
            'res_id': self.order_line_id.id,
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'new',
            'domain': '[]',
        }
