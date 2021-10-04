from unified.core.actions import Actions
from drip_emails.convertkit import util
from drip_emails.convertkit.entities.convertkit_purchase import ConvertkitPurchase
from drip_emails.convertkit.entities.convertkit_subscriber import ConvertkitSubscriber
import json

class ConvertkitActions(Actions):
    def add_subscriber_to_form(self, context, payload):
        '''add subscriber to form'''

        headers = context['headers']
        subscriber = ConvertkitSubscriber(**payload)
        url = f"forms/{subscriber.form_id}/subscribe?api_key={headers['api_key']}"
        request_body = self.body_of_subscriber(subscriber)
        response = util.rest("POST", url, context, request_body)

        return json.loads(response.text), response.status_code

    def add_subscriber_to_sequence(self, context, payload):
        '''add subscriber to sequence'''

        headers = context['headers']
        subscriber = ConvertkitSubscriber(**payload)
        url = f"sequences/{subscriber.sequence_id}/subscribe?api_key={headers['api_key']}"
        request_body = self.body_of_subscriber(subscriber)
        response = util.rest("POST", url, context, request_body)

        return json.loads(response.text), response.status_code

    def add_tag_to_subscriber(self, context, payload):
        '''add tag to subscriber'''

        headers = context['headers']
        subscriber = ConvertkitSubscriber(**payload)
        url = f"tags/{subscriber.tag_id}/subscribe?api_key={headers['api_key']}"
        request_body = self.body_of_subscriber(subscriber)
        response = util.rest("POST", url, context, request_body)

        return json.loads(response.text), response.status_code

    def body_of_subscriber(self, subscriber):
        request_body = {
            "email": subscriber.email,
            "first_name": subscriber.first_name
        }
        return request_body

    def create_purchase(self, context, payload):
        '''create purchase '''

        headers = context['headers']
        url = f"purchases?api_secret={headers['api_secret']}"
        purchase = ConvertkitPurchase(**payload)
        request_body = {
            "transaction_id": purchase.transaction_id,
            "email_address": purchase.email,
            "currency": purchase.currency_id,
            "transaction_time": purchase.transaction_time,
            "subtotal": purchase.subtotal,
            "discount": purchase.discount,
            "tax": purchase.tax,
            "shipping": purchase.shipping,
            "total": purchase.total,
            "status": purchase.status,
            "products": [
                {
                    "sku": purchase.product_sku,
                    "name": purchase.product_name,
                    "quantity": purchase.product_quantity,
                    "unit_price": purchase.product_price,
                    "pid": purchase.product_id,
                    "lid": purchase.list_id
                }
            ]
        }
        response = util.rest("POST", url, context, request_body)

        return json.loads(response.text), response.status_code

    def remove_tag_from_subscriber(self, context, payload):
        '''remove tag from subscriber'''

        headers = context['headers']
        subscriber = ConvertkitSubscriber(**payload)
        url = f"tags/{subscriber.tag_id}/unsubscribe?api_secret={headers['api_secret']}"
        request_body = {
            "email": subscriber.email
        }
        response = util.rest("POST", url, context, request_body)

        return json.loads(response.text), response.status_code
