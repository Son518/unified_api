from dataclasses import dataclass

@dataclass
class Subscription:
    id: str = None
    customer_id: str = None
    email: str = None
