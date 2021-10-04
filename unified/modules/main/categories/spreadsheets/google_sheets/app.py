from unified.core.app import App
from spreadsheets.google_sheets.actions import GooglesheetsActions
from spreadsheets.google_sheets.api import GooglesheetsApi
from spreadsheets.google_sheets.triggers import GooglesheetsTriggers


class GooglesheetsApp(App, GooglesheetsActions, GooglesheetsApi, GooglesheetsTriggers):

    def __init__(self):
        super().__init__(
            name="Google Sheets",
            description="Create, edit, and collaborate on spreadsheets with the Google Sheets app.",
            category="Spreadsheets",
            logo="https://logo.500apps.com/GoogleSheets",
            auth_info=None,
            auth_type='oauth2'
        )