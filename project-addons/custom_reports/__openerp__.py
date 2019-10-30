# -*- coding: utf-8 -*-
# © 2018 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Custom reports',
    'version': '1.0',
    'author': 'Pharmadus I.T.',
    'summary' : 'Odoo reports customized',
    'description': 'Odoo reports customized',
    'category': 'Reports',
    'website': 'www.pharmadus.com',
    'depends' : [
        'account',
        'account_payment',
        'sale',
        'purchase',
        'report_webkit',
        'l10n_es_partner_mercantil',
        'sale_transfer',
        'sale_transfer_sample_rel',
        'sale_channel',
        'sale_promotions',
        'commercial_and_financial_discount',
        'stock_reception',
        'invoice_link_sale',
        'product_spec',
        'custom_permissions',
        'custom_views',
    ],
    'data' : [
        'views/report_stockinventory.xml',
        'views/report_purchaseorder.xml',
        'views/report_purchasequotation.xml',
        'views/report_saleorder.xml',
        'views/report_invoice.xml',
        'views/report_invoice_pharmadus.xml',
        'views/report_invoice_pharmadus_be.xml',
        'views/report_invoice_biosalud.xml',
        'views/report_lot_labels.xml',
        'views/report_lot_labels_biosalud.xml',
        'views/report_lot_sample_labels.xml',
        'views/report_shipping_address.xml',
        'views/report_footer.xml',
        'views/report_footer_message.xml',
        'views/report_product_category_message_view.xml',
        'views/report_lot_sampled_package_label.xml',
        'views/account_view.xml',
        'views/account_invoice_report_view.xml',
        'views/account_payment_view.xml',
        'views/sale_report_view.xml',
        'views/stock_view.xml',
        'views/res_company_view.xml',
        'views/product_view.xml',
        'data/report_paperformat.xml',
        'data/remove_old_translations.xml',
        'data/ir_rule.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True
}
