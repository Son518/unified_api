import json
from infinity.todoist.actions import TodoistActions
from infinity.todoist.triggers import TodoistTriggers
from unified.core.app import App, AuthInfo

class TodoistApp(App,TodoistActions,TodoistTriggers):

    def __init__(self):
        super().__init__(
            name="Todoist",
            description="Todoist is a task management application that helps to manage your personal and professional productivity.",
            category="infinity",
            logo="https://logo.500apps.com/todoist",
            auth_info=None,
            auth_type='basic')