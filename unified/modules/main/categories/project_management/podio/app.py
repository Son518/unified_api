# AsanaApp - extends App, AsanaTriggers, AsanaActions, AsanaAPI, ..

# from . import module
import json

from project_management.podio.actions import PodioActions
from project_management.podio.api import PodioApi
from project_management.podio.triggers import PodioTriggers

from unified.core.app import App, AuthInfo


class PodioApp(App,PodioActions,PodioApi,PodioTriggers):

    def __init__(self):
        super().__init__(
        name = "Podio",
        description = "Podio is a collaborative work platform that's perfect for managing projects, teams, and anything else in your business that needs flexible apps that work the way you do.",
        category = "Project management",
        logo = "https://logo.500apps.com/podio",
        auth_info = None,
        auth_type = 'oauth2')