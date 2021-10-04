import json
from crm.pipelinedeals.actions import PipelinedealsActions
from crm.pipelinedeals.api import PipelinedealsApi
from crm.pipelinedeals.triggers import PipelinedealsTriggers
from unified.core.app import App, AuthInfo

class PipelinedealsApp(App,PipelinedealsActions,PipelinedealsApi,PipelinedealsTriggers):

    def __init__(self):
        super().__init__(
            name="Pipelinedeals",
            description="PipelineDeals allows users to manage their contacts, qualify leads, and track leads and deals within a singular, cloud-based program.",
            category="CRM",
            logo="https://logo.500apps.com/pipelinedeals",
            auth_info=None,
            auth_type='Basic')