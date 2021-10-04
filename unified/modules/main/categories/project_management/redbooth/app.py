import asana
import json
from project_management.redbooth.actions import RedboothActions
from project_management.redbooth.api import RedboothApi
from unified.core.app import App, AuthInfo


class RedboothApp(App, RedboothActions, RedboothApi):

    def __init__(self):
        super().__init__(
        name = "Redbooth",
        description = "Redbooth helps teams manage many tasks simultaneously with our flexible software. Stay on track with existing projects and start new ones instantly.",
        category = "Project Management",
        logo = "https://logo.500apps.com/redbooth",
        auth_info = None,
        auth_type = 'oauth2')