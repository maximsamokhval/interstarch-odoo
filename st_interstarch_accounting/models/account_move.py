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
        for move in self:
            if not move.invoice_date:
                if move.move_type != 'in_invoice':
                    if not move.date:
                        move.date = fields.Date.context_today(self)
                continue
            accounting_date = move.invoice_date
            if not move.is_sale_document(include_receipts=True):
                accounting_date = move._get_accounting_date(move.invoice_date, move._affect_tax_report())
            if accounting_date and accounting_date != move.date:
                if move.move_type == 'in_invoice' and move.invoice_date:
                    bill_date = fields.Date.from_string(move.invoice_date)
                    today = fields.Date.today()
                    # If the `invoice_date` is in previous months
                    if bill_date < today.replace(day=1):  # date less than the first day of the current month
                        # The last day of the month
                        last_day_of_month = calendar.monthrange(bill_date.year, bill_date.month)[1]
                        move.date = bill_date.replace(day=last_day_of_month)
                    # If the Bill Date is in the past days of the current month
                    elif bill_date.month == today.month and bill_date < today:
                        move.date = today
                    # If the `invoice_date` is in the future
                    elif bill_date > today:
                        move.date = bill_date
                else:
                    move.date = accounting_date
                # _affect_tax_report may trigger premature recompute of line_ids.date
                self.env.add_to_compute(move.line_ids._fields['date'], move.line_ids)
                # might be protected because `_get_accounting_date` requires the `name`
                self.env.add_to_compute(self._fields['name'], move)
