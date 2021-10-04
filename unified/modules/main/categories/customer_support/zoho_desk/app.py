from unified.core.app import App
from customer_support.zoho_desk.actions import ZohodeskActions
from customer_support.zoho_desk.api import ZohodeskApi
from customer_support.zoho_desk.triggers import ZohodeskTriggers


class ZohodeskApp(App, ZohodeskActions, ZohodeskApi, ZohodeskTriggers):

    def __init__(self):
        super().__init__(
            name="Zohodesk",
            description="Customer Service Software for Context-Aware Support",
            category="Customer Support",
            logo="https://logo.500apps.com/zoho_desk",
            auth_info=None,
            auth_type='oauth2'
        )