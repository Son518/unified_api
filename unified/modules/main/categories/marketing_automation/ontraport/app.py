import json

from marketing_automation.ontraport.actions import OntraportActions
from marketing_automation.ontraport.triggers import OntraportTriggers
from marketing_automation.ontraport.api import OntraportApi

from unified.core.app import App, AuthInfo


class OntraportApp(App, OntraportActions, OntraportApi, OntraportTriggers):

    def __init__(self):
        super().__init__(
            name="Ontraport",
            description="Ontraport is an easy-to-use online Ontraport & project management software application that helps managers, staff and clients work together more productively online",
            category="marketing_automation",
            logo="https://logo.500apps.com/ontraport",
            auth_info=None,
            auth_type='basic')
