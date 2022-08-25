from odoo import models, fields, api


class kki_forklift2(models.Model):
    _name = 'kki_forklift2.forklift2'
    _description = 'kki_forklift2.forklift2'

    name = fields.Char("name")
    image = fields.Binary("image")