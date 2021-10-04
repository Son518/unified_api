from unified.core.triggers import Triggers
from video_conferencing.livestorm.entities.livestorm_event import LivestormEvent
import json
from video_conferencing.livestorm import util

class LivestormTriggers(Triggers):

    def event_end(self, context, payload):
        """ Create event end"""

        response = payload.get('webinar')
        event_obj = LivestormEvent(
                                    title=response.get('title') or None,
                                    slug=response.get('slug') or None,
                                    created_at=response.get('created_at') or None,
                                    registration_link=response.get('registration_link') or None,
                                    estimated_duration=response.get('estimated_duration') or None,
                                    published_at=response.get('published_at') or None,
                                    room_link=response.get('room_link') or None,
                                    estimated_started_at=response.get('estimated_started_at') or None,
                                    started_at=response.get('started_at') or None,
                                    ended_at=response.get('ended_at') or None,
                                    duration=response.get('duration') or None,
                                    nb_attended=response.get('nb_attended') or None,
                                    nb_registered=response.get('nb_registered') or None,
                                    identify=response.get('identify') or None
                                )
        return event_obj.__dict__

    def event_pulished(self, context, payload):
        """ Create event pulished """

        response = payload.get('webinar')
        event_obj = LivestormEvent(
                                    title=response.get('title') or None,
                                    slug=response.get('slug') or None,
                                    created_at=response.get('created_at') or None,
                                    registration_link=response.get('registration_link') or None,
                                    estimated_duration=response.get('estimated_duration') or None,
                                    published_at=response.get('published_at') or None,
                                    nb_registered=response.get('nb_registered') or None,
                                    identify=response.get('identify') or None
                                )
        return event_obj.__dict__

    def event_start(self, context, payload):
        """ Create event start"""

        response = payload.get('webinar')
        event_obj = LivestormEvent(
                                    title=response.get('title') or None,
                                    slug=response.get('slug') or None,
                                    created_at=response.get('created_at') or None,
                                    registration_link=response.get('registration_link') or None,
                                    published_at=response.get('published_at') or None,
                                    room_link=response.get('room_link') or None,
                                    estimated_started_at=response.get('estimated_started_at') or None,
                                    started_at=response.get('started_at') or None,
                                    nb_registered=response.get('nb_registered') or None,
                                    identify=response.get('identify') or None,
                                    estimated_duration=response.get('estimated_duration') or None
                                )
        return event_obj.__dict__