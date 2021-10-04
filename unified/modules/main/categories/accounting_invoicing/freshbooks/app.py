import json
from accounting_invoicing.freshbooks.actions import FreshbooksActions
from accounting_invoicing.freshbooks.api import FreshbooksApi
from accounting_invoicing.freshbooks.triggers import FreshbooksTriggers
from unified.core.app import App, AuthInfo

class FreshbooksApp(App,FreshbooksActions,FreshbooksApi,FreshbooksTriggers):

    def __init__(self):
        super().__init__(
            name="Freshbooks",
            description="The best cloud based small business accounting software. Send invoices, track time, manage receipts, expenses, and accept credit cards.",
            category="accounting_invoicing",
            logo="https://logo.500apps.com/freshbooks",
            auth_info=None,
            auth_type='oauth2')
