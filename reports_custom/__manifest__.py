# -*- coding: utf-8 -*-

{
    'name': 'Custom reports',
    'category': 'Reporting',
    'sequence': 1,
    'summary': 'Module that generates custom reports for printing',
    'version': '1.0',
    'description': """Module that generates custom reports for printing""",
    'depends': ['sale'],
    'data': [
        'reports/reports.xml',
    ],
    'installable': True,
    'application': True,
}
