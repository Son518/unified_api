from dataclasses import dataclass


@dataclass
class CreditNote():

    contact_id: str = None
    type: str = None
    credit_note_id: str = None
    due_date: str = None
    credit_note_number: str = None
    currency: str = None
    tax_type: str = None
    description: str = None
    account: str = None
    tax_rate: str = None