import json

from email_newsletters.mailerlite.actions import MailerliteActions
from email_newsletters.mailerlite.triggers import MailerliteTriggers
from email_newsletters.mailerlite.api import MailerliteAPI

from unified.core.app import App, AuthInfo


class MailerliteApp(App, MailerliteActions, MailerliteAPI, MailerliteTriggers):

    def __init__(self):
        super().__init__(
            name="Mailerlite",
            description="Mailerlite is an easy-to-use online mailerlite & project management software application that helps managers, staff and clients work together more productively online",
            category="email_newsletters",
            logo="https://logo.500apps.com/mailerlite",
            auth_info=None,
            auth_type='basic')