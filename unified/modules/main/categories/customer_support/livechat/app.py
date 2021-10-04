import json
from customer_support.livechat.triggers import LivechatTriggers
from unified.core.app import App, AuthInfo

class LivechatApp(App,LivechatTriggers):

    def __init__(self):
        super().__init__(
            name="Livechat",
            description="Live chat is a form of customer messaging software that allows customers to speak directly with a company's representatives",
            category="customer_support",
            logo="https://logo.500apps.com/livechat",
            auth_info=None,
            auth_type='oauth2')