# -*- coding: utf-8 -*-
{
    'name': "new",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/return_views.xml',
        'views/rasidat_views.xml',
        'views/costumer_rasidat_views.xml',
        'views/take_views.xml',
        'views/costumer_info_views.xml',
        'views/product_views.xml',
        'views/purchase_views.xml',
        'views/vender_views.xml',
        'wizard/atlas_genral_report_wizard.xml',
        'reports/report.xml',
        'reports/atlas_genral_report.xml',
        'reports/sale_monthly_report.xml',
        'reports/purchase_monthly_report.xml',
        'reports/costumer_monthly_report.xml',
        'reports/costumer_rasidat_monthly_report.xml',
        'reports/return_monthly_report.xml',
        'reports/product_monthly_report.xml',
        'reports/vender_monthly_report.xml',
        'reports/takes_monthly_report.xml',
        'reports/rasidat_monthly_report.xml',
        
    ],
    'report.xmlid': [
        'new.atlas_genral_report',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
