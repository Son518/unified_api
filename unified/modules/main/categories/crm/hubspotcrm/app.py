# from . import module
import json

#from crm.agilecrm.actions import HubspotcrmActions
from crm.hubspotcrm.api import HubspotcrmApi
#from crm.hubspot.triggers import HubspotcrmTriggers

from unified.core.app import App, AuthInfo


class HubspotcrmApp(App, HubspotcrmApi):

    def __init__(self):
        super().__init__(
            name="Hubspotcrm",
            description="HubSpot is your all-in-one stop for all of your marketing software needs.",
            category="CRM",
            logo="https://logo.500apps.com/Hubspotcrm",
            auth_info=None,
            auth_type='basic')
