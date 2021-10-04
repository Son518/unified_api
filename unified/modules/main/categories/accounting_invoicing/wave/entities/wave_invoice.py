from dataclasses import dataclass, field
from datetime import datetime, timezone
from accounting_invoicing.entities.invoice import Invoice
from accounting_invoicing.wave import util


@dataclass
class WaveInvoice(Invoice):

    business_id: str = None
    customer_id: str = None
    item_price: str = None
    item_product: str = None
    item_quantity: str = None
    item_tax: str = None
    item_description: str = None
    invoice_currency: str = None
    invoice_number: str = None
    invoice_date: str = None
    invoice_title: str = None
    subhead: str = None
    footer: str = None
    additional_notes: str = None
    so_or_po_number: str = None
    end_date: str = None
    exchange_rate: str = None
    disable_credit_card_payments: str = None
    ammount_title: str = None
    item_title: str = None
    price_title: str = None
    quantity_title: str = None
    hide_amount: str = None
    hide_description: str = None
    hide_item: str = None
    hide_price: str = None
    hide_quantity: str = None
    business_id: str = None
    business_id: str = None

    def __post_init__(self):

        self.end_date = self.date_to_epoch(self.end_date)
        self.invoice_date = self.date_to_epoch(self.invoice_date)

    def date_to_epoch(self, date):
        if not(date is None or "-" in date):
            format = "%Y-%m-%d"
            date = util.epoch_to_format(format, date)
            return date
