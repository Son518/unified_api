from dataclasses import dataclass, field

@dataclass
class StripePaymentIntent:
    id: str = None
    amount: float = None
    currency: str = None
    customer_id: str = None
    description: str = None
    payment_method: str = None
    ## ?? payment_method_types: list
    
