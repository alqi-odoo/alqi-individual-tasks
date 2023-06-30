{
    'name': 'NY P&W Shoes Calculate Price',
    'summary': 'Automatically calculate the price of shoes',
    'description': """NY P&W Shoes Calculate Price
====================
This module automatically calculates the price of shoes for NY P&W Shoes based on pairs per case and price per pair.""",
    'version': '1.1',
    'license': 'OPL-1',
    'author': 'Odoo Inc.',
    'website': 'https://www.odoo.com/',
    'category': 'Custom Development',
    'depends': [
        'base',
        'stock',
    ],
    'data': [
        'views/product_template_views_inherit.xml',
    ],
}
