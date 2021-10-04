# AsanaApp - extends App, AsanaTriggers, AsanaActions, AsanaAPI, ..

# from . import module
import asana
import json

from project_management.asana.actions import AsanaActions
from project_management.asana.api import AsanaApi
from project_management.asana.triggers import AsanaTriggers

from unified.core.app import App, AuthInfo


class AsanaApp(App, AsanaActions, AsanaApi, AsanaTriggers):

    def __init__(self):
        super().__init__(
        name = "Asana",
        description = "Asana is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
        category = "Project management",
        logo = "https://logo.500apps.com/asana",
        auth_info = None,
        auth_type = 'oauth2')
