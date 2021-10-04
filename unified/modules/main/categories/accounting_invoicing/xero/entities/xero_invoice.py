from dataclasses import dataclass
from accounting_invoicing.entities.invoice import Invoice
from accounting_invoicing.xero import util

@dataclass
class XeroInvoice(Invoice):

    organization_id: str = None
    item_code: str = None
    quantity: str = None
    unit_price: str = None
    discount: str = None
    account: str = None
    tax_rate: str = None
    attachment_url: str = None
    branding_theme: str = None
    reference: str = None
    send_to_contact: str = None
    line_items_type: str = None
    creation_date: str = None
    due_date: str = None

    def __post_init__(self):
        self.creation_date_epoch()
        self.due_date_epoch()

    def due_date_epoch(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(
                format, self.due_date)

    def creation_date_epoch(self):
        if self.creation_date is None or "-" in self.creation_date:
            self.creation_date = self.creation_date
        else:
            format = "%Y-%m-%d"
            self.creation_date = util.epoch_to_format(
                format, self.creation_date)