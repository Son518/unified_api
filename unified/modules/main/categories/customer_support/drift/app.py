import json
from customer_support.drift.actions import DriftActions
from customer_support.drift.api import DriftApi
from customer_support.drift.triggers import DriftTriggers
from unified.core.app import App, AuthInfo

class DriftApp(App,DriftActions,DriftApi,DriftTriggers):

    def __init__(self):
        super().__init__(
            name="Drift",
            description="Drift is a messaging app that allows you to talk to your website visitors and customers in real-time,from anywhere.",
            category="customer_support",
            logo="https://logo.500apps.com/drift",
            auth_info=None,
            auth_type='oauth2')
