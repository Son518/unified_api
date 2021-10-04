from payment_processing.stripe.api import StripeApi
from payment_processing.stripe.triggers import StripeTriggers
from unified.core.app import App, AuthInfo
from payment_processing.stripe.actions import StripeActions
from payment_processing.stripe.api import StripeApi
from payment_processing.stripe.triggers import StripeTriggers
# from project_management.basecamp3.triggers import Basecamp3Triggers
# from project_management.basecamp3.api import Basecamp3Api


class StripeApp(App, StripeActions, StripeApi, StripeTriggers): #, Basecamp3Triggers, Basecamp3Api):

    def __init__(self):
        super().__init__(
            name="Stripe",
            description="",
            category="Payment processing",  # is this field really required???
            logo="https://logo.500apps.com/stripe",
            auth_info = None,
            # AuthInfo(
            #     client_id="1198740404539678",
            #     client_secret="bd9acdf6a05a4049bd46e6fdf557d0c4",
            #     token="1/1198849786214579:131d44492abb2c281b565e72586b91ec",
            #     refresh_url="https://app.asana.com/-/oauth_token"
            # ),
            auth_type='oauth2')
