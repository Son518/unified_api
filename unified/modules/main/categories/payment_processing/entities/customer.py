from dataclasses import dataclass

@dataclass
class Customer:
    id: str = None
    name: str = None
    family_name: str = None
    email: str = None
    phone: str = None
    address_line1: str = None
    address_line2: str = None
    locality: str = None
    city: str = None  # Administrative District	(Square)
    postal_code: str = None
    state: str = None
    country: str = None
    country_code: str = None
