from project_management.clickup.actions import ClickupActions
from project_management.clickup.triggers import ClickupTriggers
from project_management.clickup.api import ClickupApi
from unified.core.app import App, AuthInfo
import json

class ClickupApp(App, ClickupActions, ClickupApi, ClickupTriggers):

    def __init__(self):
        super().__init__(
            name = "Clickup",
            description = "clickup is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category = "Project management",
            logo = "https://logo.500apps.com/clickup",
            auth_info = None,
            auth_type = 'oauth2')
