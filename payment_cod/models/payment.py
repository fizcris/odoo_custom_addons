# -*- coding: utf-8 -*-
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import models, fields, api
from odoo.addons.payment.models.payment_acquirer import ValidationError
from odoo.tools.float_utils import float_compare
import odoo.addons.decimal_precision as dp

import logging
import pprint

_logger = logging.getLogger(__name__)

class AcquirerCod(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[
        ('cod', 'Cash On Delivery')], ondelete={
        'cod': 'set default'})

    fees_implemented = fields.Boolean('Fees Computation Supported', compute='_compute_feature_support')
    fees_active = fields.Boolean('Add Extra Fees', default=True)
    # Default COD fees values - uses existing paypal columns
    fees_dom_fixed = fields.Float('Fixed domestic fees', default=2.45)
    fees_dom_var = fields.Float('Variable domestic fees (in percents)', default=0.0)
    fees_int_fixed = fields.Float('Fixed international fees', default=0.0)
    fees_int_var = fields.Float('Variable international fees (in percents)', default=0.0)

    def _get_feature_support(self):
        """Get advanced feature support by provider.

        Each provider should add its technical in the corresponding
        key for the following features:
            * fees: support payment fees computations
            * authorize: support authorizing payment (separates
                         authorization and capture)
            * tokenize: support saving payment data in a payment.tokenize
                        object
        """
        res = super(AcquirerCod, self)._get_feature_support()
        res['fees'].append('cod')
        return res

    # @api.onchange("charge_fee_product_id")
    # def onchange_charge_fee_product_id(self):
    #     if self.charge_fee_product_id:
    #         self.charge_fee_description = self.charge_fee_product_id.name

    def cod_compute_fees(self, amount, currency_id, country_id):
        """ Compute cash on delivery fees.

            :param float amount: the amount to pay
            :param integer country_id: an ID of a res.country, or None. This is
                                       the customer's country, to be compared to
                                       the acquirer company country.
            :return float fees: computed fees
        """
        if not self.fees_active:
            return 0.0
        country = self.env['res.country'].browse(country_id)
        if country and self.company_id.country_id.id == country.id:
            percentage = self.fees_dom_var
            fixed = self.fees_dom_fixed
        else:
            percentage = self.fees_int_var
            fixed = self.fees_int_fixed
        fees = (percentage / 100.0 * amount + fixed) / (1 - percentage / 100.0)
        return fees


    def cod_get_form_action_url(self):
        return '/payment/cod/feedback'


class CodFeePaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    @api.model
    def _cod_form_get_tx_from_data(self, data):
        reference, amount, currency_name = data.get('reference'), data.get('amount'), data.get('currency_name')
        tx = self.search([('reference', '=', reference)])

        if not tx or len(tx) > 1:
            error_msg = _('received data for reference %s') % (pprint.pformat(reference))
            if not tx:
                error_msg += _('; no order found')
            else:
                error_msg += _('; multiple order found')
            _logger.info(error_msg)
            raise ValidationError(error_msg)

        return tx

    def _cod_form_get_invalid_parameters(self, data):
        invalid_parameters = []

        if float_compare(float(data.get('amount') or '0.0'), self.amount, 2) != 0:
            invalid_parameters.append(('amount', data.get('amount'), '%.2f' % self.amount))
        if data.get('currency') != self.currency_id.name:
            invalid_parameters.append(('currency', data.get('currency'), self.currency_id.name))

        return invalid_parameters

    def _cod_form_validate(self, data):
        _logger.info('Validated cod payment for tx %s: set as pending' % (self.reference))
        self._set_transaction_pending()
        return True