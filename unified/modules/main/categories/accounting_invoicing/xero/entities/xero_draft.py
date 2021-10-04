from dataclasses import dataclass
from accounting_invoicing.entities.draft import Draft
from accounting_invoicing.xero import util


@dataclass
class XeroDraft(Draft):

    organization_id: str = None
    expiry: str = None
    quote_number: str = None
    reference: str = None
    theme: str = None
    amounts_are: str = None
    item_code: str = None
    quantity: str = None
    unit_price: str = None
    discount: str = None
    account: str = None
    tax_rate: str = None
    terms: str = None    
    date: str = None

    def __post_init__(self):
        self.date_epoch()
        self.expiry_epoch()

    def date_epoch(self):
        if self.date is None or "-" in self.date:
            self.date = self.date
        else:
            format = "%Y-%m-%d"
            self.date = util.epoch_to_format(
                format, self.date)

    def expiry_epoch(self):
        if self.expiry is None or "-" in self.expiry:
            self.expiry = self.expiry
        else:
            format = "%Y-%m-%d"
            self.expiry = util.epoch_to_format(
                format, self.expiry)                