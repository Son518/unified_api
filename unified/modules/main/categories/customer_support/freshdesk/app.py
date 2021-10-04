# from . import module
import json
from customer_support.freshdesk.actions import FreshdeskActions
from customer_support.freshdesk.api import FreshdeskApi
from customer_support.freshdesk.triggers import FreshdeskTriggers
from unified.core.app import App, AuthInfo


class FreshdeskApp(App, FreshdeskActions, FreshdeskApi, FreshdeskTriggers):

    def __init__(self):
        super().__init__(
            name="Freshdesk",
            description="Freshdesk is an online, cloud-based IT Helpdesk which is ITIL ready.",
            category="Customer Support",
            logo="https://logo.500apps.com/freshdesk",
            auth_info=None,
            auth_type='basic')
