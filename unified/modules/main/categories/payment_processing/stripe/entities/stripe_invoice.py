from dataclasses import dataclass, field

from payment_processing.entities.invoice import Invoice

@dataclass
class StripeInvoice(Invoice):
    auto_advance: bool = None
    description: str = None
    subscription_id: str = None
    payment_method: str = None  ## is this reference, string, or id?
    
    # discounts: list = field(default_factory=list)
    total: float = None
    # metadata: dict = field(default_factory=dict)
    ## *** Aren't other customer fields required? *** https://stripe.com/docs/api/invoices/object    
