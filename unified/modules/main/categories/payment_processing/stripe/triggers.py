
from . import StripeCustomer, StripeSubscription, StripePaymentIntent, StripeBalanceTransaction
from . import StripePayout, StripeInvoice, StripeCharge, StripeInvoiceItem, StripeRefund

class StripeTriggers:
    def new_customer(self, context, payload):
        # customer.created
        
        customer_data = payload['data']['object']
        address = customer_data.get('address') or {}
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
            country_code=address.get('country')
        )

        return customer_entity.__dict__


    def subscription_cancelled(self, context, payload):
        # subscription_schedule.canceled

        subs_data = payload['data']['object']
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
            # metadata=subs_data['metadata'],  ## Metadata unification ??
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


    def new_charge(self, context, payload):
        # charge.pending - Occurs whenever a pending charge is created.
        # charge.cucceeded - Occurs whenever a charge is created and is successful.
        charge_data = payload['data']['object']
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


    # def new_event(self, context, payload):
    # don't know what is expected with this

    def new_coupon(self, context, payload):
        # coupon.created - Occurs whenever a coupon is created.
        ## new entity StripeCoupon required
        pass

    def new_invoice(self, context, payload):
        # invoice.created - Occurs whenever a new invoice is created.

        invoice_data = payload['data']['object']
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


    def new_invoice_item(self, context, payload):
        # invoiceitem.created - Occurs whenever an invoice item is created.
        inv_item_data = payload['data']['object']
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

        return invoice_entity.__dict__


    def new_order(self, context, payload):
        # order.created - Occurs whenever an order is created.
        ## new entity StripeOrder required
        pass


    def new_plan(self, context, payload):
        # plan.created - Occurs whenever a plan is created.
        ## new entity StripePlan required
        pass


    def new_refund(self, context, payload):
        # refund.created - Occurs whenever a refund is created.

        refund_data = payload['data']['object']
        refund_entity = StripeRefund(
            id = refund_data['id'],
            amount = refund_data['amount'],
            currency = refund_data['currency'],
            balance_transaction_id = refund_data['balance_transaction'],
            charge_id = refund_data['refunds']['data'][0]['charge'],
            payment_intent_id = refund_data['payment_intent'],
            reason = refund_data['refunds']['data'][0]['reason'],
            receipt_number = refund_data['receipt_number'],
            status = refund_data['status'],
            source_transfer_reversal = refund_data['refunds']['data'][0]['source_transfer_reversal'],
            transfer_reversal = refund_data['refunds']['data'][0]['transfer_reversal']
        )

        return refund_entity.__dict__
