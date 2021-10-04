from unified.core.app import App, AuthInfo
from dev_tools.github.actions import GithubActions
from dev_tools.github.api import GithubAPI
from dev_tools.github.triggers import GithubTriggers


class GithubApp(App, GithubActions, GithubAPI, GithubTriggers):
    def __init__(self):
        super().__init__(
            name = "Github",
            description = "Software development and version control using Git. It offers the distributed version control and source code management functionality of Git, plus its own features",
            category = "Dev Tools",
            logo = "https://logo.500apps.com/github",
            auth_info = None,
            auth_type = 'oauth2')
