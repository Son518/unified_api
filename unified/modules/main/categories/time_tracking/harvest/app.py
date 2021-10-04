from unified.core.app import App
from time_tracking.harvest.actions import HarvestAction
from time_tracking.harvest.api import HarvestApi


class HarvestApp(App, HarvestAction, HarvestApi):

    def __init__(self):
        super().__init__(
            name="Harvest",
            description="Harvest is modern time tracking software – for less effort, more joy, and improved profitability.",
            category="Time Tracking",
            logo="https://logo.500apps.com/harvest",
            auth_info=None,
            auth_type='basic'
        )