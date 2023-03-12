# -*- coding: utf-8 -*-
# from odoo import http


# class New(http.Controller):
#     @http.route('/new/new', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new/new/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('new.listing', {
#             'root': '/new/new',
#             'objects': http.request.env['new.new'].search([]),
#         })

#     @http.route('/new/new/objects/<model("new.new"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new.object', {
#             'object': obj
#         })
