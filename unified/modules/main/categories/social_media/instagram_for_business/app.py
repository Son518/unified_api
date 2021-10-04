from unified.core.app import App, AuthInfo
from social_media.instagram_for_business.api import InstagramforbusinessApi
from social_media.instagram_for_business.action import InstagramforbusinessAction

class InstagramforbusinessApp(App, InstagramforbusinessApi, InstagramforbusinessAction):
    def __init__(self):
        super().__init__(
            name="Instagram for Business",
            description="Instagram for Business is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category="Project management",
            logo="https://logo.500apps.com/instagram-for-business",
            auth_info=None,
            auth_type='oauth2')
