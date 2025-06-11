# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'lelien_custom_sync',
    'version': '16.0.1.0.0',
    'author': 'Elabore',
    'description': "Le Lien 42 : cron public and private data syncronization",
    'depends': ['base','partner_profiles'],
    'data': [
        'data/data_sync_cron.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    "auto_install": False,
    "application": False,
}
