from dataclasses import dataclass
from accounting_invoicing.entities.purchase_order import PurchaseOrder
from accounting_invoicing.xero import util

@dataclass
class XeroPurchaseOrder(PurchaseOrder):

    organization_id: str = None
    theme: str = None
    tax_type: str = None
    item_code: str = None
    quantity: str = None
    unit_price: str = None
    tax_rate: str = None
    attachments: str = None
    purchase_order_status: str = None
    date: str = None
    delivery_date: str = None

    def __post_init__(self):
        self.date_epoch()
        self.delivery_date_epoch()

    def date_epoch(self):
        if self.date is None or "-" in self.date:
            self.date = self.date
        else:
            format = "%Y-%m-%d"
            self.date = util.epoch_to_format(
                format, self.date)

    def delivery_date_epoch(self):
        if self.delivery_date is None or "-" in self.delivery_date:
            self.delivery_date = self.delivery_date
        else:
            format = "%Y-%m-%d"
            self.delivery_date = util.epoch_to_format(
                format, self.delivery_date)