{
    'name': 'Saphire Financial Reports - Webkit',
    'version': '9.0',
    'author': (
        "Suhendar,"
        "Odoo Community Association (OCA)"
    ),
    'license': 'AGPL-3',
    'category': 'Finance',
    'website': 'http://www.vileo.co.id',
    'images': [
        #'images/ledger.png',
    ],
    'depends': [
        'account',
        'report_webkit'
    ],
    'demo': [],
    'data': [
        #'views/account_view.xml',
        #'data/financial_webkit_header.xml',
        #'report/report.xml',
        #'wizard/wizard.xml',
        #'wizard/balance_common_view.xml',
        #'views/wizard/general_ledger_wizard_view.xml',
        #'wizard/partners_ledger_wizard_view.xml',
        #'wizard/trial_balance_wizard_view.xml',
        #'wizard/partner_balance_wizard_view.xml',
        #'wizard/open_invoices_wizard_view.xml',
        #'wizard/aged_open_invoices_wizard.xml',
        #'wizard/aged_partner_balance_wizard.xml',
        #'wizard/print_journal_view.xml',
        #'views/report_menus.xml',

    ],
    # tests order matter
    'test': [
        #'test/general_ledger.yml',
             #'test/partner_ledger.yml',
             #'test/trial_balance.yml',
             #'test/partner_balance.yml',
             #'test/open_invoices.yml',
             #'test/aged_trial_balance.yml'
     ],
    # 'tests/account_move_line.yml'
    'active': False,
    'installable': True,
    'application': True,
}