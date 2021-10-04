from dataclasses import dataclass, field

@dataclass
class StripeCharge:
    id: str = None
    amount: int = 0
    balance_transaction_id: str = None
    billing: dict = field(default_factory=dict)
    currency: str = None
    customer_id: str = None
    description: str = None
    invoice_id: str = None
    payment_intent_id: str = None
    # payment_method_details: dict = field(default_factory=dict)
    # shipping: dict = field(default_factory=dict)  # Shipping Address
    status: str = None
