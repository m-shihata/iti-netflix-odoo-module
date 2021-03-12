from odoo import models, fields, api

class NetflixSaleOrder(models.Model):
    _name = 'netflix.sale.order'
    _inherit = 'sale.order'

    # Inheritance debuging
    # https://github.com/odoo/odoo/blob/14.0/addons/sale/models/sale.py
    # and replaced the explicit names of rel tables 
    transaction_ids = fields.Many2many('payment.transaction', 'netflix_sales_transactions_rel')
    tag_ids = fields.Many2many('crm.tag', 'netflix_sales_tags_rel')
