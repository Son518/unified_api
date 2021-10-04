from dataclasses import dataclass
from ecommerce.shipstation.util import epoch_to_format

@dataclass
class ShipstationOrder:
    
    shipstation_store:str = None
    order_status_id:str = None
    order_date:str = None
    buyer_name:str = None
    payment_date:str = None
    buyer_email:str = None
    recipient_name:str = None
    recipient_company:str = None
    address_line1:str = None
    address_line2:str = None
    address_line3:str = None
    recipient_city:str = None
    recipient_state:str = None
    pin_code:str = None
    country_code:str = None
    recipient_phone:str = None
    ammount_paid:str = None
    tax_paid:str = None
    shipping_paid:str = None
    customer_notes:str = None
    internal_note:str = None
    is_a_gift:str = None
    gift_message:str = None
    requested_shipping_method:str = None
    items_sku:str = None
    item_name:str = None
    image_url:str = None
    quantity:str = None
    unit_price:str = None
    
    def __post_init__(self):
        self.order_date = self.convert_epoch(self.order_date)
        self.payment_date = self.convert_epoch(self.payment_date)
    
    def convert_epoch(self,date):
        
        if not(date is None or "-" in date):
            date = epoch_to_format(date)
            return date