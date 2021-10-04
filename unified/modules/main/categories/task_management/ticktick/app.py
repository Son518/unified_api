import json
from task_management.ticktick.actions import TicktickActions
from task_management.ticktick.api import TicktickApi
from unified.core.app import App, AuthInfo

class TicktickApp(App,TicktickActions,TicktickApi):

    def __init__(self):
        super().__init__(
            name="Ticktick",
            description="TickTick is a powerful to-do & task management app with seamless cloud synchronization across all your devices.",
            category="task_management",
            logo="https://logo.500apps.com/ticktick",
            auth_info=None,
            auth_type='oauth2')