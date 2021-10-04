# KeapMaxClassicApp - extends App, KeapMaxClassicTriggers, KeapMaxClassicActions, KeapMaxClassicAPI, ..

# from . import module

import json

from marketing_automation.keap_max_classic.actions import KeapMaxClassicActions
from marketing_automation.keap_max_classic.api import KeapMaxClassicApi

from unified.core.app import App, AuthInfo


class KeapmaxclassicApp(App, KeapMaxClassicActions, KeapMaxClassicApi):

    def __init__(self):
        super().__init__(
        name = "KeapMaxClassic",
        description = "KeapMaxClassic is a Sales and Marketing Automation built to help you grow without chaos",
        category = "Marketing Organisation",
        logo = "https://logo.500apps.com/keap_max_classic",
        auth_type = "oauth2",
        auth_info = None)
