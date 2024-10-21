{
    'name': 'Prudential Module',
    'version': '16.0.1.0.0',
    'category': 'Accounting',
    'summary': """ This modules is developed by prudential tech""",
    'description': """This modules enables approval feature in the payment. """,
    'author': ' Byasi Solomon',
    'company': 'Prudential Tech',
    'maintainer': 'Prudential Tech',
    'website': "",
    'depends': ['base', 'account', 'sale_management', 'purchase', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_payment_view.xml',
        'views/config_settings_view.xml',
        'views/purchase_view.xml',
        'views/purchase_config_settings_view.xml',
        'views/stock_picking_views.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
}