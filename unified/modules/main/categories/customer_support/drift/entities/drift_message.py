from dataclasses import dataclass
from customer_support.drift import util

@dataclass
class DriftMessage():
    
    orgId: str = None
    type: str = None
    data_id: str = None
    conversationId: str = None
    body: str = None
    author_id: str = None
    author_type: str = None
    author_bot: bool = False
    data_type: str = None
    createdAt: str = None
    context_ip: str = None
    location_city: str = None
    region: bool = True
    country: str = None
    countryName: str = None
    postalCode: str = None
    latitude: str = None
    longitude: str = None
    attributes: str = None
    token: str = None