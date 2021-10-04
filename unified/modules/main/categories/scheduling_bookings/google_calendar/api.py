from pyasn1.type.univ import Null
from scheduling_bookings.google_calendar import util
from scheduling_bookings.google_calendar.entities.event import GoogleCalendarEvent
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from unified.core.util import google_profile
import datetime
import json

class GoogleCalendarAPI():

    def event(self,context,params):
        """ Get event by id"""
        
        google_client = util.get_authentication(context["headers"])
        service = build('calendar', 'v3', credentials=google_client)
        event = service.events().get(calendarId='primary', eventId=params.get("event_id") or params.get("id")).execute()
        attendees_info = []

        for attendee in event["attendees"]:
            attendees_info.append(str(attendee["email"]))

        data = GoogleCalendarEvent(
            event= event["id"],
            event_id= event["id"],
            location= event.get("location"),
            calendar= event["organizer"]["email"],
            summary=event.get("summary"),
            start_date_time= event["start"]["dateTime"],
            end_date_time= event["end"]["dateTime"],
            description= event.get("description"),
            attendees= attendees_info
        )
        return data.__dict__

    def profile(self, context, params):
        """Get Profile details"""

        return google_profile(context, params)