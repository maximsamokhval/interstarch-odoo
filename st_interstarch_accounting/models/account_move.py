import calendar

from odoo import models, fields, api



class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends('invoice_date', 'company_id')
    def _compute_date(self):
        """
        Compute the `date` field of the move.
        Depends on `invoice_date`
        """
        super()._compute_date()
        for move in self:
            if move.move_type == 'in_invoice':
                move.date = move.invoice_date
