from unified.core.app import App, AuthInfo
from crm.copper_crm.actions import CoppercrmAction
from crm.copper_crm.triggers import CoppercrmTriggers
from crm.copper_crm.api import CoppercrmApi
from crm.copper_crm.search import CoppercrmSearch


class CoppercrmApp(App, CoppercrmAction, CoppercrmApi, CoppercrmTriggers, CoppercrmSearch):
    def __init__(self):
        super().__init__(
            name="Copper CRM",
            description="Copper CRM is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category="CRM",
            logo="https://logo.500apps.com/copper",
            auth_info=None,
            auth_type='basic')
