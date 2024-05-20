{
    'name': 'Car Workshop',
    'version': '1.0',
    'summary': 'Car Workshop Management',
    'description': 'Car Workshop Management',
    'installable': True,
    'application': True,
    'author': 'Suit Software',
    'depends': ['base', 'contacts', 'product', 'fleet', 'stock'],
    'data': [
        'views/car_workshop_views.xml',
        'views/car_workshop_menu.xml',
        'security/ir.model.access.csv',
        'data/car_workshop_sequences.xml',
    ]
}
