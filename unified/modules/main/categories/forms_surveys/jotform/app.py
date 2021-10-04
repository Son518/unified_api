# from . import module
import json

from forms_surveys.jotform.actions import JotFormActions
from forms_surveys.jotform.api import JotFormAPI
from forms_surveys.jotform.triggers import JotFormTriggers

from unified.core.app import App, AuthInfo


class JotformApp(App, JotFormActions, JotFormAPI, JotFormTriggers):

    def __init__(self):

        super().__init__(
            name="JotForm",
            description="JotForm  offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category = "Forms Surveys",
            logo="https://logo.500apps.com/jotform",
            auth_info=None,
            auth_type='oauth2'
        )