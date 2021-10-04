from dataclasses import dataclass
from accounting_invoicing.zoho_books import util

@dataclass
class ZohobooksEstimate():
    organization_id: str = None,
    customer_id: str = None,
    estimate_number: str = None,
    start_date: str = None,
    end_date: str = None,
    item_id: str = None,
    rate: str = None,
    quantity: str = None,
    discount: str = None,
    description: str = None,
    exchange_rate: str = None,
    estimate_notes: str = None,
    estimate_terms: str = None,
    shipping_charge: str = None

    def __post_init__(self):
        self.start_date = self.convert_epoch(self.start_date)
        self.end_date = self.convert_epoch(self.end_date)
      
    def convert_epoch(self,date):
        if not(date is None or "-" or '' in date):
            format = "%Y-%m-%d"
            date = util.epoch_to_format(format, date).replace("-", "")
            return date
    