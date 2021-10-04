# from . import module
import json
from unified.core.app import App, AuthInfo
from marketing_automation.hubspot.api import HubspotApi
from marketing_automation.hubspot.actions import HubspotActions
from marketing_automation.hubspot.triggers import HubspotTriggers
class HubspotApp(App, HubspotActions, HubspotApi, HubspotTriggers):
    def __init__(self):
        super().__init__(
            name="Hubspot",
            description="HubSpot platform has all the tools and integrations you need for marketing, sales, content management, and customer service. Each product in the platform is powerful alone, but the real magic happens when you use them together.",
            category="Marketing Automation",
            logo="https://logo.500apps.com/hubspot",
            auth_info=None,
            auth_type='basic')
