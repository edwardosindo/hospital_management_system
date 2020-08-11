# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Hospital Management',
    'version' : '1.1',
    'summary': 'Module for managing the Hospital',
    'sequence': 15,
    'license': 'AGPL-3',
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/page/billing',
    'images' : ['images/accounts.jpeg','images/bank_statement.jpeg','images/cash_register.jpeg','images/chart_of_accounts.jpeg','images/customer_invoice.jpeg','images/journal_entries.jpeg'],
    'depends' : [
        'mail',
        'sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/data.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'reports/report.xml',
        'reports/patient_card.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

