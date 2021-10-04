from dataclasses import dataclass
import json
from video_conferencing.livestorm import util
from unified.core.actions import Actions
from video_conferencing.livestorm.entities.livestorm_session import LivestormSession

class LivestormActions:
    
    def create_registrant(self, context, payload):
        '''Creates a session.'''
        
        session_entity = LivestormSession(**payload)
        endpoint = f"sessions/{session_entity.session_id}/people"
        session_data = {
                        "data": {
                            "type": session_entity.type,
                            "attributes": {
                                    "fields": [
                                            {
                                                "id": "first_name",
                                                "value": session_entity.first_name
                                            },
                                            {
                                                "id": "last_name",
                                                "value": session_entity.last_name
                                            },
                                            {
                                                "id": "email",
                                                "value": session_entity.email
                                            }
                                        ],
                                    "referrer": "referrer",
                                    "utm_source": "utm_source",
                                    "utm_medium": "utm_medium",
                                    "utm_term": "utm_term",
                                    "utm_content": "utm_content",
                                    "utm_campaign": "utm_campaign"
                                }
                            }
                        }
        response = util.rest("POST",endpoint,context['headers']['api_key'],session_data)
        return json.loads(response.text)