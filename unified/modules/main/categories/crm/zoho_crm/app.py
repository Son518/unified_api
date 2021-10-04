from unified.core.app import App, AuthInfo
from crm.zoho_crm.actions import ZohocrmActions
from crm.zoho_crm.api import ZohocrmApi
from crm.zoho_crm.search import ZohocrmSearch
from crm.zoho_crm.triggers import ZohocrmTriggers


class ZohocrmApp(App, ZohocrmActions, ZohocrmApi, ZohocrmSearch, ZohocrmTriggers):
    def __init__(self):
        super().__init__(
            name = "Zoho CRM",
            description = "Zoho CRM is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category = "Project management",
            logo = "https://logo.500apps.com/Zoho CRM",
            auth_info = None,
            auth_type = 'oauth2')
