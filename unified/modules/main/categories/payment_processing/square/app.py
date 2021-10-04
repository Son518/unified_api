from unified.core.app import App
from payment_processing.square.actions import SquareActions
from payment_processing.square.triggers import SquareTriggers
from payment_processing.square.api import SquareApi


class SquareApp(App, SquareActions, SquareTriggers, SquareApi):

    def __init__(self):
        super().__init__(
            name="Basecamp 3",
            description="Square helps millions of sellers run their business-from secure credit card processing to point of sale solutions.",
            category="Payment Processing",
            logo="https://logo.500apps.com/square",
            auth_info=None,
            auth_type='oauth2')
