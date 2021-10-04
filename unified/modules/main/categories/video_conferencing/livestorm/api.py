import json
from flask import jsonify
import requests
from requests.api import request
from video_conferencing.livestorm.entities.livestorm_session import LivestormSession
from video_conferencing.livestorm import util

class LivestormApi():

    def session(self, context, params):
        '''get session by id'''

        endpoint = f"sessions/{params['session_id']}"
        response = json.loads(util.rest("GET",endpoint,context['headers']["api_key"]).text)
        result=response.get('data')
        session_obj = LivestormSession(
                                        session_id=result.get('id') or None,
                                        type=result.get('type') or None, 
                                        event_id=result.get('attributes').get('event_id') or None,
                                        status=result.get('attributes').get('status') or None,
                                        timezone=result.get('attributes').get('timezone') or None,
                                        registrants_count=result.get('attributes').get('registrants_count') or None,
                                        room_link=result.get('attributes').get('room_link') or None
                                    )
        return session_obj.__dict__