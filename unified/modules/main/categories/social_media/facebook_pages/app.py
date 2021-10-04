from unified.core.app import App, AuthInfo
from social_media.facebook_pages.api import FacebookpageAPI
from social_media.facebook_pages.actions import FacebookpagesAction

class FacebookpagesApp(App, FacebookpagesAction, FacebookpageAPI):
    def __init__(self):
        super().__init__(
            name="Facebook Pages",
            description="Facebook is a social networking site that makes it easy for you to connect and share with family and friends online.",
            category="Social media",
            logo="https://logo.500apps.com/facebookpages",
            auth_info=None,
            auth_type='oauth2')
