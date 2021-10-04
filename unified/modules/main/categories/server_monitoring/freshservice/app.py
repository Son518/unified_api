from unified.core.app import App
from server_monitoring.freshservice.actions import FreshserviceActions
from server_monitoring.freshservice.api import FreshserviceApi
from server_monitoring.freshservice.triggers import FreshserviceTriggers


class FreshserviceApp(App, FreshserviceActions, FreshserviceApi, FreshserviceTriggers):

    def __init__(self):
        super().__init__(
            name="Freshservice",
            description="Freshservice Cloud based ITSM software for your service desk " \
                "with powerful automation tool to manage incidents, assets and more.",
            category="Server Monitoring",
            logo="https://logo.500apps.com/freshservice",
            auth_info=None,
            auth_type='basic'
        )