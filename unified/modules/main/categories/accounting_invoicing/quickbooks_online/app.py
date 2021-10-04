from unified.core.app import App, AuthInfo
from accounting_invoicing.quickbooks_online.actions import QuickbooksonlineActions
from accounting_invoicing.quickbooks_online.triggers import QuickbooksonlineTriggers
from accounting_invoicing.quickbooks_online.api import QuickbooksonlineApi


class QuickbooksonlineApp(App, AuthInfo, QuickbooksonlineTriggers, QuickbooksonlineActions, QuickbooksonlineApi):

    def __init__(self):
        super().__init__(
            name="Quickbooks Online",
            description="QuickBooks Online is the web version of the popular accounting packages QuickBooks",
            category="Accounting Invoicing",
            logo="https://logo.500apps.com/quickbooksonline",
            auth_info=None,
            auth_type='oauth2')
