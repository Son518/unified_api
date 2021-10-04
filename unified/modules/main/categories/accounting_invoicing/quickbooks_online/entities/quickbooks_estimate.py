from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util


@dataclass
class QuickbooksonlineEstimate:
    customer_id: str = None
    number: str = None
    line_amount: str = None
    line_decription: str = None
    line_item: str = None
    line_item_quantity: str = None
    line_item_tax_code: str = None
    expiration_date: str = None
    message_displayed_on_estimate: str = None

    def __post_init__(self):
        if not(self.expiration_date is None or "-" in self.expiration_date):
            format = '%Y-%m-%d'
            self.expiration_date = util.epoch_to_format(
                format, self.expiration_date)
