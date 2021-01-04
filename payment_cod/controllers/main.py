# -*- coding: utf-8 -*-
import logging
import pprint
import werkzeug

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)


class CodController(http.Controller):
    _accept_url = '/payment/cod/feedback'

    @http.route([
        '/payment/cod/feedback',
    ], type='http', auth='public', csrf=False)
    def cod_form_feedback(self, **post):
        _logger.info('Beginning form_feedback with post data %s', pprint.pformat(post))  # debug
        request.env['payment.transaction'].sudo().form_feedback(post, 'cod')
        return werkzeug.utils.redirect('/shop/confirmation')
