from unified.core.app import App
from crm.microsoftdynamics365crm.actions import Microsoftdynamics365crmActions
from crm.microsoftdynamics365crm.api import Microsoftdynamics365crmApi


class Microsoftdynamics365crmApp(App, Microsoftdynamics365crmActions, Microsoftdynamics365crmApi):

    def __init__(self):
        super().__init__(
            name="Microsoft Dynamics 365 CRM",
            description="Microsoft Dynamics CRM is a customer relationship management software package developed by Microsoft.",
            category="CRM",
            logo="https://logo.500apps.com/microsoftdynamics365crm",
            auth_info=None,
            auth_type="oauth2")
