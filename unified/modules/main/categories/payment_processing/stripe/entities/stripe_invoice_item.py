from dataclasses import dataclass, field
from datetime import datetime
@dataclass
class StripeInvoiceItem:
    """
    https://stripe.com/docs/api/invoiceitems/object
    """
    id: str = None
    customer_id: str = None
    amount: float = None
    currency: str = None
    description: str = None
    metadata: dict = field(default_factory=dict)
    period_start: datetime = None
    period_end: datetime = None
    price: int = None
    price_id: str = None
    proration: bool = None
    quantity: int = None
    price_type: str = None ## Type wasn't found, but price/type was for price type
