import json
from project_management.runrunit.actions import RunrunitActions
from project_management.runrunit.api import RunrunitApi
from unified.core.app import App, AuthInfo


class RunrunitApp(App, RunrunitActions, RunrunitApi):

    def __init__(self):
        super().__init__(
            name="Runrunit",
            description="Runrunit is a task, time and performance management software for companies, which formalizes the existing workflow, keeps documents and decisions organized, and priorities clear. It increases your company's productivity by 25%, on average.",
            category="Project Management",
            logo="https://logo.500apps.com/runrunit",
            auth_info=None,
            auth_type='basic'
        )
