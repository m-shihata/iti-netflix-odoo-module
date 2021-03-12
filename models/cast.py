# -*- coding: utf-8 -*-

from odoo import models, fields, api

class NetflixMoviesCast(models.Model):
    _name = 'netflix.movies.cast'
    _description = 'Netflix Movies Cast'

    name = fields.Char()
    age = fields.Date()
    address = fields.Char()
