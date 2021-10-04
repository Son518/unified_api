# from . import module
import json
from marketing_automation.getresponse.actions import GetresponseActions
from marketing_automation.getresponse.api import GetResponseApi
from marketing_automation.getresponse.triggers import GetresponseTriggers
from unified.core.app import App, AuthInfo


class GetresponseApp(App, GetresponseActions, GetResponseApi, GetresponseTriggers):

    def __init__(self):
        super().__init__(
            name="Getresponse",
            description="Getresponse offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category="Marketing Automation",
            logo="https://logo.500apps.com/getresponse",
            auth_info=None,
            auth_type='oauth2')
