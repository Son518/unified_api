import json
from requests.models import Response
from time_tracking.clockify.entities.clockify_create_project import ClockifyProject
from time_tracking.clockify.entities.clockify_create_client import ClockifyClient
from time_tracking.clockify.entities.clockify_create_tag import ClockifyTag
from time_tracking.clockify.entities.clockify_create_time_entry import ClockifyTimeEntry
from time_tracking.clockify.entities.clockify_create_task import ClockifyTask
from time_tracking.clockify.entities.clockify_stop_timer import ClockifyStopTimer
from core.actions import Actions
from time_tracking.clockify import util

class ClockifyActions(Actions):

    def create_project(self, context, project_payload):
        """ 
        Creates project
        context holds the headers 
        project_entity holds the request.body
        """
        project_entity = ClockifyProject(**project_payload)
        data = {
                "name": project_entity.name,
                "clientId": project_entity.client_id,
                "isPublic": project_entity.is_project_public,
                "billable": project_entity.is_project_billable
            }     
        response = util.rest("POST","projects",data,context["headers"]["api_key"],project_entity.workspace_id)
        return json.loads(response.text)

    def create_client(self, context, client_payload):
        """ 
        Creates client
        context holds the headers 
        client_entity holds the request.body
        """
        client_entity = ClockifyClient(**client_payload)
        data = {
                "name": client_entity.name
            }     
        response = util.rest("POST","client",data,context["headers"]["api_key"],client_entity.workspace_id)
        return json.loads(response.text)

    def create_tag(self, context, tag_payload):
        """ 
        Creates tag
        context holds the headers 
        tag_entity holds the request.body
        """
        tag_entity = ClockifyTag(**tag_payload)
        data = {
                "name": tag_entity.name
            }     
        response = util.rest("POST","tag",data,context["headers"]["api_key"],tag_entity.workspace_id)
        return json.loads(response.text)
    
    def create_time_entry(self, context, time_payload):
        """ 
        Creates time
        context holds the headers 
        time_entity holds the request.body
        """
        time_entity = ClockifyTimeEntry(**time_payload)
        data = {
                "start": time_entity.start_datetime,
                "billable": time_entity.billable,
                "description": time_entity.description,
                "projectId": time_entity.project_id,
                "taskId": time_entity.task_id,
                "end": time_entity.end_datetime,
                "tagIds": [
                    time_entity.tag_id
                ]   
            }
        response = util.rest("POST","time",data,context["headers"]["api_key"],time_entity.workspace_id)
        return json.loads(response.text)
    
    def create_task(self, context, task_payload):
        """ 
        Creates task
        context holds the headers 
        task_entity holds the request.body
        """
        task_entity = ClockifyTask(**task_payload)
        data = {
                "name": task_entity.name,
                "status": task_entity.status
            }
        response = util.rest("POST","task",data,context["headers"]["api_key"],task_entity.workspace_id,id=task_entity.project_id)
        return json.loads(response.text)
    
    def stop_timer(self, context, time_payload):
        """ 
        Stops timer
        context holds the headers 
        time_entity holds the request.body
        """
        time_entity = ClockifyStopTimer(**time_payload)
        data = {
                "end": time_entity.end_datetime,
                "projectId": time_entity.project_id
            }
        response = util.rest("POST","stop",data,context["headers"]["api_key"],time_entity.workspace_id,time_entity.user_id)
        return json.loads(response.text)