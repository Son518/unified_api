from unified.core.app import App
from forms_surveys.typeform.actions import TypeformActions
from forms_surveys.typeform.triggers import TypeformTriggers
from forms_surveys.typeform.api import TypeformApi


class TypeformApp(App, TypeformActions, TypeformTriggers, TypeformApi):

    def __init__(self):
        super().__init__(
            name="Basecamp 3",
            description="Build beautiful, interactive forms — get more responses. No coding needed. Templates for quizzes, research, feedback, lead generation, and more.",
            category="Form & Surveys",
            logo="https://logo.500apps.com/typeform",
            auth_info=None,
            auth_type='oauth2')
