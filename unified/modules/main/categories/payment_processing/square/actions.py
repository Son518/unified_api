import json
import uuid

from unified.core.actions import Actions
from . import util

from payment_processing.square.entities.square_customer import SquareCustomer
from payment_processing.square.entities.square_card import SquareCard
from payment_processing.square.entities.square_refund import SquareRefund
from payment_processing.square.entities.square_transaction import SquareTransaction
class SquareActions(Actions):
    # def forms(self, context, payload):
    #     if method == 'POST':
    #         create_form
    #     elif method == 'GET':
    #         get_forms/forms_list
    #     elif method == 'PUT'
    #         update_form
    #     elif METHOD == 'DELETE??'
    #         delete_form


    def create_customer(self, context, payload):
        """Create a new customer"""

        client = util.get_square_client(context)

        customer_entity = SquareCustomer(**payload)
        customer_data = {
            "given_name": customer_entity.first_name,
            "nickname": customer_entity.nickname,
            "family_name": customer_entity.last_name,
            "email_address": customer_entity.email,
            "address": {
                "address_line_1": customer_entity.address_line1,
                "address_line_2": customer_entity.address_line2,
                "locality": customer_entity.locality,
                "administrative_district_level_1": customer_entity.city, ## OR should it be customer_entity.state ??
                "postal_code": customer_entity.postal_code,
                "country": customer_entity.country_code
            },
            "phone_number": customer_entity.phone,
            "reference_id": customer_entity.reference_id,            
            "note": customer_entity.description
        }

        result = client.customers.create_customer(customer_data)
        
        if result.is_success():
            result.body['id'] = result.body['customer']['id']
            return result.body
        else: # resp.is_error()
            return json.dumps(result.errors)


    def update_customer(self, context, payload):
        """Updates an existing customer"""

        client = util.get_square_client(context)

        customer_entity = SquareCustomer(**payload)
        customer_data = {
            "given_name": customer_entity.first_name,
            "nickname": customer_entity.nickname,
            "family_name": customer_entity.last_name,
            "email_address": customer_entity.email,
            "address": {
                "address_line_1": customer_entity.address_line1,
                "address_line_2": customer_entity.address_line2,
                "locality": customer_entity.locality,
                "administrative_district_level_1": customer_entity.city, ## OR should it be customer_entity.state ??
                "postal_code": customer_entity.postal_code,
                "country": customer_entity.country_code
            },
            "phone_number": customer_entity.phone,
            "reference_id": customer_entity.reference_id,            
            "note": customer_entity.description
        }
        
        result = client.customers.update_customer(customer_entity.id, customer_data)
        
        if result.is_success():
            result.body['id'] = result.body['customer']['id']
            return result.body
        else: # resp.is_error()
            return json.dumps(result.errors)


    def complete_payment(self, context, payload):
        """Complete the payment of APPROVED status, with given id"""

        client = util.get_square_client(context)

        result = client.payments.complete_payment(payment_id=payload['id'])

        if result.is_success():
            return result.body
        else: # if result.is_error():
            return json.dumps(result.errors)


    def add_customer_to_group(self, context, payload):
        """Add group to customer"""

        client = util.get_square_client(context)
        result = client.customers.add_group_to_customer(
            customer_id = payload['customer_id'],
            group_id = payload['group_id']  ## OR should it be customer_id and id (for group)??
        )

        if result.is_success():
            return result.body
        else: # if result.is_error():
            return json.dumps(result.errors)


    def capture_transaction(self, context, payload):
        """Captures a transaction"""

        client = util.get_square_client(context)
        tx_entity = SquareTransaction(**payload)

        tx_data = {
            'location_id': tx_entity.location_id,
            'transaction_id': tx_entity.transaction_id,
        }

        result = client.transactions.capture_transaction(**tx_data)

        if result.is_success():
            return result.body
        else: # if result.is_error():
            return json.dumps(result.errors)


    def create_credit_card(self, context, payload):
        """Adds a card on file to an existing merchant."""

        client = util.get_square_client(context)
        card_entity = SquareCard(**payload)

        card_data = {
            "idempotency_key": card_entity.idempotency_key or uuid.uuid4().hex,
            "source_id": card_entity.source_id,
            "card": {
                "cardholder_name": card_entity.cardholder_name,
                "billing_address": {
                    "address_line_1": card_entity.address_line1,
                    "address_line_2": card_entity.address_line2,
                    "locality": card_entity.locality,
                    "administrative_district_level_1": card_entity.city,  ## Or should itbe card_entity.state ??
                    "postal_code": card_entity.postal_code,
                    "country": card_entity.coutry_code,
                },
                "customer_id": card_entity.customer_id,
                "reference_id": "user-id-1"
            }
        }

        result = client.cards.create_card(card_data)

        if result.is_success():
            return result.body
        else: # if result.is_error():
            return json.dumps(result.errors)

    
    def create_refund2(self, context, payload):
        """Create Payment Refund. Means Refund a payment."""

        client = util.get_square_client(context)
        refund_entity = SquareRefund(**payload)

        app_fee_money = {}
        if refund_entity.app_fee_amount:
            app_fee_money['amount'] = refund_entity.app_fee_amount

        if refund_entity.app_fee_amount:
            app_fee_money['currency'] = refund_entity.app_fee_currency_code

        refund_data = {
            "idempotency_key": refund_entity.idempotency_key or uuid.uuid4().hex,
            "amount_money": {
                "amount": refund_entity.amount,
                "currency": refund_entity.currency_code,
            },

            "payment_id": refund_entity.payment_id,
            "reason": refund_entity.reason,
        }

        if app_fee_money:
            refund_data['app_fee_money'] = app_fee_money

        result = client.refunds.refund_payment(refund_data)

        if result.is_success():
            return result.body
        else: # if result.is_error():
            return json.dumps(result.errors)
