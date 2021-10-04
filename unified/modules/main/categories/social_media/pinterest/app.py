import json
from social_media.pinterest.actions import PinterestActions
from unified.core.app import App, AuthInfo

class PinterestApp(App,PinterestActions):

    def __init__(self):
        super().__init__(
            name="Pinterest",
            description="Pinterest is a visual discovery engine for finding ideas like recipes, home and style inspiration, and more. With billions of Pins on Pinterest, you'll always find ideas to spark inspiration.",
            category="social_media",
            logo="https://logo.500apps.com/Pinterest",
            auth_info=None,
            auth_type='oauth2')