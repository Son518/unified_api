from dataclasses import dataclass
from unified.core import util

@dataclass
class ShopifyProduct:
    product_variant_id: str = None
    product_id: str = None
    title: str = None
    product_type: str = None
    vendor: str = None
    product_description: str = None
    tags: str = None
    published_at: str = None
    price: str = None
    inventory_policy: str = None
    image_url: str = None
    sku: str = None
    is_published: str = None
    publish_to_point_of_sale: str = None
    compare_at_price: str = None

    def __post_init__(self):
        if not(self.published_at is None or "-" in self.published_at):
            format = '%Y-%m-%d'
            self.published_at = util.epoch_to_format(format, self.published_at)
