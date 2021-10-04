# from . import module
import json
from customer_support.zendesk.actions import ZendeskActions
from customer_support.zendesk.api import ZendeskApi
from customer_support.zendesk.triggers import ZendeskTriggers
from unified.core.app import App, AuthInfo


class ZendeskApp(App, ZendeskActions, ZendeskApi, ZendeskTriggers):

    def __init__(self):
        super().__init__(
            name="Zendesk",
            description="Zendesk makes better experiences for agents, admins, and customers. As employees, we encourage each other to grow and innovate. As a company, we roll up our sleeves to plant roots in the communities we call home. Our customer service and engagement platform is powerful and flexible, and scales to meet the needs of any business. Even yours.",
            category="CUSTOMER SUPPORT",
            logo="https://logo.500apps.com/Zendesk",
            auth_info=None,
            auth_type='basic')
