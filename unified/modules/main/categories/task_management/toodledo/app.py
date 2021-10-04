import json
from task_management.toodledo.actions import ToodledoActions
from unified.core.app import App, AuthInfo

class ToodledoApp(App,ToodledoActions):

    def __init__(self):
        super().__init__(
            name="Toodledo",
            description="Toodledo has the ability to connect to many popular services and devices to allow you to access your tasks from anywhere.",
            category="task_management",
            logo="https://logo.500apps.com/toodledo",
            auth_info=None,
            auth_type='oauth2')