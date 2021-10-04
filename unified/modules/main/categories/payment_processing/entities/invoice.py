from dataclasses import dataclass, field

@dataclass
class Invoice:
    id: str = None
    customer_id: str = None  
    email: str = None
    payment_method: str = None
    total: float = None
