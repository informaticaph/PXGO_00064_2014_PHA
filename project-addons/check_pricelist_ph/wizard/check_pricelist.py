# -*- coding: utf-8 -*-
# © 2017 Pharmadus I.T.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import models, fields, api, _


class CheckPricelistMessage(models.TransientModel):
    _name = 'check.pricelist.message'

    sale_id = fields.Many2one(comodel_name='sale.order')
    title = fields.Char(compute='_get_title')


class CheckPricelistWarnings(models.TransientModel):
    _name = 'check.pricelist.warnings'

    message_id = fields.Many2one(comodel_name='check.pricelist.message')
    number = fields.Integer(string='Nº', readonly=True)
    description = fields.Char('Description', readonly=True)
    type = fields.Selection(selection=[
        ('com_discount', 'Different commercial discounts'),
        ('fin_discount', 'Different financial discounts'),
        ('not_in_pl', 'Product not in price list'),
        ('price', 'Different price from price list'),
        ('vat', 'Different VAT')])
    order_line_id = fields.Many2one(comodel_name='sale.order.line')
    fix = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        message = self.env['check.pricelist.message'].browse(vals['message_id'])
        vals['number'] = len(message.warning_ids) + 1
        return super(CheckPricelistWarnings, self).create(vals)


class CheckPricelistMessage(models.TransientModel):
    _inherit = 'check.pricelist.message'

    warning_ids = fields.One2many(comodel_name='check.pricelist.warnings',
                                  inverse_name='message_id')

    @api.one
    def _get_title(self):
        self.title = _('There are %d warnings detected') % \
                     (len(self.warning_ids))

    @api.multi
    def fix_warnings(self):
        for warning in self.warning_ids.filtered('fix'):
            if warning.type == 'com_discount':
                s = self.sale_id
                s.commercial_discount_percentage = \
                    s.partner_id.commercial_discount
                s.commercial_discount_input = \
                    s.partner_id.commercial_discount
                s.generate_discounts
                continue

            elif warning.type == 'fin_discount':
                s = self.sale_id
                s.financial_discount_percentage = \
                    s.partner_id.financial_discount
                s.financial_discount_input = \
                    s.partner_id.financial_discount
                s.generate_discounts
                continue

            elif warning.type == 'not_in_pl':
                # For now, nothing to do...
                continue

            elif warning.type == 'price':
                ol = warning.order_line_id
                pricelist = ol.order_id.pricelist_id.version_id.\
                    filtered('active')
                pl_price = pricelist.items_id.filtered(
                    lambda r: r.product_id == ol.product_id)
                ol.price_unit = pl_price.price_surcharge
                continue

            elif warning.type == 'vat':
                ol = warning.order_line_id
                ol.tax_id = ol.product_id.taxes_id
                continue

        self.sale_id.update_with_discounts()
        return self.sale_id.check_pricelist()