from dataclasses import dataclass, field

from payment_processing.entities.subscription import Subscription

@dataclass
class StripeSubscription(Subscription):
    cancel_at_period_end: bool = None
    # plan_id: str = None  # *** not found in api documentation for Subscription object *** https://stripe.com/docs/api/subscriptions/object
    collection_method: str = None  
    coupon: str = None
    metadata: dict = field(default_factory=dict)

    ##
    ## start_date and end_date SHOULD be there for a subscription 
    ##

    price_id: str = None
    currency: str = None
    product_id: str = None
    unit_price: float = None
    recurring_interval: str = None
    recurring_count: int = None