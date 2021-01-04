# -*- coding: utf-8 -*-

{
    'name': 'Payment Cash On Delivery acquirer',
    'category': 'Accounting/Payment Acquirers',
    'sequence': 60,
    'summary': 'Payment Acquirer: Cash On Delivery Implementation',
    'version': '1.0',
    'description': """Payment Cash On Delivery""",
    'depends': ['payment'],
    'data': [
        'views/payment_views.xml',
        'views/payment_cod_templates.xml',
        'data/payment_acquirer_data.xml',
        "templates/website_sale.xml"
    ],
    'installable': True,
    'application': True,
    'post_init_hook': 'create_missing_journal_for_acquirers',
    'uninstall_hook': 'uninstall_hook',
}
