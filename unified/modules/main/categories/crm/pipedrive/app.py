# from . import module
import json

from crm.pipedrive.actions import PipedriveActions
from crm.pipedrive.api import PipedriveAPI
from crm.pipedrive.triggers import PipedriveTriggers
from unified.core.app import App, AuthInfo


class PipedriveApp(App, PipedriveActions, PipedriveTriggers, PipedriveAPI):

    def __init__(self):
        super().__init__(
            name="Pipdrivecrm",
            description="Pipedrive CRM offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category="CRM",
            logo="https://logo.500apps.com/Pipedrive",
            auth_info=None,
            auth_type='oauth2')
