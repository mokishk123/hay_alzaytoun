from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    unit = fields.Float(
        string='Unit',
        compute='_compute_unit',
        store=True,
    )

    unit_products = fields.Char(
        string='Unit Products',
        compute='_compute_unit_products',
        store=False,
    )

    @api.depends('order_line.price_unit')
    def _compute_unit(self):
        for order in self:
            order.unit = sum(line.price_unit for line in order.order_line)


    @api.depends('order_line.product_id')
    def _compute_unit_products(self):
        for order in self:
            products = order.order_line.mapped('product_id.name')
            order.unit_products = ', '.join(products) if products else ''
