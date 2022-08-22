# -*- coding: utf-8 -*-
# from odoo import http


# class Orderbook/(http.Controller):
#     @http.route('/orderbook//orderbook//', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/orderbook//orderbook//objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('orderbook/.listing', {
#             'root': '/orderbook//orderbook/',
#             'objects': http.request.env['orderbook/.orderbook/'].search([]),
#         })

#     @http.route('/orderbook//orderbook//objects/<model("orderbook/.orderbook/"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('orderbook/.object', {
#             'object': obj
#         })
