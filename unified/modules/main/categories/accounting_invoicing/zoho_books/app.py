import json
from accounting_invoicing.zoho_books.actions import ZohobooksActions
from accounting_invoicing.zoho_books.api import ZohobooksApi
from accounting_invoicing.zoho_books.triggers import ZohobooksTriggers
from unified.core.app import App, AuthInfo


class ZohobooksApp(App,ZohobooksActions,ZohobooksApi,ZohobooksTriggers):

    def __init__(self):
        super().__init__(
            name="Zohobooks",
            description="Zoho Books is online accounting software that manages your finances, automates business workflows",
            category="accounting_invoicing",
            logo="https://logo.500apps.com/zohobooks",
            auth_info=None,
            auth_type='oauth2')
