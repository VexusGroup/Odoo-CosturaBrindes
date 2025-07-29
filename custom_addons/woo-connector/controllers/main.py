from odoo import http
from odoo.http import request

class WooController(http.Controller):

    @http.route('/woo/order', type='json', auth='public', methods=['POST'], csrf=False)
    def receive_order(self, **kwargs):
        data = request.jsonrequest
        # Apenas loga por enquanto
        request.env['ir.logging'].sudo().create({
            'name': 'Woo Order',
            'type': 'server',
            'dbname': request.env.cr.dbname,
            'level': 'INFO',
            'message': str(data),
            'path': 'woo_connector',
            'func': 'receive_order',
            'line': '15',
        })
        return {'status': 'received'}
