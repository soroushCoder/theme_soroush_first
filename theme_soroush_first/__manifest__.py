# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Theme Soroush Version 2',
    'description': 'website theme to customization possibilities.',
    'category': 'Theme/Shoping',
    'sequence': 1000,
    'version': '2.0',
    'depends': ['website','product', 'sale','website_sale','theme_default'],
	'author':'Soroush Ebadi',
    'data': [
        'data/theme_default_data.xml',
        'views/theme_default_templates.xml',  
        'views/ecommerce_snippest_extra.xml',
        'views/website_ecommerce_template_views.xml',
        'views/template.xml'
    ],
    'images': [
         'static/description/cover.jpg',
		'static/description/icon.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
