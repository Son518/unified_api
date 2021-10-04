from dataclasses import dataclass, field

@dataclass
class StripeWebhook:
    """
    https://stripe.com/docs/api/webhook_endpoints/object
    """
    id: str = None
    enabled_event: str = None # actually this is a list. We presume to take [0]
    description: str = None
    created: int = None # epoch
    secret: str = None
    status: str = None
    url: str = None
