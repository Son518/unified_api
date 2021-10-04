from dataclasses import dataclass
from accounting_invoicing.entities.payment import Payment
from accounting_invoicing.xero import util


@dataclass
class XeroPayment(Payment):

    organization_id: str = None
    document_type: str = None
    document_id: str = None
    paid_to: str = None
    currency_rate: str = None
    due_date: str = None

    def __post_init__(self):
        self.due_date_epoch()

    def due_date_epoch(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(
                format, self.due_date) 
    