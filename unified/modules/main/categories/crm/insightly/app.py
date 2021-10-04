# InsightlyApp - extends App, InsightlyTriggers, InsightlyActions, InsightlyAPI, ..

# from . import module

import json

from crm.insightly.actions import InsightlyActions
from crm.insightly.api import InsightlyApi
from crm.insightly.triggers import InsightlyTriggers

from unified.core.app import App, AuthInfo


class InsightlyApp(App, InsightlyActions, InsightlyApi, InsightlyTriggers):

    def __init__(self):
        super().__init__(
        name = "Insightly",
        description = "Insightly is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
        category = "CRM",
        logo = "https://logo.500apps.com/insightly",
        auth_type = "basic",
        auth_info = None
)
