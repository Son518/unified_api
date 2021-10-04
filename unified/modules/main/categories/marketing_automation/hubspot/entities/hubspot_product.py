from dataclasses import dataclass


@dataclass
class HubspotProduct:
    product_id: str = None
    product_name: str = None
    sku: str = None
    description: str = None
    image: str = None
    url: str = None
    folder_id: str = None
    unit_price: str = None
    unit_cost: str = None
    term: str = None
