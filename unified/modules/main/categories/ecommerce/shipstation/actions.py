import requests
import json
from unified.core.actions import Actions
from unified.core.util import convert_epoch
from ecommerce.shipstation.util import get_basic_token, rest
from ecommerce.shipstation.entities.shipstation_order import ShipstationOrder

class ShipstationActions(Actions):
    
    def create_order(self, context, order_payload):
        
        """ Create new order"""
        
        access_token = get_basic_token(context['headers'])
        url = "https://ssapi.shipstation.com/orders/createorder"
        order_details =  ShipstationOrder(**order_payload)
        
        # Status of the order
        order_status = {
            "1" : "awaiting_payment", 
            "2" : "awaiting_shipment", 
            "3" : "shipped",
            "4" : "cancelled",
            "5" : "on_hold"
        }
        
        order = {
        "orderNumber": order_details.shipstation_store,
        "orderDate": order_details.order_date,
        "items":[
            {
                "name" : order_details.item_name
            },
        ],
        "shipTo": {
        "name": order_details.recipient_name,
        "street1": order_details.address_line1,
        "city": order_details.recipient_city,
        "postalCode": order_details.pin_code,
        }
        }
        
        # Create billTo 
        order["billTo"] = dict()
        
        if order_details.order_status_id is not None:
            
            order["orderStatus"]= order_status.get(order_details.order_status_id)
        
        if order_details.address_line3 is not None:
            
            order["street3"] = order_details.address_line3
        
        if order_details.ammount_paid is not None:
            
            order["items"][0]["amountPaid"] = order_details.ammount_paid
        
        if order_details.unit_price is not None:
            
            order["items"][0]["unitPrice"] = order_details.unit_price
        
        if order_details.quantity is not None:
            
            order["quantity"] = order_details.quantity
        
        if order_details.shipping_paid is not None:
            
            order["shippingAmount"] = order_details.shipping_paid
        
        if order_details.tax_paid is not None:
            
            order["taxAmount"] = order_details.tax_paid
        
        if order_details.is_a_gift is not None:
            
            order["gift"] = order_details.is_a_gift
        
        if order_details.country_code is not None:
            
            order["shipTo"]["country"] = order_details.country_code
        
        if order_details.payment_date is not None:
            
            order["paymentDate"] = order_details.payment_date
        
        if order_details.customer_notes is not None:
            
            order["customerNotes"] = order_details.customer_notes
        
        if order_details.internal_note is not None:
            
            order["internalNotes"] = order_details.internal_note
        
        if order_details.gift_message is not None:
            
            order["giftMessage"] = order_details.gift_message
        
        if order_details.requested_shipping_method is not None:
            
            order["requestedShippingService"] = order_details.requested_shipping_method
        
        if order_details.items_sku is not None:
            
            order["items"][0]["sku"] = order_details.items_sku
        
        if order_details.image_url is not None:
            
            order["items"][0]["imageUrl"] = order_details.image_url
        
        if order_details.buyer_name is not None:
            
            order["billTo"]["name"] = order_details.buyer_name
        
        if order_details.buyer_email is not None:
            
            order["billTo"]["email"] = order_details.buyer_email
        
        if order_details.recipient_company is not None:
            
            order["shipTo"]["company"] = order_details.recipient_company
        
        if order_details.address_line2 is not None:
            
            order["shipTo"]["street2"] = order_details.address_line2
        
        if order_details.recipient_state is not None:
            
            order["shipTo"]["state"] = order_details.recipient_state
        
        if order_details.recipient_phone is not None:
            
            order["shipTo"]["phone"] = order_details.recipient_phone
        
        response = rest("POST", url, access_token, order)
        
        return json.loads(response.text)
    
    
    def verify(self, context, params):
        
        """ Verify """
        
        # URL
        url = "https://ssapi.shipstation.com/users"
        
        # Generate access token
        access_token = get_basic_token(context["headers"])
        
        # Request
        response  = rest("GET", url, access_token)
        
        # Return response
        return json.loads(response.text)[0], response.status_code