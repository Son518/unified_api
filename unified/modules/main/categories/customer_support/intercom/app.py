# from . import module
import json
from customer_support.intercom.actions import IntercomActions
from customer_support.intercom.api import IntercomApi
from customer_support.intercom.triggers import IntercomTriggers
from unified.core.app import App, AuthInfo


class IntercomApp(App, IntercomActions, IntercomApi, IntercomTriggers):

    def __init__(self):
        super().__init__(
            name="Intercom",
            description="Intercom is a customer communication platform that enables targeted communication with customers on your website, inside your web and mobile apps, and by email.",
            category="Customer Support",
            logo="https://logo.500apps.com/Intercom",
            auth_info=None,
            auth_type='oauth2')
