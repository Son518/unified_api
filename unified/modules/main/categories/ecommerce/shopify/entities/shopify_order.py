from dataclasses import dataclass


@dataclass
class ShopifyOrder:
    order_id:str=None
    product_variant_id: str = None
    product_quantity: str = None
    note: str = None
    customer_id: str = None
    tags: str = None
    send_receipt: bool = False
    send_fulfillment_receipt: str = None
    fulfillment_status: str = None
    shipping_address_first_name: str = None
    shipping_address_last_name: str = None
    shipping_address_company: str = None
    shipping_address_phone: str = None
    shipping_address_address: str = None
    shipping_address_city: str = None
    shipping_address_country: str = None
    shipping_address_state: str = None
    shipping_address_postal: str = None
    billing_address_first_name: str = None
    billing_address_last_name: str = None
    billing_address_company: str = None
    billing_address_phone: str = None
    billing_address_address: str = None
    billing_address_city: str = None
    billing_address_country: str = None
    billing_address_state: str = None
    billing_address_postal: str = None
    email:str=None
    taxes_included:str=None
    currency:str=None
    name:str=None
    total_price:str=None
