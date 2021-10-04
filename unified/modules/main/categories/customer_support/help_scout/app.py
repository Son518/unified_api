# from . import module
import json
from customer_support.help_scout.actions import HelpscoutActions
from customer_support.help_scout.api import HelpscoutApi
from customer_support.help_scout.triggers import HelpscoutTriggers
from unified.core.app import App, AuthInfo


class HelpscoutApp(App, HelpscoutActions, HelpscoutApi, HelpscoutTriggers):

    def __init__(self):
        super().__init__(
            name="Help Scout",
            description="Help Scout provides an email-based customer support platform, knowledge base tool, and an embeddable search/contact widget for customer service professionals.",
            category="Customer Support",
            logo="https://logo.500apps.com/Help Scout",
            auth_info=None,
            auth_type='oauth2')
