# -*- coding: utf-8 -*-
# from odoo import http


# class KkiSaleManagement(http.Controller):
#     @http.route('/kki_sale_management/kki_sale_management/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_sale_management/kki_sale_management/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_sale_management.listing', {
#             'root': '/kki_sale_management/kki_sale_management',
#             'objects': http.request.env['kki_sale_management.kki_sale_management'].search([]),
#         })

#     @http.route('/kki_sale_management/kki_sale_management/objects/<model("kki_sale_management.kki_sale_management"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_sale_management.object', {
#             'object': obj
#         })
