from dataclasses import dataclass


@dataclass
class PurchaseOrder():

    pusrchase_order_id: str = None
    contact_id: str = None
    order_number: str = None
    reference: str = None
    currency: str = None
    description: str = None
    discount: str = None
    account: str = None
    delivery_address: str = None
    telephone: str = None