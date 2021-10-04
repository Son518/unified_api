from dataclasses import dataclass
import json
from video_conferencing.clickmeeting import util
from unified.core.actions import Actions
from video_conferencing.clickmeeting.entities.clickmeeting_event import ClickmeetingEvent
from video_conferencing.clickmeeting.entities.clickmeeting_registrant import ClickmeetingRegistrant

class ClickmeetingActions:
    
    def create_new_event(self, context, payload):
        '''Creates a event.'''

        event_entity = ClickmeetingEvent(**payload)
        endpoint = f'conferences'
        data = {
                "name": event_entity.name,
                "room_type": event_entity.room_type,
                "access_type": event_entity.access_type,
                "permanent_room": event_entity.permanent_room
            }
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)

    def add_new_registrant(self, context, payload):
        '''Creates a registrants .'''

        register_entity = ClickmeetingRegistrant(**payload)
        endpoint = f'conferences/{register_entity.room_id}/registration'
        data = {
                "registration[1]" : register_entity.name,
                "registration[2]" : register_entity.last_name,
                "registration[3]" : register_entity.email_address
            }              
        response = util.rest("POST",endpoint,context['headers']['api_key'],data)
        return json.loads(response.text)