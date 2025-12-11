# -*- coding: utf-8 -*-
{
    'name': 'PC Management',
    'version': '1.0',
    'author': 'Harold',
    'category': 'Custom',
    'summary': 'Gestión de ordenadores y componentes de PC',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pc_component_views.xml',
        'views/pc_computer_views.xml',
        'views/pc_menu.xml',
    ],
    'installable': True,
    'application': True,
}
