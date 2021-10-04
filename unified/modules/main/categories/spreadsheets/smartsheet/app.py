from unified.core.app import App
from spreadsheets.smartsheet.actions import SmartsheetActions
from spreadsheets.smartsheet.triggers import SmartsheetTriggers
from spreadsheets.smartsheet.api import SmartsheetApi

class SmartsheetApp(App, SmartsheetActions, SmartsheetApi, SmartsheetTriggers):

    def __init__(self):
        super().__init__(
            name="Smartsheet",
            description="Smartsheet offers contact management, marketing automation, telephony, analytics, web engagement, real-time alerts and social suite. Track, nurture, and sell like a pro.",
            category="Spreadsheets",
            logo="https://logo.500apps.com/Smartsheet",
            auth_info=None,
            auth_type='Basic')
