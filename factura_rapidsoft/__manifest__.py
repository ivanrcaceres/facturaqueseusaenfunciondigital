# -*- coding: utf-8 -*-
{
    'name': "factura_rapidsoft",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    # 'depends': ['base'],
    # 'base','account','paraguay_backoffice'
    'depends': ['base','account','paraguay_backoffice'],

    # always loaded
    'data': [
        # los xml para la factura de rapidsoft
        'reports/factura_rapidsoft_reports.xml',
        'reports/factura_report.xml',
        'reports/factura_report2.xml',
        'reports/factura_report_dolares.xml',
        'reports/facturausdgs.xml',


        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}