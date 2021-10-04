import stripe
from stripe import webhook
from stripe.api_resources import invoice, invoice_item

# from payment_processing.stripe import util
from . import StripeCustomer, StripeSubscription, StripePaymentIntent
from . import StripePayout, StripeInvoice, StripeCharge, StripeInvoiceItem, StripeWebhook

from unified.core.actions import Actions


class StripeActions(Actions):
    # Set your secret key. Remember to switch to your live secret key in production.
    # See your keys here: https://dashboard.stripe.com/apikeys

    def create_customer(self, context, customer_payload):
        """Create a customer
        """
 
        stripe.api_key = context['headers']['api_key']

        customer_entity = StripeCustomer(**customer_payload)
        customer_data = {
            "name": customer_entity.name,
            "description": customer_entity.description,
            "email": customer_entity.email,
            "phone": customer_entity.phone,
            "payment_method": customer_entity.payment_method,
            "address" : {
                "line1": customer_entity.address_line1, 
                "line2": customer_entity.address_line2,
                "city": customer_entity.city,
                "postal_code": customer_entity.postal_code,
                "state": customer_entity.state,
                "country": customer_entity.country_code,
            }
        }

        resp = stripe.Customer.create(**customer_data)

        return resp


    def update_customer(self, context, customer_payload):
        """Updates an existing customer"""

        stripe.api_key = context['headers']['api_key']

        customer_entity = StripeCustomer(**customer_payload)
        customer_data = {
            "name": customer_entity.name,
            "description": customer_entity.description,
            "email": customer_entity.email,
            "phone": customer_entity.phone,
            "payment_method": customer_entity.payment_method,
            "address" : {
                "line1": customer_entity.address_line1, 
                "line2": customer_entity.address_line2,
                "city": customer_entity.city,
                "postal_code": customer_entity.postal_code,
                "state": customer_entity.state,
                "country": customer_entity.country_code,
            }
        }

        resp = stripe.Customer.modify(customer_entity.id, **customer_data)
        
        return resp
        

    def delete_customer(self, context, customer_payload):
        """Updates an existing customer"""

        stripe.api_key = context['headers']['api_key']

        resp = stripe.Customer.delete(customer_payload['id'])
        
        return resp


    def create_subscription(self, context, subs_payload):
        """Creates a new subscription"""

        stripe.api_key = context['headers']['api_key']

        subs_entity = StripeSubscription(**subs_payload)
        

        """
        *** price-object        
        id
        currency
        product
        unit_amount_decimal  ## OR unit_amount
        quantity

        *** product-object
        id
        active: bool
        name
        description
        """

        subs_item = {}
        if subs_entity.price_id:
            subs_item['price'] = subs_entity.price_id
        else:
            subs_item['price_data'] = {
                "currency": subs_entity.currency,
                "product": subs_entity.product_id, 
                "unit_amount_decimal": subs_entity.unit_price,  ## OR unit_amount
                # "quantity": : subs_entity.quantity,  - optional
                "recurring": {
                    "interval": subs_entity.recurring_interval,
                    "interval_count": subs_entity.recurring_count,
                } 
            }

        subs_data = {
            "customer": subs_entity.customer_id,
            "items": [
                subs_item,
            ]

        }

        resp = stripe.Subscription.create(**subs_data)
        
        return resp
        

    def update_subscription(self, context, subs_payload):
        """Updates an existing subscription"""

        stripe.api_key = context['headers']['api_key']

        subs_entity = StripeSubscription(**subs_payload)
        subs_item = {}
        if subs_entity.price_id:
            subs_item['price'] = subs_entity.price_id
        else:
            subs_item['price_data'] = {
                    "currency": subs_entity.currency,
                    "product": subs_entity.product_id, 
                    "unit_amount_decimal": subs_entity.unit_price,  ## OR unit_amount
                    # "quantity": : subs_entity.quantity,  - optional
                    "recurring": {
                        "interval": subs_entity.recurring_interval,
                        "interval_count": subs_entity.recurring_count,
                    } 
            }

        subs_data = {
            "items": [
                subs_item,
            ]

        }

        resp = stripe.Subscription.modify(subs_entity.id, **subs_data)
        
        return resp


    def cancel_subscription(self, context, subs_payload):
        """Cancel an existing subscription"""

        stripe.api_key = context['headers']['api_key']

        resp = stripe.Subscription.delete(subs_payload['id'])
        
        return resp

    def create_payment_intent(self, context, pay_int_payload):
        """Creates a new Payment Intent"""
        
        stripe.api_key = context['headers']['api_key']

        pay_int_entity = StripePaymentIntent(**pay_int_payload)
        pay_int_data = {
            "amount": pay_int_entity.amount,
            "currency": pay_int_entity.currency,
            "customer": pay_int_entity.customer_id,
            "description": pay_int_entity.description,
            "payment_method": pay_int_entity.payment_method,
        }

        resp = stripe.PaymentIntent.create(**pay_int_data)

        return resp


    def update_payment_intent(self, context, pay_int_payload):
        """Updates an existing Payment Intent"""

        stripe.api_key = context['headers']['api_key']

        pay_int_entity = StripePaymentIntent(**pay_int_payload)
        pay_int_data = {
            "amount": pay_int_entity.amount,
            "currency": pay_int_entity.currency,
            "customer": pay_int_entity.customer_id,
            "description": pay_int_entity.description,
            "payment_method": pay_int_entity.payment_method,
        }

        resp = stripe.PaymentIntent.modify(pay_int_entity.id, **pay_int_data)

        return resp

    def create_payout(self, context, payout_payload):
        """Creates a new Payout"""

        payout_entity = StripePayout(**payout_payload)
        payout_data = {
            "amount": payout_entity.amount,
            "currency": payout_entity.currency,
            "description": payout_entity.description,
            # "method": payout_entity.payment_method,
        }

        resp = stripe.Payout.create(**payout_data)

        return resp


    def create_invoice(self, context, invoice_payload):
        """Create a new Invoice"""

        stripe.api_key = context['headers']['api_key']

        invoice_entity = StripeInvoice(**invoice_payload)
        invoice_data = {
            "customer": invoice_entity.customer_id,
            "subscription": invoice_entity.subscription_id,
            "auto_advance": invoice_entity.auto_advance,
            "description": invoice_entity.description,
        }

        resp = stripe.Invoice.create(**invoice_data)

        return resp


    def update_invoice(self, context, invoice_payload):
        """Update an existing Invoice"""

        stripe.api_key = context['headers']['api_key']

        invoice_entity = StripeInvoice(**invoice_payload)
        invoice_data = {
            "customer": invoice_entity.customer_id,
            "subscription": invoice_entity.subscription_id,
            "auto_advance": invoice_entity.auto_advance,
            "description": invoice_entity.description,
        }

        resp = stripe.Invoice.modify(invoice_entity.id, **invoice_data)

        return resp


    def create_invoice_item(self, context, invoice_item_payload):
        """Create a new Invoice-Item"""
        
        stripe.api_key = context['headers']['api_key']

        invoice_item_entity = StripeInvoiceItem(**invoice_item_payload)
        invoice_item_data = {
            'customer': invoice_item_entity.customer_id,
            'amount': invoice_item_entity.amount, ## * 100 ??
            'currency': invoice_item_entity.currency,
            'description': invoice_item_entity.description,
            # 'metadata': invoice_item_entity.metadata, ## HOW TO unify metadata?
            'period': {
                'start': invoice_item_entity.period_start,
                'end': invoice_item_entity.period_end,
            },
            'price': invoice_item_entity.price_id,
            'proration': invoice_item_entity.proration,
            'quantity': invoice_item_entity.quantity,
            # 'price_type': invoice_item_entity.price_type,  # not found in documentation
        }

        resp = stripe.InvoiceItem.create(**invoice_item_data)

        return resp


    def update_invoice_item(self, context, invoice_item_payload):
        """Update an existing Invoice-Item"""
        
        stripe.api_key = context['headers']['api_key']


    def create_charge(self, context, charge_payload):
        """Create a new Charge"""

        stripe.api_key = context['headers']['api_key']

        charge_entity = StripeCharge(**charge_payload)
        charge_data = {
            "amount": charge_entity.amount,
            "currency": charge_entity.currency,
            # "billing": charge_entity.billing,
            "customer": charge_entity.customer_id,
            "description": charge_entity.description,
            "invoice": charge_entity.invoice_id,
            "status": charge_entity.status,
        }

        resp = stripe.Charge.create(**charge_data)

        return resp


    def create_webhook(self, context, webhook_payload):
        """Create a new Webhook"""

        stripe.api_key = context['headers']['api_key']

        webhook_entity = StripeWebhook(**webhook_payload)
        webhook_data = {
            "enabled_events": [webhook_entity.enabled_event],
            "description": webhook_entity.description,
            "url": webhook_entity.url,
            "created": webhook_entity.created,
            "status": webhook_entity.status,
            "secret": webhook_entity.secret,
        }

        resp = stripe.WebhookEndpoint.create(**webhook_data)

        return resp

        
    def update_webhook(self, context, webhook_payload):
        """Update an existing Webhook"""

        stripe.api_key = context['headers']['api_key']

        webhook_entity = StripeWebhook(**webhook_payload)
        webhook_data = {
            "enabled_events": [webhook_entity.enabled_event],
            "description": webhook_entity.description,
            "url": webhook_entity.url,
            "created": webhook_entity.created,
            "status": webhook_entity.status,
            "secret": webhook_entity.secret,
        }

        resp = stripe.WebhookEndpoint.modify(webhook_entity.id, **webhook_data)

        return resp


    def delete_webhook(self, context, webhook_payload):
        """Delete an existing webhook"""

        stripe.api_key = context['headers']['api_key']

        resp = stripe.WebhookEndpoint.delete(webhook_payload['id'])
        
        return resp


