import asana
import json
from task_management.googletasks.actions import GoogletasksActions
from task_management.googletasks.api import GoogletasksApi
from unified.core.app import App, AuthInfo


class GoogletasksApp(App, GoogletasksActions, GoogletasksApi):

    def __init__(self):
        super().__init__(
        name = "GoogleTasks",
        description = "Google Tasks lets you create a to-do list within your desktop Gmail or the Google Tasks app.",
        category = "Task Management",
        logo = "https://logo.500apps.com/googletasks",
        auth_info = None,
        auth_type = 'oauth2')