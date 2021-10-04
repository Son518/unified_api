# WaveApp - extends App, WaveTriggers, WaveActions, WaveAPI, ..

# from . import module

import json

from accounting_invoicing.wave.actions import WaveActions
from accounting_invoicing.wave.api import WaveApi

from unified.core.app import App, AuthInfo


class WaveApp(App, WaveActions, WaveApi):

    def __init__(self):
        super().__init__(
        name = "Wave",
        description = "Wave is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
        category = "Accounting Invoicing",
        logo = "https://logo.500apps.com/wave",
        auth_type = "oauth2",
        auth_info = None)
