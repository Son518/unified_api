from unified.core.app import App
# from crm.salesmate.actions import SalesforceActions
from crm.salesmate.api import SalesmateApi
# from crm.salesmate.triggers import SalesforceTriggers


class SalesmateApp(App, SalesmateApi):

    def __init__(self):
        super().__init__(
            name="Salesmate CRM",
            description="powerful CRM technology for nonprofits, educational institutions, and philanthropic organizations to amplify your social impact.",
            category="CRM",
            logo="https://logo.500apps.com/salesmate",
            auth_info=None,
            auth_type="oauth2")