from unified.core.app import App
from project_management.paymo.actions import PaymoActions
from project_management.paymo.triggers import PaymoTriggers
from project_management.paymo.api import PaymoApi

class PaymoApp(App,PaymoActions,PaymoTriggers,PaymoApi):
    def __init__(self):
        super().__init__(
            name="paymo",
            description="A fully featured platform that allows your team to take control of their work, time, and finances.",
            category="Project management",
            logo="https://logo.500apps.com/paymo",
            auth_info=None,
            auth_type='basic')