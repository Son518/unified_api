from dataclasses import dataclass, field

from payment_processing.entities.customer import Customer

@dataclass
class StripeCustomer(Customer):
    description: str = None
    payment_method: str = None
    # metadata: dict = field(default_factory=dict)