import json
from crm.nimble.actions import NimbleActions
from unified.core.app import App, AuthInfo

class NimbleApp(App,NimbleActions):

    def __init__(self):
        super().__init__(
            name="Nimble",
            description="Nimble is a social relationship management tool that brings together your contacts from many disparate locations into one place.",
            category="crm",
            logo="https://logo.500apps.com/Nimble",
            auth_info=None,
            auth_type='basic')