from unified.core.app import App
from social_media.linkedin.actions import LinkedinActions

class LinkedinApp(App, LinkedinActions):

    def __init__(self):
        super().__init__(
            name="Linkedin",
            description="LinkedIn is an American business and employment-oriented online service that operates via websites and mobile apps.",
            category="social_media",
            logo="https://logo.500apps.com/linkedin",
            auth_info=None,
            auth_type='oauth2')
