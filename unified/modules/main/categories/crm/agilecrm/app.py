# from . import module
import json

from crm.agilecrm.actions import AgilecrmActions
from crm.agilecrm.api import AgilecrmApi
from crm.agilecrm.triggers import AgilecrmTriggers

from unified.core.app import App, AuthInfo


class AgilecrmApp(App, AgilecrmActions, AgilecrmApi, AgilecrmTriggers):

    def __init__(self):
        super().__init__(
            name="Agilecrm",
            description="Agile CRM offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category="CRM",
            logo="https://logo.500apps.com/Agilecrm",
            auth_info=None,
            auth_type='oauth2')
