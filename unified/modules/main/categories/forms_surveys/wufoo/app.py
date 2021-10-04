from unified.core.app import App
from forms_surveys.wufoo.actions import WufooActions
from forms_surveys.wufoo.api import WufooAPI


class WufooApp(App, WufooActions, WufooAPI):

    def __init__(self):
        super().__init__(
            name="WufooApp",
            description="Build beautiful, interactive forms — get more responses. No coding needed. Templates for quizzes, research, feedback, lead generation, and more.",
            category="Form & Surveys",
            logo="https://logo.500apps.com/wufoo",
            auth_info=None,
            auth_type='oauth2')