from unified.core.app import App, AuthInfo
from file_management_storage.dropbox.actions import DropboxActions
from file_management_storage.dropbox.api import DropboxApi


class DropboxApp(App, DropboxActions, DropboxApi):
    def __init__(self):
        super().__init__(
            name="Dropbox",
            description="Dropbox lets you store your files online, sync them to all your devices, and share them easily. Get started for free, then upgrade for more space and security features.",
            category="File Management Storage",
            logo="https://logo.500apps.com/drop-box",
            auth_info=None,
            auth_type='oauth2'
        )
