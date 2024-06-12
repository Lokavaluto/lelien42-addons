# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Le Lien 42 customization',
    'version': '12.0.1.0.0',
    'category': '',
    'description': "Le Lien 42 : custom fields and views",
    'depends': ['base','lcc_members'],
    'data': [
        'views/res_partner_views.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    "auto_install": False,
    "application": False,
}
