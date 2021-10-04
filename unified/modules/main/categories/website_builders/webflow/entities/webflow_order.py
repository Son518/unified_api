from dataclasses import dataclass

@dataclass
class WebflowOrder():
    
    site_id: str = None
    order_id: str = None
    reason: str = None
    comment: str = None
    shipping_provider: str = None
    shipping_tracking: str = None