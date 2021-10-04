import json

from crm.freshworks.actions import FreshworksActions
from crm.freshworks.api import FreshworksApi
from crm.freshworks.triggers import FreshworksTriggers

from unified.core.app import App, AuthInfo


class FreshworksApp(App, FreshworksActions, FreshworksApi, FreshworksTriggers):

    def __init__(self):
        super().__init__(
            name="Freshworkscrm",
            description="Freshsales is CRM with built-in phone and email. You can manage leads and deals, track customer activities on website, and customize reports for better insights.",
            category="CRM",
            logo="https://logo.500apps.com/freshworkscrm",
            auth_info=None,
            auth_type='oauth2')
