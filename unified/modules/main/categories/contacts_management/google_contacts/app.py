from unified.core.app import App
from contacts_management.google_contacts.api import GoogleContactsApi

class GooglecontactsApp(App, GoogleContactsApi):
    def __init__(self):
        super().__init__(
            name="Google contacts",
            description="Google Contacts is Google's contact management tool that is available in its free email service Gmail, as a standalone service, and as a part of Google's business-oriented suite of web apps Google Workspace",
            category="CRM",
            logo="https://logo.500apps.com/google-contact",
            auth_info=None,
            auth_type="oauth2")
