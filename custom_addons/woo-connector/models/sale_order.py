from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    woo_order_number = fields.Char(string="WooCommerce Order Number")
    woo_sent = fields.Boolean(string="Enviado do WooCommerce", default=False)
