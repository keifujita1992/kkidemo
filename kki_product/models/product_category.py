# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_product_category(models.Model):
    _name = 'product_category'
    _description = 'product_category'

    name = fields.Char("category")
