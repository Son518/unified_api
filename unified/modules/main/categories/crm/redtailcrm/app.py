import json

from crm.redtailcrm.actions import RedtailcrmActions
#from project_management.asana.api import AsanaApi
#from project_management.asana.triggers import AsanaTriggers

from unified.core.app import App, AuthInfo


class RedtailcrmApp(App, RedtailcrmActions):

    def __init__(self):
        super().__init__(
            name="Redtailcrm",
            description="Redtailcrm cost-effective, feature-rich, customizable, and highly automated, redtail CRM assists you in every aspect of your client relationships.",
            category="CRM",
            logo="https://logo.500apps.com/asana",
            auth_info=None,
            auth_type='oauth2')
