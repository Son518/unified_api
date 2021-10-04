import json
from unified.core.app import App, AuthInfo
from drip_emails.convertkit.actions import ConvertkitActions
from drip_emails.convertkit.api import CovertkitApi

class ConvertkitApp(App, ConvertkitActions, CovertkitApi):

    def __init__(self):
        super().__init__(
            name="Convertkit",
            description="Connect with your fans, foster your community, and earn a living online with the only marketing platform built for creators, by creators.",
            category="drip_emails",
            logo="https://logo.500apps.com/convertkit",
            auth_info=None,
            auth_type='basic')
