# AsanaApp - extends App, AsanaTriggers, AsanaActions, AsanaAPI, ..

# from . import module
import asana
import json

from project_management.mondaydotcom.actions import MondaydotcomActions
from project_management.mondaydotcom.api import MondaydotcomAPI
from project_management.mondaydotcom.triggers import MondaydotcomTriggers


from unified.core.app import App, AuthInfo


class MondaydotcomApp(App, MondaydotcomActions, MondaydotcomAPI, MondaydotcomTriggers):

    def __init__(self):
        super().__init__(
            name="Monday.com",
            description="monday.com helps you move projects forward fast, letting everyone know what's been done on a task—and what needs finished right now.",
            category="Project management",
            logo="https://logo.500apps.com/monday.com",
            auth_info=None,
            auth_type='oauth2')