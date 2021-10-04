
from unified.core.app import App, AuthInfo
from project_management.basecamp3.actions import Basecamp3Actions
from project_management.basecamp3.triggers import Basecamp3Triggers
from project_management.basecamp3.api import Basecamp3Api


class Basecamp3App(App, Basecamp3Actions, Basecamp3Triggers, Basecamp3Api):

    def __init__(self):
        super().__init__(
            name = "Basecamp 3",
            description = "Basecamp’s unique blend of tools is everything any team needs to stay on the same page about whatever they’re working on.",
            category = "Project management",
            logo = "https://logo.500apps.com/basecamp3",
            auth_info = None,
            auth_type = 'oauth2')
