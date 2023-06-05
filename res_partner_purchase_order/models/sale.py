from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    oc_number = fields.Char(string='Número OC')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id.purchase_order:
            self.oc_number = False
        else:
            self.oc_number = ''

    def action_confirm(self):
        if self.partner_id.purchase_order and not self.oc_number:
            raise ValidationError(
                "A cotação não pode ser confirmada. O campo 'Número OC' deve ser preenchido.")
        return super(SaleOrder, self.with_context(bypass_check=True)).action_confirm()

    def action_done(self):
        if self.partner_id.purchase_order and not self.oc_number:
            raise ValidationError(
                "A cotação não pode ser confirmada. O campo 'Número OC' deve ser preenchido.")
        return super(SaleOrder, self.with_context(bypass_check=True)).action_done()