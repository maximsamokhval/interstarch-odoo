import calendar

from odoo import models, fields



class AccountMove(models.Model):
    _inherit = "account.move"

    def _compute_date(self):
        """
        Compute the `date` field of the move.
        Depends on `invoice_date`
        """
        super()._compute_date()
        for move in self:
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


