# -*- coding: utf-8 -*-

from odoo import api, fields, models


class BinLocation(models.Model):
    _name = 'bin.location'
    _description = 'Bin Location'
    _rec_name = 'bin_name'

    # attributes
    bin_name = fields.Char('Name')