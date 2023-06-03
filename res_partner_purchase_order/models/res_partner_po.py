from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    purchase_order = fields.Boolean(string='Pedido de Compra')