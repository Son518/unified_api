import re

from pyasn1.type.univ import Null
from six import iteritems
from scheduling_bookings.google_calendar import util
from scheduling_bookings.google_calendar.entities.quick_add_event import GoogleCalendarQuickAddEvent
from scheduling_bookings.google_calendar.entities.event import GoogleCalendarEvent
from scheduling_bookings.google_calendar.api import GoogleCalendarAPI
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from unified.core.actions import Actions
import datetime
import json


class GoogleCalendarActions(Actions):

    def quick_add_event(self, context, payload):
        """ Add a quick event"""

        google_client = util.get_authentication(context["headers"])
        service = build('calendar', 'v3', credentials=google_client)
        event_data = GoogleCalendarQuickAddEvent(**payload)
        created_event = service.events().quickAdd(calendarId='primary',text=event_data.describe_event, sendUpdates="all").execute()
        
        # Add attendee to event
        if event_data.attendees is not None:
            event = {
                "start": created_event.get("start"),
                "end": created_event.get("end"),
                "attendees": [
                    {"email": event_data.attendees}
                ],
                "summary": created_event.get("summary")
            }
            updated_event = service.events().update(calendarId='primary', eventId=created_event['id'], body=event).execute()
            return updated_event
        return created_event

    def delete_event(self, context, payload):
        """ Delete event by Id"""

        google_client = util.get_authentication(context["headers"])
        service = build('calendar', 'v3', credentials=google_client)
        event_data = GoogleCalendarEvent(**payload)
        data = False

        if event_data.notify_attendes.lower() == "yes":
            data= True

        response = service.events().delete(calendarId='primary', eventId= event_data.event, sendNotifications= data).execute()
        
        # If successful, this method returns an empty response body.
        if response == "":
            return {"response":"Completed"}

        return response

    def update_event(slef, context, payload):
        """ Update Event"""

        google_client = util.get_authentication(context["headers"])
        service = build('calendar', 'v3', credentials=google_client)
        data = GoogleCalendarEvent(**payload)
        event = {}

        if data.summary is not None:
            event["summary"] = data.summary

        if data.description is not None:
            event["description"] = data.description

        if data.location is not None:
            event["location"] = data.location

        if data.start_date_time is not None:
            event["start"] = {
                "dateTime": data.start_date_time,
                "timeZone": data.timezone
            } 

        if data.end_date_time is not None:
            event["end"] = {
                "dateTime": data.end_date_time,
                "timeZone": data.timezone
            }

        if data.repeat_frequency is not None:
            repeat_frequency = data.repeat_frequency.upper()

            if data.repeat_on_these_days_of_the_week is not None:
                repeat_days = data.repeat_on_these_days_of_the_week[:2].upper()
                event["recurrence"] = [
                    f'RRULE:FREQ={repeat_frequency};BYDAY={repeat_days};COUNT={data.repeat_how_many_times}'
                ]

            else: 
                event["recurrence"] = [
                    f'RRULE:FREQ={repeat_frequency};COUNT={data.repeat_how_many_times}'
                ]

        if data.attendees is not None:
            event["attendees"] = [
                {'email': data.attendees}
            ]

        if data.color is not None:
            event["colorId"] = data.color

        if data.use_default_remainders is not None and data.use_default_remainders.lower() == "yes":
            event["reminders"] = {
                "useDefault": True
            }
        else:
            event["reminders"] = {
                "useDefault": False
            } 

        updated_event = service.events().update(calendarId='primary', eventId=data.event, body=event).execute()
        return updated_event

    def add_attendees_to_event(slef, context, payload):
        """ Add attendees to event"""

        google_client = util.get_authentication(context["headers"])
        service = build('calendar', 'v3', credentials=google_client)
        data = GoogleCalendarEvent(**payload)

        param = {
            "event_id": data.event
        }

        get_event_data = GoogleCalendarAPI.event(slef, context, param)

        event = {
            "start": {
                "dateTime": get_event_data["start_date_time"]
            },
            "end":{
                "dateTime": get_event_data["end_date_time"]
            },
            "summary": get_event_data["summary"]
        }

        if data.attendees is not None:
            event["attendees"] = [
                {'email': data.attendees}
            ]

        updated_event = service.events().update(calendarId='primary', eventId=data.event, body=event).execute()
        return updated_event

    def create_calendar(slef, context, payload):
        """ Create calendar"""

        google_client = util.get_authentication(context["headers"])
        service = build('calendar', 'v3', credentials=google_client)
        data = GoogleCalendarEvent(**payload)

        event = {
            "start":{
                "dateTime": data.start_date_time,
                "timeZone": data.timezone
            },
            "end":{
                "dateTime": data.end_date_time,
                "timeZone": data.timezone
            },
            "summary": data.name,
            "description": data.description
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        return event

    def create_detailed_event(slef, context, payload):
        """ Create detailed event"""

        google_client = util.get_authentication(context["headers"])
        service = build('calendar', 'v3', credentials=google_client)
        data = GoogleCalendarEvent(**payload)

        event = {
            "start":{
                "dateTime": data.start_date_time,
                "timeZone": data.timezone
            },
            "end":{
                "dateTime": data.end_date_time,
                "timeZone": data.timezone
            }
        }

        if data.summary is not None:
            event["summary"] = data.summary

        if data.description is not None:
            event["description"] = data.description

        if data.location is not None:
            event["location"] = data.location

        if data.repeat_frequency is not None:
            repeat_frequency = data.repeat_frequency.upper()

            if data.repeat_on_these_days_of_the_week is not None:
                repeat_days = data.repeat_on_these_days_of_the_week[:2].upper()
                event["recurrence"] = [
                    f'RRULE:FREQ={repeat_frequency};BYDAY={repeat_days};COUNT={data.repeat_how_many_times}'
                ]

            else: 
                event["recurrence"] = [
                    f'RRULE:FREQ={repeat_frequency};COUNT={data.repeat_how_many_times}'
                ]

        if data.attendees is not None:
            event["attendees"] = [
                {'email': data.attendees}
            ]

        if data.color is not None:
            event["colorId"] = data.color

        if data.use_default_remainders is not None and data.use_default_remainders.lower() == "yes":
            event["reminders"] = {
                "useDefault": True
            }
            
        else:
            event["reminders"] = {
                "useDefault": False
            } 

        if data.add_conferencing == "no":
            event["conferenceDataVersion"] = 0

        else:
            event["conferenceDataVersion"] = 1

        if data.guest_can_modify_event is not None and data.guest_can_modify_event.lower() == "no":
            event["guestsCanModify"] = False

        else:
            event["guestsCanModify"] = True

        event = service.events().insert(calendarId='primary', body=event).execute()
        return event
