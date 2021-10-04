from unified.core.triggers import Triggers
from project_management.pivotal_tracker.entities.pivotal_tracker_activity import PivotaltrackerActivity
from project_management.pivotal_tracker.entities.pivotal_tracker_story import PivotaltrackerStory
import json
from project_management.pivotal_tracker import util

class PivotaltrackerTriggers(Triggers):

    def new_activity(self, context, payload):
        """ Create new activity"""

        response = payload[0]
        changes = response["changes"][0]
        activity_obj = PivotaltrackerActivity(
                                            guid=response['guid'],
                                            kind=response['kind'],
                                            project_version=response['project_version'],
                                            message=response['message'],
                                            highlight=response["highlight"],
                                            id=changes["id"],
                                            change_type=changes['change_type'],
                                            story_id=changes['new_values']['story_id'],
                                            text=changes['new_values']['text'],
                                            person_id=changes['new_values']['person_id'],
                                            created_at=changes['new_values']['created_at'],
                                            updated_at=changes['new_values']['updated_at']
                                        )
        return activity_obj.__dict__

    def new_story(self, context, payload):
        """ Create new story"""

        response = payload[0]
        changes = response["changes"][0]
        story_obj = PivotaltrackerStory(
                                    guid=response['guid'],
                                    kind=response['kind'],
                                    project_version=response['project_version'],
                                    message=response['message'],
                                    highlight=response["highlight"],
                                    id=changes["id"],
                                    change_type=changes['change_type'],
                                    created_at=changes['new_values']['created_at'],
                                    updated_at=changes['new_values']['updated_at']
                                )
        return story_obj.__dict__