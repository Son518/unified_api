from unified.core.triggers import Triggers
from project_management.wrike.entities.wrike_project import WrikeProject
from project_management.wrike.entities.wrike_task import WrikeTask
import json


class WrikeTriggers(Triggers):

    def new_folder(self, context, payload):
        ''' triggers when new folder created'''

        project = WrikeProject(
            id=payload["folderId"],
            event_author_id=payload["eventAuthorId"],
            event_type=payload["eventType"],
            updated_date=payload["lastUpdatedDate"],
        )

        return project.__dict__

    def new_task(self, context, payload):
        ''' triggers when new task created'''

        task = WrikeTask(
            id=payload["taskId"],
            event_author_id=payload["eventAuthorId"],
            event_type=payload["eventType"],
            updated_date=payload["lastUpdatedDate"],
        )

        return task.__dict__
