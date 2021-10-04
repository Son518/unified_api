import json
from ecommerce.shopify import util
from ecommerce.shopify.entities.shopify_product import ShopifyProduct
from ecommerce.shopify.entities.shopify_customer import ShopifyCustomer


class ShopifyApi:
    def customer_by_email(self, context, payload):
        '''Get customer by email'''

        access_token = context['headers']['access_token']
        url = f"admin/api/2021-07/customers.json?email={payload['email']}"
        response = util.rest(
            'GET', url, context['headers']['domain'], access_token)
        customer_data = json.loads(response.text)["customers"][0]

        return self.mapping_of_customer(customer_data)

    def mapping_of_customer(self, customer_obj):
        '''mappings of customer for apis and triggers'''

        cusomer = ShopifyCustomer(
            customer_id=customer_obj['id'],
            first_name=customer_obj.get('first_name'),
            last_name=customer_obj.get('last_name'),
            email_address=customer_obj.get('email'),
            company_name=customer_obj.get('default_address').get(
                'company') if customer_obj.get('default_address') else None,
            street_address=customer_obj.get('default_address').get(
                'address1') if customer_obj.get('default_address') else None,
            street_address_line2=customer_obj.get(
                'default_address').get('address2') if customer_obj.get('default_address') else None,
            city=customer_obj.get('default_address').get(
                'city') if customer_obj.get('default_address') else None,
            state=customer_obj.get('default_address').get(
                'province') if customer_obj.get('default_address') else None,
            country=customer_obj.get('default_address').get(
                'country') if customer_obj.get('default_address') else None,
            zip_code=customer_obj.get('default_address').get(
                'zip') if customer_obj.get('default_address') else None,
            phone=customer_obj.get('phone'),
            tags=customer_obj.get('tags'),
            note=customer_obj.get('note'),
            accepts_marketing=customer_obj.get('accepts_marketing'),
            tax_exempt=customer_obj.get('tax_exempt'),
        )

        return cusomer.__dict__

    def product_by_title(self, context, payload):
        '''get product by title '''

        access_token = context['headers']['access_token']
        url = f"admin/api/2021-07/products.json?title={payload['title']}"
        response = util.rest(
            'GET', url, context['headers']['domain'], access_token)
        product_data = json.loads(response.text)['products'][0]

        return self.mapping_of_product(product_data)

    def mapping_of_product(self, product):
        '''mappings of product for apis and triggers'''

        product_obj = ShopifyProduct(
            product_id=product['id'],
            title=product.get('title'),
            product_type=product.get('product_type'),
            vendor=product.get('vendor'),
            product_description=product.get('body_html'),
            tags=product.get('tags'),
            published_at=product.get('published_at'),
            price=product.get('variants')[0].get('price'),
            inventory_policy=product.get(
                'variants')[0].get('inventory_policy'),
            image_url=product.get('image').get('src') if product.get('image') else None,
            sku=product.get('variants')[0].get('sku'),
            is_published=product.get('status'),
            compare_at_price=product.get('variants')[0].get('compare_at_price')
        )
        
        return product_obj.__dict__
    
    def profile(self, context, params):
        access_token = context['headers']['access_token']
        url = f"admin/api/2021-07/users/current.json"
        response_data = util.rest(
            'GET', url, context['headers']['domain'], access_token)
        response = response_data.json()['user']
        profile = {
            'id':response['id'],
            'email':response['email'],
            'name':response['fullName']
        }
        return profile