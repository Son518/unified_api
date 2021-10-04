import json
from task_management.any_do.actions import AnydoActions
from unified.core.app import App, AuthInfo


class AnydoApp(App,AnydoActions):

    def __init__(self):
        super().__init__(
            name="Any_do",
            description="Any.do is a web-based to-do list app and task management tool, with data sync across additional applications for iOS and Android phones and tablets, web browsers, and Mac OS X.",
            category="task_management",
            logo="https://logo.500apps.com/any_do",
            auth_info=None,
            auth_type='basic')