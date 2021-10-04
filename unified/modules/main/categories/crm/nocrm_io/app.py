import json
from crm.nocrm_io.actions import NocrmioActions
from crm.nocrm_io.api import NocrmioApi
from crm.nocrm_io.triggers import NoCRMioTriggers
from unified.core.app import App, AuthInfo


class NocrmioApp(App, NocrmioActions, NocrmioApi, NoCRMioTriggers):

    def __init__(self):
        super().__init__(
            name="noCRM.io",
            description="noCRM.io helps you to track and close deals without wasting time filling out forms. Boost productivity and manage your sales cycle from end-to-end",
            category="CRM",
            logo="https://logo.500apps.com/nocrm.io",
            auth_info=None,
            auth_type='basic')
