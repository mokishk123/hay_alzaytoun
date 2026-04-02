{
    'name': 'Hay Alzaytoun',
    'version': '19.0.1.0',
    'author': 'Mohamed Kishk',
    'depends': [
        'base',
        'sale_project',
        'sale_renting',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/rental_order_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
