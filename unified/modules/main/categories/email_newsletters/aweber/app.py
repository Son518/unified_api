import json
from email_newsletters.aweber.actions import AweberActions
from email_newsletters.aweber.api import AweberApi

from unified.core.app import App, AuthInfo


class AweberApp(App, AweberActions, AweberApi):

    def __init__(self):
        super().__init__(
            name="Aweber",
            description="AWeber provides professional email marketing software and services. AWeber's easy signup forms and autoresponders make it easy for you to stay in touch with your customers.",
            category="Email Newsletter",
            logo="https://logo.500apps.com/aweber",
            auth_info=None,
            auth_type='basic')
