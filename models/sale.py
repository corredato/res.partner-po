from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id.purchase_order:
            self.client_order_ref = False
        else:
            self.client_order_ref = ''

    def action_unlock(self):
        if self.partner_id.purchase_order and not self.client_order_ref:
            raise ValidationError(
                "A cotação não pode ser confirmada. O campo 'Referência do Cliente' deve ser preenchido.")
        return super(SaleOrder, self.with_context(bypass_check=True)).action_unlock()

    def action_done(self):
        if self.partner_id.purchase_order and not self.client_order_ref:
            raise ValidationError(
                "A cotação não pode ser confirmada. O campo 'Referência do Cliente' deve ser preenchido.")
        return super(SaleOrder, self.with_context(bypass_check=True)).action_done()