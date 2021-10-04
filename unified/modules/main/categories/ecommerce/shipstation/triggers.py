from unified.core.triggers import Triggers
from ecommerce.shipstation.entities.shipstation_order import ShipstationOrder
from ecommerce.shipstation.util import get_basic_token,rest
import json

class ShipStationTrigger(Triggers):
    
    def new_order(self, context, payload):
        
        # Get access_token
        access_token = get_basic_token(context['headers'])
        url = payload['resource_url']
        
        # Get the order details
        response = rest("GET", url, access_token)
        customer_data = json.loads(response.text)["orders"][0]
        
        return self.mapping_of_customer(customer_data)
    
    
    def mapping_of_customer(self, customer_data):
        """ mapping details to customer """
        
        result = ShipstationOrder(
            shipstation_store = customer_data.get('shipstation_store', None),
            order_status_id = customer_data.get('orderStatus', None),
            order_date = customer_data.get('orderDate', None),
            buyer_name = customer_data['billTo']['name'] if customer_data['billTo']['name'] else None,
            payment_date = customer_data.get('paymentDate', None),
            recipient_name = customer_data['shipTo']['name'] if customer_data['shipTo']['name'] else None,
            recipient_company = customer_data['shipTo']['company'] if customer_data['shipTo']['company'] else None,
            address_line1 = customer_data['shipTo']['street1'] if customer_data['shipTo']['street1'] else None,
            address_line2 = customer_data['shipTo']['street2'] if customer_data['shipTo']['street2'] else None,
            address_line3 = customer_data['shipTo']['street3'] if customer_data['shipTo']['street3'] else None,
            recipient_city = customer_data['shipTo']['city'] if customer_data['shipTo']['city'] else None,
            recipient_state = customer_data['shipTo']['state'] if customer_data['shipTo']['state'] else None,
            pin_code = customer_data['shipTo']['postalCode'] if customer_data['shipTo']['postalCode'] else None,
            country_code = customer_data['shipTo']['country'] if customer_data['shipTo']['country'] else None,
            recipient_phone = customer_data['shipTo']['phone'] if customer_data['shipTo']['phone'] else None,
            ammount_paid = customer_data.get('amountPaid', None),
            tax_paid = customer_data.get("taxAmount", None),
            shipping_paid = customer_data.get("shippingAmount", None),
            customer_notes = customer_data.get('customerNotes', None),
            internal_note = customer_data.get('internalNotes', None),
            is_a_gift = customer_data.get('gift', None),
            gift_message = customer_data.get('giftMessage', None),
            requested_shipping_method = customer_data.get('requestedShippingService', None),
            items_sku = customer_data['items'][0]['sku'] if len(customer_data['items']) > 0 else None,
            item_name = customer_data['items'][0]['name'] if len(customer_data['items']) > 0 else None,
            image_url = customer_data['items'][0]['imageUrl'] if len(customer_data['items']) > 0 else None,
            quantity = customer_data['items'][0]['quantity'] if len(customer_data['items']) > 0 else None,
            unit_price = customer_data['items'][0]['unitPrice'] if len(customer_data['items']) > 0 else None
        )
        
        return result.__dict__