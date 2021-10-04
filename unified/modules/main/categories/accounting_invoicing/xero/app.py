# from . import module
import json
from accounting_invoicing.xero.actions import XeroActions
from accounting_invoicing.xero.api import XeroApi
from unified.core.app import App, AuthInfo


class XeroApp(App, XeroActions, XeroApi):

    def __init__(self):
        super().__init__(
            name="Xero",
            description="Xero offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category="Accounting Invoicing",
            logo="https://logo.500apps.com/xero",
            auth_info=None,
            auth_type='oauth2')
