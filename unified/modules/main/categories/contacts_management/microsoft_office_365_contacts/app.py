from unified.core.app import App
from contacts_management.microsoft_office_365_contacts.api import Microsoftoffice365contactsApi

class Microsoftoffice365contactsApp(App, Microsoftoffice365contactsApi):
    def __init__(self):
        super().__init__(
            name="Microsoft office 365 Contacts",
            description="Windows Contacts is a contact manager that is included in Windows Vista, Windows 7, Windows 8, and Windows 10. It replaced but retains most of the functionality of Windows Address Book and worked with Windows Live Mail and the Vista version of Windows Mail. Windows Contacts uses an XML-based schema format",
            category="CRM",
            logo="https://logo.500apps.com/Microsoft-office-365-Contacts",
            auth_info=None,
            auth_type="oauth2")
