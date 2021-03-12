# -*- coding: utf-8 -*-
from odoo import models, fields, api

class NetflixMoviesCategories(models.Model):
    _name = 'netflix.movies.categories'
    _description = 'Class Categories'

    name = fields.Char(string="Category name")
    movies = fields.One2many('netflix.movies', 'category_id')
