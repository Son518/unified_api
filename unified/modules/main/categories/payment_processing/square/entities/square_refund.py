from dataclasses import dataclass

@dataclass
class SquareRefund:
    id: str = None
    status: str = None
    amount: str = None
    currency_code: str = None
    payment_id: str = None
    location_id: str = None
    reason: str = None
    
    idempotency_key: str = None
