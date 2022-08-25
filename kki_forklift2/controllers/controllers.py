# -*- coding: utf-8 -*-
# from odoo import http


# class KkiForklift2(http.Controller):
#     @http.route('/kki_forklift2/kki_forklift2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_forklift2/kki_forklift2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_forklift2.listing', {
#             'root': '/kki_forklift2/kki_forklift2',
#             'objects': http.request.env['kki_forklift2.kki_forklift2'].search([]),
#         })

#     @http.route('/kki_forklift2/kki_forklift2/objects/<model("kki_forklift2.kki_forklift2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_forklift2.object', {
#             'object': obj
#         })
