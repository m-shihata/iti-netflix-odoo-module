# -*- coding: utf-8 -*-
import json
from odoo import http


class ItiNetflix(http.Controller):
    @http.route('/iti_netflix/movies', auth='public', methods=['GET'])
    def retreive_movies(self, **kw):
        movies = http.request.env['netflix.movies'].sudo().search([])
        return json.dumps([{'id': movie.id, 'name': movie.name} for movie in movies])

    @http.route('/iti_netflix/movies', auth='public', methods=['POST'])
    def create_movie(self, **kw):
        return json.dumps({'3': 'movie3'})

    @http.route('/iti_netflix/movies/sync', auth='public', methods=['POST'], csrf=False)
    def sync_movies(self, **kw):
        new_movies = http.request.env['netflix.movies'].sudo()._sync_movies()
        return json.dumps([movie.id for movie in new_movies])

    @http.route('/iti_netflix/categories', auth='public', methods=['GET'])
    def retrieve_categories(self, **kw):
        categories = http.request.env['netflix.movies.categories'].sudo().search([])
        return json.dumps([category.name for category in categories])

#     @http.route('/iti_netflix/iti_netflix/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('iti_netflix.listing', {
#             'root': '/iti_netflix/iti_netflix',
#             'objects': http.request.env['iti_netflix.iti_netflix'].search([]),
#         })

#     @http.route('/iti_netflix/iti_netflix/objects/<model("iti_netflix.iti_netflix"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('iti_netflix.object', {
#             'object': obj
#         })
