import json
from phone_sms.twilio.actions import TwilioActions
from phone_sms.twilio.api import TwilioApi
from phone_sms.twilio.triggers import TwilioTriggers
from unified.core.app import App, AuthInfo


class TwilioApp(App,TwilioActions,TwilioApi,TwilioTriggers):

    def __init__(self):
        super().__init__(
            name="Twilio",
            description="Twilio provides a simple entry point into the telephony world, and helps your business avoid many of the traditional complexities.",
            category="phone_sms",
            logo="https://logo.500apps.com/twilio",
            auth_info=None,
            auth_type='basic')
