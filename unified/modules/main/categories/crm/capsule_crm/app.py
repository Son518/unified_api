from unified.core.app import App
from crm.capsule_crm.actions import CapsulecrmActions
from crm.capsule_crm.triggers import CapsulecrmTriggers
from crm.capsule_crm.api import CapsulecrmApi


class CapsulecrmApp(App, CapsulecrmActions, CapsulecrmTriggers, CapsulecrmApi):
    def __init__(self):
        super().__init__(
            name="Capsule CRM",
            description="Capsule CRM offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category="CRM",
            logo="https://logo.500apps.com/CapsuleCRM",
            auth_info=None,
            auth_type='oauth2')
