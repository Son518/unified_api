from dataclasses import dataclass


@dataclass
class Invoice():

    invoice_id: str = None
    description: str = None
    name: str = None
    email: str = None
    status: str = None
    currency: str = None
    number: str = None