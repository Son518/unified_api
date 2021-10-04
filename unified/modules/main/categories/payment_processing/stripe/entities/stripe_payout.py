from dataclasses import dataclass, field
import datetime

@dataclass
class StripePayout:
    id: str = None
    amount: float = None
    currency: str = None
    arrival_date: datetime.datetime = None
    description: str = None
    payment_method: str = None
    ## ?? payment_method_types: list
    
