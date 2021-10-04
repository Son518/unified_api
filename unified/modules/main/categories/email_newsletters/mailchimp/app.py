from unified.core.app import App, AuthInfo
from email_newsletters.mailchimp.actions import MailchimpAction
from email_newsletters.mailchimp.triggers import MailchimpTrigger
from email_newsletters.mailchimp.api import MailchimpApi


class MailchimpApp(App, MailchimpAction, MailchimpTrigger, MailchimpApi):

    def __init__(self):
        super().__init__(
            name="Mailchimp",
            description="Mailchimp is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category="Project management",
            logo="https://logo.500apps.com/mailchimp",
            auth_info=None,
            auth_type='oauth2')
