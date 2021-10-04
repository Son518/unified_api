import json

from . import util

from payment_processing.entities.customer import Customer
from payment_processing.square.entities.square_transaction import SquareTransaction
from payment_processing.square.entities.square_refund import SquareRefund
from payment_processing.square.entities.square_payment import SquarePayment

class SquareApi:

    def _customer_data_to_entity(self, customer_data):
        if customer_data.get('address'):
            addr = {
                'address_line1': customer_data['address']['address_line_1'],
                'address_line2': customer_data['address']['address_line_2'],
                'locality': customer_data['address'].get('locality'),
                'city': customer_data['address']['administrative_district_level_1'],
                'postal_code': customer_data['address']['postal_code'],
                'country_code': customer_data['address'].get('country'),  ## NOT returning value for US?
            }
        else:
            addr = {}

        customer_entity = Customer(
            id=customer_data['id'],
            name=customer_data['given_name'],
            family_name=customer_data.get('family_name'),
            email=customer_data.get('email'),
            phone=customer_data.get('phone_number'),
            **addr,
        )

        return customer_entity


    def customer(self, context, params):
        """Get a customer, with given 'id of the form"""

        client = util.get_square_client(context)
        result = client.customers.retrieve_customer(params['id'])
        
        if result.is_success():
            customer_data = result.body['customer']
            customer_entity = self._customer_data_to_entity(customer_data)

            return customer_entity.__dict__

        else: # result.is_error()
            return json.dumps(result.errors)


    def customer_by_id(self, context, params):
        self.customer(context, params)


    def customers(self, context, params):
        """Get list of all customers"""

        client = util.get_square_client(context)
        result = client.customers.list_customers()

        if result.is_success():
            customer_list = []
            for customer_data in result.body['customers']:
                customer_entity = self._customer_data_to_entity(customer_data)

                customer_list.append(customer_entity.__dict__)

            #TODO: Remove json.dumps from here and use jsonify in main application.py
            #      Currently it can't be done without breaking already merged apps.
            #      Those apps require removal of json.dumps in the apps' code 
            return json.dumps(customer_list)  

        else: # result.is_error()
            return json.dumps(result.errors)


    def _search_customers(self, context, params):
        """Search customers by filter options"""

        client = util.get_square_client(context)

        search_data = {
            "query": {
                "filter": {
                },
            }
        }

        if 'limit' in params:
            search_data['limit'] = params['limit']

        if 'email' in params:
            search_data['query']['filter']['email_address'] = {'exact': params['email']}

        created_at = {}
        if 'start_date' in params:
            created_at["start_at"] = util.epoch_to_format(params['start_date'], '%Y-%m-%dT%H:%M:%S%z') ## "2018-01-01T00:00:00-00:00",

        if 'end_date' in params:
            created_at["end_at"] = util.epoch_to_format(params['end_date'], '%Y-%m-%dT%H:%M:%S%z') ## "2018-01-01T00:00:00-00:00",

        if 'start_date_time' in params:
            created_at["start_at"] = util.epoch_to_format(params['start_date_time'], '%Y-%m-%dT%H:%M:%S%z') ## "2018-01-01T00:00:00-00:00",

        if 'end_date_time' in params:
            created_at["end_at"] = util.epoch_to_format(params['end_date_time'], '%Y-%m-%dT%H:%M:%S%z') ## "2018-01-01T00:00:00-00:00",

        if created_at:
            search_data['query']['filter']['created_at'] = created_at

        
        result = client.customers.search_customers(search_data)

        if result.is_success():
            customer_list = []
            if result.body:
                for customer_data in result.body['customers']:
                    customer_entity = self._customer_data_to_entity(customer_data)

                    customer_list.append(customer_entity.__dict__)

            return json.dumps(customer_list)

        else: # result.is_error()
            return json.dumps(result.errors)


    def customer_by_email(self, context, params):
        """Search customer by email address"""

        return self._search_customers(context, params)  ## return ONLY one??


    def customers_by_created_time(self, context, params):
        """Search customers by created time"""

        return self._search_customers(context, params)

   
    def transactions(self, context, params):
        """Get list of transactions for one of the business locations.
        *TRANSACTIONS IS DEPRECATED*"""

        client = util.get_square_client(context)
        result = client.transactions.list_transactions(location_id=params['location_id'])

        if result.is_success():
            tx_list = []
            if result.body:
                for tx_data in result.body['transactions']:
                    tx_entity = SquareTransaction(
                        transaction_id=tx_data['id'],
                        location_id=tx_data['location_id'],
                    )

                    tx_list.append(tx_entity.__dict__)

            return json.dumps(tx_list) ## does it work with test_suite? {'content-type': 'application/json'}

        else: # result.is_error()
            return json.dumps(result.errors)


    def refunds(self, context, params):
        """Lists refunds for one of the business's locations.
        *TRANSACTIONS IS DEPRECATED*"""

        client = util.get_square_client(context)

        ## This is the side-effect of MERGING headers into params!
        params = util.strip_headers(params)
        result = client.refunds.list_payment_refunds()

        if result.is_success():
            refund_list = []
            if result.body:
                for refund_data in result.body['refunds']:
                    refund_entity = SquareRefund(
                        id=refund_data['id'],
                        status=refund_data['status'],
                        amount=refund_data['amount_money']['amount'],
                        currency_code=refund_data['amount_money']['currency'],
                        payment_id=refund_data['payment_id'],
                        order_id=refund_data['order_id'],
                        location_id=refund_data['location_id'],
                        reason=refund_data.get('reason')
                    )

                    refund_list.append(refund_entity.__dict__)

            return json.dumps(refund_list)

        else: # result.is_error()
            return json.dumps(result.errors)


    def payments(self, context, params):
        """Get list of payments"""

        client = util.get_square_client(context)
        params = util.strip_headers(params)
        result = client.payments.list_payments(**params)

        if result.is_success():
            payment_list = []
            if result.body:
                for payment_data in result.body['payments']:
                    payment_entity = self._payment_data_to_entity(payment_data)
                    payment_list.append(payment_entity.__dict__)

            return json.dumps(payment_list)

        else: # result.is_error()
            return json.dumps(result.errors)


    def _payment_data_to_entity(self, payment_data):
        payment_entity = SquarePayment(
            id=payment_data['id'],
            source_id=payment_data['source_id'],
            status=payment_data['status'],
            amount=payment_data['amount_money']['amount'],
            currency_code=payment_data['amount_money']['currency'],
            # tip_amount=payment_data['tip_money']['amount'],
            # tip_currency_code=payment_data['tip_money']['currency'],
            app_fee_amount=payment_data['app_fee_money']['amount'],
            app_fee_currency_code=payment_data['app_fee_money']['currency'],
            autocomplete=payment_data['autocomplete'],
            customer_id=payment_data['customer_id'],
            order_id=payment_data['order_id'],
            location_id=payment_data['location_id'],
            reference_id=payment_data['reference_id']
        )

        return payment_data


    def payment(self, context, params):
        """Get payment details"""

        client = util.get_square_client(context)
        client.payments.get_payment()
        payment_data = client.payments.get_payment(payment_id=params['id'])

        payment_entity = self._payment_data_to_entity(payment_data)
        return payment_entity.__dict__


    def payment_by_id(self, context, params):
        """Get payment details, with id"""

        return self.payment(context, params)


    def transaction(self, context, params):
        """Search customers by filter options"""

        client = util.get_square_client(context)
        result = client.transactions.retrieve_transaction(
            location_id=params['location_id'],
            transaction_id=params['transaction_id']
            )

        if result.is_success():
            tx_data = result.body['transaction']
            tx_entity = SquareTransaction(
                transaction_id=tx_data['id'],
                location_id=tx_data['location_id'],
            )
            return json.dumps(tx_entity.__dict__)

        else: # result.is_error()
            return json.dumps(result.errors)
