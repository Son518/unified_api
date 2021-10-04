# ClickSendApp - extends App, ClickSendTriggers, ClickSendActions, ClickSendAPI, ..

# from . import module

import json

from phone_sms.clicksend_sms.actions import ClickSendActions
from phone_sms.clicksend_sms.api import ClickSendApi
from phone_sms.clicksend_sms.triggers import ClickSendTriggers

from unified.core.app import App, AuthInfo


class ClicksendsmsApp(App, ClickSendActions, ClickSendApi, ClickSendTriggers):

    def __init__(self):
        super().__init__(
        name = "ClickSend",
        description = "ClickSend  is a cloud-based gateway service for your business that lets you send bulk SMS, email, fax & letters worldwide.",
        category = "Phone and SMS",
        logo = "https://logo.500apps.com/clicksend",
        auth_type = "basic",
        auth_info = None
)
