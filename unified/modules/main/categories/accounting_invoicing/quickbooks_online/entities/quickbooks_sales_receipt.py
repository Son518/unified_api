from dataclasses import dataclass
from accounting_invoicing.quickbooks_online import util


@dataclass
class QuickbooksonlieSalesReceipt:
    sale_receipt_id: str = None
    customer_id: str = None
    message: str = None
    service_date: str = None
    line_item_quantity: str = None
    line_item_unit_price: str = None
    line_item_tax_code: str = None
    transaction_date: str = None
    sales_receipt_number: str = None
    line_description: str = None
    product_id: str = None

    def __post_init__(self):
        if not(self.service_date is None or "-" in self.service_date):
            format = '%Y-%m-%d'
            self.service_date = util.epoch_to_format(
                format, self.service_date)
