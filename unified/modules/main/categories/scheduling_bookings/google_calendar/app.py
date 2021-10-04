import asana
import json

from scheduling_bookings.google_calendar.action import GoogleCalendarActions
from scheduling_bookings.google_calendar.api import GoogleCalendarAPI
from unified.core.app import App, AuthInfo


class GooglecalendarApp(App, GoogleCalendarActions, GoogleCalendarAPI):

    def __init__(self):
        super().__init__(
        name = "GoogleCalender",
        description = "Google Calender is a collaborative information manager for workspace. It helps you organize people and tasks effectively.",
        category = "Scheduling booking",
        logo = "https://logo.500apps.com/googlecalendar",
        auth_info = None,
        auth_type = 'oauth2')