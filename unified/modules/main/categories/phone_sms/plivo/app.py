
import json
from phone_sms.plivo.actions import PlivoActions
from unified.core.app import App, AuthInfo


class PlivoApp(App, PlivoActions):
    def __init__(self):
        super().__init__(
            name="Plivo",
            description="Plivo's SMS API and Voice API platform enables businesses to communicate with their customers on a global scale.",
            category="phone_sms",
            logo="https://logo.500apps.com/plivo",
            auth_info=None,
            auth_type='basic')
