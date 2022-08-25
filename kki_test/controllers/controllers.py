# -*- coding: utf-8 -*-
# from odoo import http


# class KkiTest(http.Controller):
#     @http.route('/kki_test/kki_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kki_test/kki_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('kki_test.listing', {
#             'root': '/kki_test/kki_test',
#             'objects': http.request.env['kki_test.kki_test'].search([]),
#         })

#     @http.route('/kki_test/kki_test/objects/<model("kki_test.kki_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kki_test.object', {
#             'object': obj
#         })
