from odoo import models, fields, api
from datetime import datetime, timedelta

class NetflixMovies(models.Model):
    _name = 'netflix.movies'
    _description = 'Class Movies'

    name = fields.Char()
    production_year = fields.Date()
    company = fields.Char()
    subscription_price = fields.Float()

    url = fields.Char()
    image = fields.Binary()
    category_id = fields.Many2one('netflix.movies.categories')
    country_id = fields.Many2one('res.country')
    producer_id = fields.Many2one('res.partner')

    description = fields.Html()
    cast_ids = fields.Many2many('netflix.movies.cast')

    def _get_report_name(self):
        return f'{self.name} {self.production_year}'

    def _sync_movies(self):
        # we need to get data from some server
        # Let's assume this is what came back
        new_movies = [
            {'name': 'Avatar'},
            {'name': 'Lucy'}
        ]
        return [self.create(movie) for movie in new_movies]

    # def _sync_next_call(self):
    #     now =
    #     next_call = None
    #
    #
    #         next_call = datetime.now().strftime('%Y-%m-%d 07:00:00') if now.hour < 7 else (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d 07:00:00')
    #
    #     return next_call.
