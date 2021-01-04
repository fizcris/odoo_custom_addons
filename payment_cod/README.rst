========================
payment_cod
========================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2|

Cash on delivery addon
**********************

Tested with Odoo 14.0
#####################

This is a quite crude approach where most of the *action* happens on the front end under shop/payment

Usage
######
* Create new "Cash On Delivery" type acquirer
    * The only important thing is the name and type
    * The Fees inputed here  are only shown in case of forntend failure
* Create delivery method with the fees you want to apply
    * Delivery method must have the same name as the acquirer created before.


* Enjoy  :)

known limitations
#####################

- Carrier name and Acquirer name MUST be the same
- Just one Cash On Delivery acquirer is allowed (not implemented more than one)
- Provider fees ignored

Contributors
#####################

* Cristian Alonso  <fizcris@gmail.com>