
from unified.core.app import App, AuthInfo
from email_newsletters.mailjet.actions import MailjetActions
#from email_newsletters.mailjet.triggers import MailjetTriggers
from email_newsletters.mailjet.api import MailjetApi


class MailjetApp(App, MailjetActions,MailjetApi):

    def __init__(self):
        super().__init__(
            name="Mailjet",
            description="Mailjet is an all-in-one solution to send, track and deliver transactional, notification and marketing emails. Engage, analyze and react with your client base through email. Get started by using the Mailjet zap to synchronise contacts from your favorite eCommerce, CRM or other SaaS tools to your Mailjet contact lists. For users on API version 3 or higher.",
            category="Email Newsletters",
            logo="https://logo.500apps.com/mailjet",
            auth_info=None,
            auth_type='oauth2')
