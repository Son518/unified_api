from unified.core.app import App, AuthInfo
from ecommerce.shipstation.actions import ShipstationActions
from ecommerce.shipstation.triggers import ShipStationTrigger

class ShipstationApp(App, ShipstationActions, ShipStationTrigger):
    def __init__(self):
        super().__init__(
            name="Shipstation",
            description="ShipStation is the leading web-based order management and shipping software designed to make retailers exceptionally efficient at processing, fulfilling, and shipping their ecommerce orders.",
            category="ecommerce",
            logo="https://logo.500apps.com/shipstation",
            auth_info=None,
            auth_type='basic')
