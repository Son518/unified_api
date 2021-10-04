from unified.core.app import App, AuthInfo
from social_media.twitter.actions import TwitterAction
from social_media.twitter.api import TwitterApi


class TwitterApp(App, TwitterAction, TwitterApi):
    def __init__(self):
        super().__init__(
            name="Twitter",
            description="Twitter is a social networking site that makes it easy for you to connect and share with family and friends online.",
            category="Social media",
            logo="https://logo.500apps.com/twitter",
            auth_info=None,
            auth_type='oauth2')
