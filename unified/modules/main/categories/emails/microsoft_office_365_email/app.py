from unified.core.app import App, AuthInfo
from emails.microsoft_office_365_email.actions import Microsoftoffice365emailActions
from emails.microsoft_office_365_email.api import Microsoftoffice365emailApi


class Microsoftoffice365emailApp(App, Microsoftoffice365emailActions, Microsoftoffice365emailApi):

    def __init__(self):
        super().__init__(
            name = "Microsoft Office 365 Email",
            description = "Microsoft Office 365 Email is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category = "Project management",
            logo = "https://logo.500apps.com/Microsoft-Office-365-Email",
            auth_info = None,
            auth_type = 'oauth2'
        )
