import json
from task_management.microsoft_to_do.actions import MicrosofttodoActions
from task_management.microsoft_to_do.api import MicrosofttodoApi
from unified.core.app import App, AuthInfo

class MicrosofttodoApp(App,MicrosofttodoActions,MicrosofttodoApi):

    def __init__(self):
        super().__init__(
            name="Microsofttodo",
            description="Microsoft To Do is a task management app to help you stay organized and manage your day-to-day.",
            category="task_management",
            logo="https://logo.500apps.com/Microsofttodo",
            auth_info=None,
            auth_type='oauth2')