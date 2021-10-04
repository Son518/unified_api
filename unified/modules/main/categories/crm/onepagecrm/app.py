import json

from crm.onepagecrm.actions import OnepagecrmActions
from crm.onepagecrm.api import OnepagecrmApi
from crm.onepagecrm.triggers import OnepagecrmTriggers

from unified.core.app import App, AuthInfo


class OnepagecrmApp(App, OnepagecrmActions,OnepagecrmApi,OnepagecrmTriggers):

    def __init__(self):
        super().__init__(
            name="Onepagecrm",
            description="OnePageCRM converts the complexity of CRM into a simple to-do list. Built using GTD (Getting Things Done) productivity principles, its streamlined approach to sales helps you convert leads to customers, reach targets and grow your business fast. By focusing on that one Next Action, your sales team are organized and empowered to move a deal forward. OnePageCRM strives to offer a product that is as easy to use as email and helps your company achieve zero admin.",
            category="CRM",
            logo="https://logo.500apps.com/onepagecrm",
            auth_info=None,
            auth_type='basic')
