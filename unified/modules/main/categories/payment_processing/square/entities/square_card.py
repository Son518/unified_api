from dataclasses import dataclass

@dataclass
class SquareCard:
    id: str = None
    customer_id: str = None
    cardholder_name: str = None
    address_line1: str = None
    address_line2: str = None
    locality: str = None
    city: str = None
    postal_code: str = None
    country_code: str = None
    
    reference_id: str = None
    source_id: str = None
    idempotency_key: str = None
