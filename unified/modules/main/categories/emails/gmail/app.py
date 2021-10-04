from unified.core.app import App
from emails.gmail.actions import GmailActions
from emails.gmail.apis import GmailApi
from emails.gmail.triggers import GmailTriggers

class GmailApp(App, GmailActions, GmailApi, GmailTriggers):

    def __init__(self):
        super().__init__(
            name="Gmail",
            description="Gmail is a free email service provided by Google.",
            category="Emails",
            logo="https://logo.500apps.com/Gmail",
            auth_info=None,
            auth_type='oauth2'
        )
