{
    'name': 'Hai Alzaytoun',
    'version': '19.0.1.0',
    'author': 'Mohamed Kishk',
    'depends': [
        'base',
        'sale',
        'sale_project',
        'sale_renting',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/rental_sale_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
