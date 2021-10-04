# WrikeApp - extends App, WrikeTriggers, WrikeActions, WrikeAPI, ..

# from . import module
import json

from project_management.wrike.actions import WrikeActions
from project_management.wrike.api import WrikeApi
from project_management.wrike.triggers import WrikeTriggers

from unified.core.app import App, AuthInfo


class WrikeApp(App, WrikeActions, WrikeApi, WrikeTriggers):

    def __init__(self):
        super().__init__(
            name="Wrike",
            description="Wrike is a project management tool where you can plan and organize your projects, tasks, and folders. You can customize your dashboard, synchronize tasks and milestones with calendar, and be up to date with the live activity stream.",
            category="Project management",
            logo="https://logo.500apps.com/wrike",
            auth_info=None,
            auth_type='oauth2')
