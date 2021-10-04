from unified.core.app import App, AuthInfo
from documents.google_docs.actions import GoogledocsAction
from documents.google_docs.api import GoogledocsApi

class GoogledocsApp(App, GoogledocsAction, GoogledocsApi):
    def __init__(self):
        super().__init__(
            name="Google Docs",
            description="Google Docs is an online word processor included as part of the free, web-based Google Docs Editors suite offered by Google which also includes Google Sheets, Google Slides, Google Drawings, Google Forms, Google Sites, and Google Keep",
            category="documents",
            logo="https://logo.500apps.com/google-docs",
            auth_info=None,
            auth_type='oauth2')
