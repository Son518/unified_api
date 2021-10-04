from dataclasses import dataclass


@dataclass
class ShopifyInventory:
    location_id: str = None
    product_variant_id: str = None
    set_quantity_to: str = None
