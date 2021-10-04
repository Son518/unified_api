from unified.core.app import App, AuthInfo
from ecommerce.shopify.api import ShopifyApi
from ecommerce.shopify.actions import ShopifyAction
from ecommerce.shopify.triggers import ShopifyTrigger

class ShopifyApp(App, ShopifyAction, ShopifyApi, ShopifyTrigger):
    def __init__(self):
        super().__init__(
            name="Shopify",
            description="Shopify Inc. is a Canadian multinational e-commerce company headquartered in Ottawa, Ontario. It is also the name of its proprietary e-commerce platform for online stores and retail point-of-sale systems",
            category="ecommerce",
            logo="https://logo.500apps.com/shopify",
            auth_info=None,
            auth_type='oauth2')
