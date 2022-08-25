# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kki_sale_management(models.Model):
    _inherit = "sale.order"

    memo = fields.Text()

    note = fields.Char("ノート")

    x_selection = fields.Selection([
        ('1', 'いち'),
        ('2', 'に'),
        ('3', 'さん'),
        ('4', 'よん'),
    ], default='',
        string="選択", )
    x_m2o = fields.Many2one("res.partner",string="名簿")
#     name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float()
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
