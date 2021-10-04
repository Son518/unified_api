from unified.core.app import App, AuthInfo
from social_media.medium.api import MediumAPI
from social_media.medium.actions import MediumAction

class MediumApp(App, MediumAction, MediumAPI):
    def __init__(self):
        super().__init__(
            name="Medium",
            description="Medium is a social networking site that makes it easy for you to connect and share with family and friends online.",
            category="Social media",
            logo="https://logo.500apps.com/medium",
            auth_info=None,
            auth_type='oauth2')
