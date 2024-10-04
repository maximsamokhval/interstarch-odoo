# -*- coding: utf-8 -*-

{
    'name': 'ST Interstarch Stock',
    'version': '17.0.0.0.0',
    'summary': 'Stock customisation for Interstarch',
    'sequence': 10,
    'description': """

""",
    'category': 'Inventory/Inventory',
    'website': 'https://smarttek.solutions/',
    'depends': [
        'stock',
    ],
    'data': [
    ],
    'assets': {
        'web.assets_backend': [
            'st_interstarch_stock/static/src/js/list_renderer.js'
        ]
    },

    'demo': [],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}
