import json
from website_builders.webflow.actions import WebflowActions
from unified.core.app import App, AuthInfo

class WebflowApp(App,WebflowActions):

    def __init__(self):
        super().__init__(
            name="Webflow",
            description="Webflow is a SaaS application that allows designers to build responsive websites with browser-based visual editing software.",
            category="website_builders",
            logo="https://logo.500apps.com/webflow",
            auth_info=None,
            auth_type='oauth2')