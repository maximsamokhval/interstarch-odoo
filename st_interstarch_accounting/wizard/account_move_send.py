from odoo import api, models


class AccountMoveSend(models.TransientModel):
    _inherit = 'account.move.send'

    @api.model
    def _process_send_and_print(self, moves, wizard=None, allow_fallback_pdf=False, **kwargs):
        for invoice in moves:
            if invoice.invoice_pdf_report_id and invoice.move_type == 'out_invoice':
                invoice.invoice_pdf_report_id.unlink()
        return super()._process_send_and_print(moves, wizard, allow_fallback_pdf, **kwargs)
