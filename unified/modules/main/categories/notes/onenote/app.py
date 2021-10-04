import json
from notes.onenote.actions import OnenoteActions
from notes.onenote.api import OnenoteApi
from unified.core.app import App, AuthInfo

class OnenoteApp(App,OnenoteActions,OnenoteApi):

    def __init__(self):
        super().__init__(
            name="OneNote",
            description="OneNote is a digital notebook that automatically saves and syncs your notes as you work.",
            category="notes",
            logo="https://logo.500apps.com/OneNote",
            auth_info=None,
            auth_type='oauth2')