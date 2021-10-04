from unified.core.app import App
from teamchat.slack.actions import SlackActions
from teamchat.slack.api import SlackApi
from teamchat.slack.triggers import SlackTriggers


class SlackApp(App, SlackActions, SlackApi, SlackTriggers):

    def __init__(self):
        super().__init__(
            name = "Slack",
            description = "One platform for your team and your work",
            category = "teamchat",
            logo="https://logo.500apps.com/slack",
            auth_info=None,
            auth_type='bearer'
        )