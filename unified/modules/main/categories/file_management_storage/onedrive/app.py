from unified.core.app import App
from file_management_storage.onedrive.actions import OnedriveActions
from file_management_storage.onedrive.api import OnedriveApi


class OnedriveApp(App, OnedriveActions, OnedriveApi):

    def __init__(self):
        super().__init__(
            name="OneDrive",
            description="Save your files and photos to OneDrive and access them from any device, anywhere.",
            category="File Management Storage",
            logo="https://logo.500apps.com/onedrive",
            auth_info=None,
            auth_type='oauth2'
        )