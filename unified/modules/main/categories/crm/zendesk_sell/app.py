import json

from crm.zendesk_sell.actions import ZendesksellActions
from crm.zendesk_sell.api import ZendesksellApi

from unified.core.app import App, AuthInfo


class ZendesksellApp(App, ZendesksellActions  ,ZendesksellApi):

    def __init__(self):
        super().__init__(
            name="Zendesksellcrm",
            description="zendesksell is an easy-to-use online teamwork & project management software application that helps managers, staff and clients work together more productively online",
            category="CRM",
            logo="https://logo.500apps.com/zendesk",
            auth_info=None,
            auth_type='basic')
