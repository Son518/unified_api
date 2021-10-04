from unified.core.app import App, AuthInfo
from file_management_storage.google_drive.api import GoogledriveApi
from file_management_storage.google_drive.actions import GoogledriveAction
from file_management_storage.google_drive.triggers import GoogledriveTriggers


class GoogledriveApp(App, GoogledriveAction, GoogledriveApi, GoogledriveTriggers):
    def __init__(self):
        super().__init__(
            name="Google Drive",
            description="Google Drive is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
            category="File Management and Storage",
            logo="https://logo.500apps.com/google-drive",
            auth_info=None,
            auth_type='oauth2')
