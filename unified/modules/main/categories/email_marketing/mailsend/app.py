from unified.core.app import App
from email_marketing.mailsend.triggers import MailsendTriggers


class MailsendApp(App, MailsendTriggers):

    def __init__(self):
        super().__init__(
            name="Mailsend",
            description="Connect with your audience like never before by creating & sending state of the art newsletters, and managing drip campaigns from one central location.",
            category="Infinity",
            logo="https://logo.500apps.com/mailsend",
            auth_info=None,
            auth_type='Basic')
