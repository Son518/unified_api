import json
from requests.models import Response
from core.triggers import Triggers
from time_tracking.clockify.entities.clockify_create_project import ClockifyProject
from time_tracking.clockify.entities.clockify_create_client import ClockifyClient
from time_tracking.clockify.entities.clockify_create_tag import ClockifyTag
from time_tracking.clockify.entities.clockify_create_task import ClockifyTask
from time_tracking.clockify.entities.clockify_create_time_entry import ClockifyTimeEntry
from time_tracking.clockify.entities.clockify_new_timer_started import ClockifyTimerStarted

class ClockifyTriggers(Triggers):

    def new_project(self,context,payload):
        """
        triggers when new project created 
        context holds the headers 
        payload holds the request.body
        """
        data = ClockifyProject(
                                name = payload["name"],
                                client_id = payload["clientId"],
                                is_project_public = payload["public"],
                                is_project_billable = payload["billable"],
                                workspace_id = payload["workspaceId"]
                            )
        return data.__dict__

    def new_client(self,context,payload):
        """
        triggers when new project created 
        context holds the headers 
        payload holds the request.body
        """
        data = ClockifyClient(
                                name = payload["name"],
                                id = payload["id"],
                                archived = payload["archived"],
                                workspace_id = payload["workspaceId"]
                            )
        return data.__dict__

    def new_tag(self,context,payload):
        """
        triggers when new tag created 
        context holds the headers 
        payload holds the request.body
        """
        data = ClockifyTag(
                            name = payload["name"],
                            id = payload["id"],
                            archived = payload["archived"],
                            workspace_id = payload["workspaceId"]
                        )
        return data.__dict__

    def new_time_entry(self,context,payload):
        """
        triggers when new time  created 
        context holds the headers 
        payload holds the request.body
        """
        data = ClockifyTimeEntry(
                                    id = payload["id"],
                                    workspace_id = payload["workspaceId"],
                                    start_datetime = payload["timeInterval"]["start"],
                                    end_datetime = payload["timeInterval"]["end"],
                                    project_id = payload["projectId"],
                                    task_id = payload["task"]["id"],
                                    tags = payload["tags"],
                                    is_project_billable = payload["billable"],
                                    description = payload["description"]
                                )
        return data.__dict__

    def new_task(self,context,payload):
        """
        triggers when new task created 
        context holds the headers 
        payload holds the request.body
        """
        data = ClockifyTask(     
                                name = payload["name"],
                                status = payload["status"],
                                project_id = payload["projectId"],
                                id = payload["id"],
                                estimate = payload["estimate"],
                                billable = payload["billable"]
                            )
        return data.__dict__

    def new_timer_started(self,context,payload):
        """
        triggers when new time started 
        context holds the headers 
        payload holds the request.body
        """
        data = ClockifyTimerStarted(     
                                        project_id = payload["projectId"],
                                        workspace_id = payload["workspaceId"],
                                        description = payload["description"],
                                        is_billable = payload["billable"],
                                        user_id = payload["userId"],
                                        start = payload["timeInterval"]["start"]
                                    )
        return data.__dict__