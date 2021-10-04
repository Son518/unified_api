from unified.core.app import App
from crm.salesforce.actions import SalesforceActions
from crm.salesforce.api import SalesforceApi
from crm.salesforce.triggers import SalesforceTriggers


class SalesforceApp(App, SalesforceActions, SalesforceApi, SalesforceTriggers):

    def __init__(self):
        super().__init__(
            name="Salesforce CRM",
            description="powerful CRM technology for nonprofits, educational institutions, and philanthropic organizations to amplify your social impact.",
            category="CRM",
            logo="https://logo.500apps.com/salesforce",
            auth_info=None,
            auth_type="oauth2")
