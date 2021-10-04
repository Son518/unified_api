from unified.core.triggers import Triggers
from ecommerce.shopify.api import ShopifyApi
from ecommerce.shopify.entities.shopify_order import ShopifyOrder


class ShopifyTrigger(Triggers):
    def new_customer(self, context, payload):
        return ShopifyApi().mapping_of_customer(payload)

    def new_product(self, context, payload):
        return ShopifyApi().mapping_of_product(payload)

    def updated_customer(self, cotext, payload):
        return ShopifyApi().mapping_of_customer(payload)

    def new_draft_order(self, context, payload):
        order = ShopifyOrder(
            order_id=payload['id'],
            product_variant_id=payload.get('line_items')[0].get('variant_id'),
            product_quantity=payload.get('line_items')[0].get('quantity'),
            note=payload.get('note'),
            customer_id=payload.get('customer').get(
                'id') if payload.get('customer') else None,
            tags=payload.get('tags'),
            fulfillment_status=payload.get('status'),
            shipping_address_first_name=payload.get('shipping_address').get(
                'first_name') if payload.get('shipping_address') else None,
            shipping_address_last_name=payload.get('shipping_address').get(
                'last_name') if payload.get('shipping_address') else None,
            shipping_address_company=payload.get('shipping_address').get(
                'company') if payload.get('shipping_address') else None,
            shipping_address_phone=payload.get('shipping_address').get(
                'phone') if payload.get('shipping_address') else None,
            shipping_address_address=payload.get('shipping_address').get(
                'address1') if payload.get('shipping_address') else None,
            shipping_address_city=payload.get('shipping_address').get(
                'city') if payload.get('shipping_address') else None,
            shipping_address_country=payload.get('shipping_address').get(
                'country') if payload.get('shipping_address') else None,
            shipping_address_state=payload.get('shipping_address').get(
                'province') if payload.get('shipping_address') else None,
            shipping_address_postal=payload.get('shipping_address').get(
                'zip') if payload.get('shipping_address') else None,
            billing_address_first_name=payload.get('billing_address').get(
                'first_name') if payload.get('billing_address') else None,
            billing_address_last_name=payload.get('billing_address').get(
                'last_name') if payload.get('billing_address') else None,
            billing_address_company=payload.get('billing_address').get(
                'company') if payload.get('billing_address') else None,
            billing_address_phone=payload.get('billing_address').get(
                'phone') if payload.get('billing_address') else None,
            billing_address_address=payload.get('billing_address').get(
                'address1') if payload.get('billing_address') else None,
            billing_address_city=payload.get('billing_address').get(
                'city') if payload.get('billing_address') else None,
            billing_address_country=payload.get('billing_address').get(
                'country') if payload.get('billing_address') else None,
            billing_address_state=payload.get('billing_address').get(
                'province') if payload.get('billing_address') else None,
            billing_address_postal=payload.get('billing_address').get(
                'zip') if payload.get('billing_address') else None,
            email=payload.get('email'),
            taxes_included=payload.get('taxes_included'),
            currency=payload.get('currency'),
            name=payload.get('name'),
            total_price=payload.get('total_price')
        )
        return order.__dict__
