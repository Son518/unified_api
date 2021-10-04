from calendar import c
from re import sub
import stripe
from stripe.api_resources import customer

from flask import jsonify

# from payment_processing.stripe import util
# from payment_processing.stripe import util
from . import StripeCustomer, StripeSubscription, StripePaymentIntent, StripeBalanceTransaction
from . import StripePayout, StripeInvoice, StripeCharge, StripeInvoiceItem, StripeRefund, StripeWebhook

class StripeApi:
    """Strip API calls. This class is inherited by App class, so that these methods can be called with App's reference.
    """


    # TODO: move this to util
    # OR, shall we make it a part of data class?
    def _customer_to_dict(self, customer_data):
        
        address = customer_data.get('address', {})
        customer_entity = StripeCustomer(
            id=customer_data['id'],
            name=customer_data['name'],
            description=customer_data['description'],
            email=customer_data['email'],
            phone=customer_data['phone'],
            address_line1=address.get('line1'),
            address_line2=address.get('line2'),
            city=address.get('city'),
            postal_code=address.get('postal_code'),
            state=address.get('state'),
            ## country: str = None
            country_code=address.get('country')
        )

        return customer_entity.__dict__


    def customer(self, context, params):
        """Create a customer
        """

        stripe.api_key = context['headers']['api_key']

        customer_data = stripe.Customer.retrieve(params['id'])
        return self._customer_to_dict(customer_data)


    def customer_by_id(self, context, params):
        return self.customer(context, params)


    def customers_by_email(self, context, params):  # OR customers_by_email ??
        """[summary]

        Args:
            context (dict): Context data, such as headers
            params (dict): Parameters passed

        Returns:
            list: List of customers, found by given email
        """
        context.update({
            'condition':{
                'email': params['email']
            }
        })
        return self.customers(context, params)
        

    def customers_by_created_time(self, context, params):
        stripe.api_key = context['headers']['api_key']

        context.update({
            'condition':{
                'created': params['created_time']
            }
        })

        return self.customers(context, params)


    def customers(self, context, params):

        stripe.api_key = context['headers']['api_key']

        condition = context.get('condition', {})
        customer_list = stripe.Customer.list(**condition)['data']
        result_list = []
        for customer_data in customer_list:
            result_list.append(self._customer_to_dict(customer_data))

        return jsonify(result_list)


    def _subscription_to_dict(self, subs_data):

        price = subs_data['items']['data'][0]['price']
        subs_entity = StripeSubscription(
            id=subs_data['id'],
            customer_id=subs_data['customer'],
            cancel_at_period_end=subs_data['cancel_at_period_end'],
            collection_method=subs_data['collection_method'],
            # coupon=subs_data['coupon'],  # coupon is not returned in Subscription data

            ## It is found that if a 'discount' is applied to subscription and discount has a coupon then 
            ## subscription has 'coupon
            ##
            ## It means, assuming only existing coupons will be used,
            ## that to create a subscription with coupon, we need to create a coupon
            metadata=subs_data['metadata'],  ## Metadata unification ??
            ##
            ## start_date and end_date SHOULD be there for a subscription
            ##
            price_id=price['id'],
            currency=price['currency'],
            product_id=price['product'],
            unit_price=price['unit_amount'],
            recurring_interval=price['recurring']['interval'],
            recurring_count=price['recurring']['interval_count']
        )

        return subs_entity.__dict__


    def subscription(self, context, params):
        """Get a Subscription by ID"""

        stripe.api_key = context['headers']['api_key']
        subs_data = stripe.Subscription.retrieve(params['id'])

        return self._subscription_to_dict(subs_data)


    def subscription_by_id(self, context, params):
        return self.subscription(context, params)


    def subscriptions_by_created_time(self, context, params):

        return self.subscriptions(context.update({
            'condition':{
                'created': params['created_time']
            }
        }))


    def subscriptions(self, context, params):

        stripe.api_key = context['headers']['api_key']

        condition = context.get('condition', {})
        subs_list = stripe.Subscription.list(**condition)['data']
        result_list = []
        for subs_data in subs_list:
            result_list.append(self._subscription_to_dict(subs_data))

        return jsonify(result_list)


    def charge(self, context, params):

        stripe.api_key = context['headers']['api_key']

        charge_data = stripe.Charge.retrieve(params['id'])
        charge_entity = StripeCharge(
            id=charge_data['id'],
            amount=charge_data['amount'], ## * 100?
            balance_transaction_id=charge_data['balance_transaction'],
            # billing=charge_data['billing'],
            currency=charge_data['currency'],
            customer_id=charge_data['customer'],
            description=charge_data['description'],
            invoice_id=charge_data['invoice'],
            payment_intent_id=charge_data['payment_intent'],
            # payment_method_details: dict = field(default_factory=dict)
            # shipping: dict = field(default_factory=dict)  # Shipping Address
            status=charge_data['status']
        )

        return charge_entity.__dict__

    def charge_by_id(self, context, params):
        return self.charge(context, params)

    def _balance_transaction_to_dict(self, bal_trans_data):
        
        bal_trans_entity = StripeBalanceTransaction(
            id=bal_trans_data['id'],
            amount=bal_trans_data['amount'],  ## cents
            currency=bal_trans_data['currency'],
            description=bal_trans_data['description'],
            fee=bal_trans_data['fee'],
            ## fee_details: dict = field(default_factory=dict)  # Fee details
            net_amount=bal_trans_data['net'],
            source_id=bal_trans_data['source'],
            status=bal_trans_data['status'],
            txn_type=bal_trans_data['type'],
            created=bal_trans_data['created'],
            available_on=bal_trans_data['available_on'] # datetime / timestamp
        )

        return bal_trans_entity.__dict__


    def balance_transaction(self, context, params):

        stripe.api_key = context['headers']['api_key']

        bal_trans_data = stripe.BalanceTransaction.retrieve(params['id'])

        return self._balance_transaction_to_dict(bal_trans_data)


    def balance_transaction_by_id(self, context, params):
        return self.balance_transaction(context, params)

    def balance_transactions(self, context, params):
        """
        """
        stripe.api_key = context['headers']['api_key']

        result_list = []
        bal_trans_list = stripe.BalanceTransaction.list()['data']
        for bal_trans_data in bal_trans_list:
            result_list.append(self._balance_transaction_to_dict(bal_trans_data))

        return jsonify(result_list)


    def invoice(self, context, params):
        
        stripe.api_key = context['headers']['api_key']

        invoice_data = stripe.Invoice.retrieve(params['id'])
        invoice_entity = StripeInvoice(
            id=invoice_data['id'],
            customer_id=invoice_data['customer'],
            description=invoice_data['description'],
            auto_advance=invoice_data['auto_advance'],
            payment_method=invoice_data['collection_method'],
            subscription_id=invoice_data['subscription'],  ## is this object or id?
            total=invoice_data['total']
        )

        return invoice_entity.__dict__


    def invoice_by_id(self, context, params):
        return self.invoice(context, params)


    def invoice_item(self, context, params):

        stripe.api_key = context['headers']['api_key']

        inv_item_data = stripe.InvoiceItem.retrieve(params['id'])
        invoice_entity = StripeInvoiceItem(
            id=inv_item_data['id'],
            customer_id=inv_item_data['customer'],
            amount=inv_item_data['amount'],
            currency=inv_item_data['currency'],
            description=inv_item_data['description'],
            ## metadata: dict = field(default_factory=dict)  HOW TO UNIFY DICTIONARIES??
            period_start=inv_item_data['period']['start'],
            period_end=inv_item_data['period']['end'],
            price_id=inv_item_data['price']['id'],
            proration=inv_item_data['proration'],
            quantity=inv_item_data['quantity'],
            ## price_type: str = None ## Type wasn't found, but price/type was for price type
        )

        return invoice_entity.__dict__


    def invoice_item_by_id(self, context, params):
        return self.invoice_item(context, params)

    def invoice_items(self, context, params):

        stripe.api_key = context['headers']['api_key']

        result_list = []
        inv_item_list = stripe.InvoiceItem.list()['data']
        for inv_item_data in inv_item_list:
            invoice_entity = StripeInvoiceItem(
                id=inv_item_data['id'],
                customer_id=inv_item_data['customer'],
                amount=inv_item_data['amount'],
                currency=inv_item_data['currency'],
                description=inv_item_data['description'],
                ## metadata: dict = field(default_factory=dict)  HOW TO UNIFY DICTIONARIES??
                period_start=inv_item_data['period']['start'],
                period_end=inv_item_data['period']['end'],
                price_id=inv_item_data['price']['id'],  ## id or price info?
                price=inv_item_data['price']['unit_amount'],
                proration=inv_item_data['proration'],
                quantity=inv_item_data['quantity'],
                price_type=inv_item_data['price']['type']
            )

            result_list.append(invoice_entity.__dict__)
                
        return jsonify(result_list)


    def invoice_items_by_created_time(self, context, params):

        stripe.api_key = context['headers']['api_key']

        inv_items = []
        inv_item_list = stripe.InvoiceItem.list(**context['condition'])
        for inv_item_data in inv_item_list:
            invoice_entity = StripeInvoiceItem(
                id=inv_item_data['id'],
                customer_id=inv_item_data['customer'],
                amount=inv_item_data['amount'],
                currency=inv_item_data['currency'],
                description=inv_item_data['description'],
                ## metadata: dict = field(default_factory=dict)  HOW TO UNIFY DICTIONARIES??
                period_start=inv_item_data['period']['start'],
                period_end=inv_item_data['period']['end'],
                price_id=inv_item_data['price'],
                proration=inv_item_data['proration'],
                quantity=inv_item_data['quantity'],
                ## price_type: str = None ## Type wasn't found, but price/type was for price type
            )

            inv_items.append(invoice_entity.__dict__)
        
        return jsonify(inv_items)


    # def current_balance(self, context, params):
    #     pass

    # def balance_history(self, context, params):
    #     pass


    def payouts(self, context, params):

        stripe.api_key = context['headers']['api_key']

        result_list = []
        payout_list = stripe.Payout.list()['data']
        for payout_data in payout_list:
            payout_entity = StripePayout(
                id = payout_data['id'],
                amount = payout_data['amount'],
                currency = payout_data['currency'],
                arrival_date = payout_data['arrival_date'],
                description = payout_data['description'],
                payment_method = payout_data['payment_method']
            )

            result_list.append(payout_entity.__dict__)

        return jsonify(result_list)


    def refunds(self, context, params): 

        stripe.api_key = context['headers']['api_key']

        result_list = []
        refund_list = stripe.Refund.list()['data']
        for refund_data in refund_list:
            print('====>>> refund_data', refund_data)
            refund_entity = StripeRefund(
                id = refund_data['id'],
                amount = refund_data['amount'],
                currency = refund_data['currency'],
                balance_transaction_id = refund_data['balance_transaction'],
                charge_id = refund_data['charge'],
                payment_intent_id = refund_data['payment_intent'],
                reason = refund_data['reason'],
                receipt_number = refund_data['receipt_number'],
                status = refund_data['status'],
                source_transfer_reversal = refund_data['source_transfer_reversal'],
                transfer_reversal = refund_data['transfer_reversal']
            )

            result_list.append(refund_entity.__dict__)

        return jsonify(result_list)
        

    def payment_intents(self, context, params):

        stripe.api_key = context['headers']['api_key']

        result_list = []
        pay_intent_list = stripe.PaymentIntent.list()['data']
        for pay_intent_data in pay_intent_list:
            pay_intent_entity = StripePaymentIntent(
                id = pay_intent_data['id'],
                amount = pay_intent_data['amount'],
                currency = pay_intent_data['currency'],
                customer_id = pay_intent_data['customer'],
                description = pay_intent_data['description'],
                payment_method = pay_intent_data['payment_method']
            )

            result_list.append(pay_intent_entity.__dict__)

        return jsonify(result_list)



    def webhook(self, context, params):
        stripe.api_key = context['headers']['api_key']

        webhook_data = stripe.WebhookEndpoint.retrieve(params['id'])
        webhook_entity = StripeWebhook(
            id=webhook_data['id'],
            enabled_event=webhook_data['enabled_events'][0],
            description=webhook_data['description'],
            created=webhook_data['created'],
            secret=webhook_data['secret'],
            status=webhook_data['status'],
            url=webhook_data['url']
        )
        
        return webhook_entity.__dict__



