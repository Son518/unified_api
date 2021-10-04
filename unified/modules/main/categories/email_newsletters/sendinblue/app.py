
from unified.core.app import App, AuthInfo
from email_newsletters.sendinblue.actions import SendinblueActions
from email_newsletters.sendinblue.triggers import SendinblueTriggers
from email_newsletters.sendinblue.api import SendinblueApi


class SendinblueApp(App, SendinblueActions,SendinblueApi,SendinblueTriggers):

    def __init__(self):
        super().__init__(
            name="Sendinblue",
            description="Sendinblue is a SaaS solution for relationship marketing.The company was founded in 2012 by Armand Thiberge and Kapil Sharma,and offers a cloud-based marketing communication software suite with email marketing,transactional email,marketing automation,customer-relationship management,landing pages,Facebook ads,retargeting ads,SMS marketing,and more.",
            category="Email Newsletters",
            logo="https://logo.500apps.com/sendinblue",
            auth_info=None,
            auth_type='oauth2')
