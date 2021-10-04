from dataclasses import dataclass
from accounting_invoicing.entities.credit_note import CreditNote
from accounting_invoicing.xero import util

@dataclass
class XeroCreditNote(CreditNote):

    organization_id: str = None
    attachment: str = None
    item_code: str = None
    unit_price: str = None
    quantity: str = None
    credit_note_status: str = None    
    due_date: str = None
    discount: str = None

    def __post_init__(self):
        self.due_date_epoch()

    def due_date_epoch(self):
        if self.due_date is None or "-" in self.due_date:
            self.due_date = self.due_date
        else:
            format = "%Y-%m-%d"
            self.due_date = util.epoch_to_format(
                format, self.due_date)
