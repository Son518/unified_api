# from . import module
import json

from forms_surveys.surveymonkey.actions import SurveymonkeyActions
from forms_surveys.surveymonkey.api import SurveymonkeyAPI

from unified.core.app import App, AuthInfo


class SurveymonkeyApp(App, SurveymonkeyActions, SurveymonkeyAPI):

    def __init__(self):

        super().__init__(
            name="Survey Monkey",
            description="SurveyMonkey is the world's leading People Powered Data platform enabling curious individuals and companies",
            category = "Forms Surveys",
            logo="https://logo.500apps.com/surveymonkey",
            auth_info=None,
            auth_type='oauth2'
        )