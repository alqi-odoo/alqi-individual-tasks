{
    'name': 'Luxer Sale Subscription',
    'summary': 'Sale subscription with Luxer site address',
    'description': """Luxer Sale Subscription
====================
This module adds a Luxer site address to the sale subscription module. If a site address is included in a sale order, then it will be included in the invoice as well.""",
    'version': '1.0',
    'license': 'OPL-1',
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'category': 'Custom Development',
    'depends': [
        'base',
        'sale_subscription',
    ],
    'data': [
        'views/account_move_views_inherit.xml',
        'views/sale_order_views_inherit.xml',
    ],
}
