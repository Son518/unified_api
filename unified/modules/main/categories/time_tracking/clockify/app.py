import json
from time_tracking.clockify.actions import ClockifyActions
from time_tracking.clockify.triggers import ClockifyTriggers
from time_tracking.clockify.api import ClockifyApi
from unified.core.app import App, AuthInfo

class ClockifyApp(App,ClockifyActions,ClockifyTriggers,ClockifyApi):

    def __init__(self):
        super().__init__(
            name="Clockify",
            description="Clockify is a time tracker and timesheet app that lets you track work hours across projects.",
            category="time_tracking",
            logo="https://logo.500apps.com/clockify",
            auth_info=None,
            auth_type='basic')