# AsanaApp - extends App, AsanaTriggers, AsanaActions, AsanaAPI, ..

# from . import module
import json

from project_management.trello.actions import TrelloActions
from project_management.trello.triggers import TrelloTriggers
from project_management.trello.api import TrelloApi
from unified.core.app import App, AuthInfo


class TrelloApp(App, TrelloActions, TrelloTriggers, TrelloApi):

    def __init__(self):
        super().__init__(
            name="Trello",
            description="Trello is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category="Project management",
            logo="https://logo.500apps.com/Trello",
            auth_info=AuthInfo(
                client_id="",
                client_secret="",
                token="",
                refresh_url="",
                api_key="",
                domain=""
            ),
            auth_type='oauth1')
