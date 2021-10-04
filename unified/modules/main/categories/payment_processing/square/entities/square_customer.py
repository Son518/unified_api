
from dataclasses import dataclass
from payment_processing.entities.customer import Customer

@dataclass
class SquareCustomer:
    id: str = None
    first_name: str = None
    last_name: str = None
    nickname: str = None
    email: str = None
    phone: str = None
    address_line1: str = None
    address_line2: str = None
    locality: str = None
    city: str = None
    state: str = None
    postal_code: str = None
    country_code: str = None
    description: str = None
    company: str = None
    reference_id: str = None
