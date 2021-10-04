import json

from project_management.teamwork.actions import TeamworkActions
from project_management.teamwork.api import TeamworkApi
from project_management.teamwork.triggers import TeamworkTriggers

from unified.core.app import App, AuthInfo


class TeamworkApp(App, TeamworkActions, TeamworkApi, TeamworkTriggers):

    def __init__(self):
        super().__init__(
            name="Teamwork",
            description="Teamwork is an easy-to-use online teamwork & project management software application that helps managers, staff and clients work together more productively online",
            category="Project management",
            logo="https://logo.500apps.com/teamwork",
            auth_info=AuthInfo(
                api_key="twp_Yf83dPP5SybjAiPrpSmeqsv3XC7x",
                domain="mantra5",
                client_id="1198740404539678",
                client_secret="bd9acdf6a05a4049bd46e6fdf557d0c4",
                token="1/1198849786214579:131d44492abb2c281b565e72586b91ec",
                refresh_url="https://app.asana.com/-/oauth_token"
            ),
            auth_type='basic')
