# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'lelien_custom_partner',
    'version': '16.0.1.0.0',
    'author': 'Elabore',
    'description': "Le Lien 42 : various customizations for partner",
    'depends': ['base','lcc_members'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    "auto_install": False,
    "application": False,
}
