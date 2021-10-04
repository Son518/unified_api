# TogglApp - extends App, TogglTriggers, TogglActions, TogglAPI, ..

# from . import module

import json

from time_tracking.toggl.actions import TogglActions
from time_tracking.toggl.api import TogglApi

from unified.core.app import App, AuthInfo


class TogglApp(App, TogglActions, TogglApi):

    def __init__(self):
        super().__init__(
        name = "Toggl",
        description = "Toggl takes the stress out of time tracking, project-planning, and hiring.",
        category = "Time Tracking",
        logo = "https://logo.500apps.com/toggl",
        auth_type = "basic",
        auth_info = None
)
