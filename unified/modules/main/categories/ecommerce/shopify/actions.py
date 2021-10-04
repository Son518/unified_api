from ecommerce.shopify import util
from unified.core.actions import Actions
from ecommerce.shopify.entities.shopify_blog import ShopifyBlog
from ecommerce.shopify.entities.shopify_order import ShopifyOrder
from ecommerce.shopify.entities.shopify_product import ShopifyProduct
from ecommerce.shopify.entities.shopify_customer import ShopifyCustomer
from ecommerce.shopify.entities.shopify_inventory import ShopifyInventory

class ShopifyAction(Actions):
    def create_customer(self, context, payload):
        '''Creates a new customer.'''

        access_token = context['headers']['access_token']
        url = 'admin/api/2021-07/customers.json'
        customer = ShopifyCustomer(**payload)
        request_body = self.get_customer_payload(customer)
        response = util.rest(
            'POST', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code

    def get_customer_payload(self,customer):

        request_body = {
            "customer": {
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "email": customer.email_address,
                "phone": customer.phone,
                "tags": customer.tags,
                "note": customer.note,
                "tax_exempt": (customer.tax_exempt == 'true'),
                "send_email_invite": (customer.send_email_invite == 'true'),
                "accepts_marketing": (customer.accepts_marketing == 'true'),
                "addresses": [
                    {
                        "company": customer.company_name,
                        "street_address": customer.street_address,
                        "city": customer.street_address_line2,
                        "province": customer.state,
                        "zip": customer.zip_code,
                        "country": customer.country
                    }
                ]
            }
        }

        return request_body

    def update_customer(self, context, payload):
        """Updates an existing customer"""

        access_token = context['headers']['access_token']
        customer = ShopifyCustomer(**payload)
        url = f'admin/api/2021-07/customers/{customer.customer_id}.json'
        request_body = self.get_customer_payload(customer)
        response = util.rest(
            'PUT', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code

    def create_product(self, context, payload):
        '''Creates a new product.'''

        access_token = context['headers']['access_token']
        product = ShopifyProduct(**payload)
        request_body = self.get_product_payload(product)
        url = "admin/api/2021-07/products.json"
        response = util.rest(
            'POST', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code
    
    def get_product_payload(self,product):
        request_body = {
            "product": {
                "title": product.title,
                "body_html": product.product_description,
                "vendor": product.vendor,
                "product_type": product.product_type,
                "tags": product.tags,
                "status": "active" if product.is_published == 'true' else "draft",
                "published_at": product.published_at,
                "variants": [
                    {
                        "price": int(product.price) if product.price else None,
                        "sku": product.sku,
                    }
                ]
            }
        }
        if product.image_url:
            request_body["images"]: [{"src": product.image_url}]
        if product.inventory_policy:
            request_body["product"]['variants'][0]["inventory_policy"] = product.inventory_policy
        
        return request_body

    def update_product(self, context, payload):
        '''Updates an existing product'''

        access_token = context['headers']['access_token']
        product = ShopifyProduct(**payload)
        url = f"admin/api/2021-07/products/{product.product_id}.json"
        request_body = self.get_product_payload(product)
        response = util.rest(
            'PUT', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code

    def create_product_variant(self, context, payload):
        '''creates a specific product .'''

        access_token = context['headers']['access_token']
        product_varient = ShopifyProduct(**payload)
        url = f"/admin/api/2021-07/products/{product_varient.product_id}/variants.json"
        request_body = self.get_product_variant_payload(product_varient)
        response = util.rest(
            'POST', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code

    def update_product_variant(self, context, payload):
        '''Updates an existing product variant. Replaces only data that is set.'''

        access_token = context['headers']['access_token']
        product_varient = ShopifyProduct(**payload)
        url = f"/admin/api/2021-07/variants/{product_varient.product_variant_id}.json"
        request_body = self.get_product_variant_payload(product_varient)
        response = util.rest(
            'PUT', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code
    
    def get_product_variant_payload(self,product_varient):
        request_body = {
            "variant": {
                "option1": product_varient.title,
                "price": product_varient.price,
                "sku": product_varient.sku,
                "compare_at_price": product_varient.compare_at_price,
                "inventory_policy": product_varient.inventory_policy
            }
        }
        return request_body

    def create_blog_entry(self, context, payload):
        '''Creates a new blog post.'''

        access_token = context['headers']['access_token']
        blog = ShopifyBlog(**payload)
        url = f"/admin/api/2021-07/blogs/{blog.blog_id}/articles.json"
        request_body = {
            "article": {
                "title": blog.title,
                "author": blog.author_name,
                "tags": blog.tags,
                "body_html": blog.content,
                "summary_html": blog.summary,
                "image": {
                    "src": blog.featured_image_url
                }
            }
        }
        response = util.rest(
            'POST', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code

    def create_order(self, context, payload):
        '''Creates a new order'''

        access_token = context['headers']['access_token']
        order = ShopifyOrder(**payload)
        url = "admin/api/2021-07/orders.json"
        request_body = {
            "order": {
                "send_receipt":(order.send_receipt == "true"),
                "customer":{
                    "id":order.customer_id
                },
                "billing_address": {
                    "company":order.billing_address_company,
                    "first_name": order.billing_address_first_name,
                    "last_name": order.billing_address_last_name,
                    "address1": order.billing_address_address,
                    "phone": order.billing_address_phone,
                    "city": order.billing_address_city,
                    "province": order.billing_address_state,
                    "country": order.billing_address_country,
                    "zip": order.billing_address_postal
                },
                "shipping_address": {
                   	"company":order.shipping_address_company,
                    "first_name": order.shipping_address_first_name,
                    "last_name": order.shipping_address_last_name,
                    "address1": order.shipping_address_address,
                    "phone": order.shipping_address_phone,
                    "city": order.shipping_address_city,
                    "province": order.shipping_address_state,
                    "country": order.shipping_address_country,
                    "zip": order.shipping_address_postal
                },
                "tags": order.tags,
                "transactions": [{
                    "kind": "authorization",
                    "status": order.fulfillment_status,
                    "amount": order.total_price
                }],
                "note":order.note,
                "line_items": [{"variant_id": order.product_variant_id, "quantity": order.product_quantity}]
            }
        }
        response = util.rest(
            'POST', url, context['headers']['domain'], access_token, request_body)

        return response.text, response.status_code