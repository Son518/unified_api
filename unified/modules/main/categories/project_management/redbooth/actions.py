from unified.core.actions import Actions
from project_management.redbooth import util
from project_management.redbooth.entities.redbooth_comment import RedboothComment
from project_management.redbooth.entities.redbooth_subtask import RedboothSubtask
from project_management.redbooth.entities.redbooth_task import RedboothTask
from project_management.redbooth.entities.redbooth_taskslist import RedboothTaskslist
from project_management.redbooth.entities.redbooth_workspace import RedboothWorkspace
import datetime
import json


class RedboothActions(Actions):
    
    def create_comment(self, context, payload):
        """ Create comment"""
        
        access_token = util.get_authentication(context["headers"])  
        payload_data = RedboothComment(**payload)

        body = {
            "target_type" : payload_data.target_type,
            "target_id" : payload_data.task_id
        }

        if payload_data.body is not None:
            body["body"] = payload_data.body      

        response = util.rest("POST", f"comments", access_token, body)
        return json.loads(response.text)

    def create_subtask(self, context, payload):
        """ Create Subtask"""

        access_token = util.get_authentication(context["headers"])
        payload_data = RedboothSubtask(**payload)

        body = {
            "task_id" : payload_data.task_id,
            "name" : payload_data.name
        }     

        response = util.rest("POST", f"subtasks", access_token, body)
        return json.loads(response.text)

    def create_task(self, context, payload):
        """ Create Task"""

        access_token = util.get_authentication(context["headers"])
        payload_data = RedboothTask(**payload)

        body = {
            "project_id" : payload_data.project_id,
            "task_list_id" : payload_data.tasklist_id,
            "name": payload_data.name
        }     

        if payload_data.description is not None:
            body["description"] = payload_data.description

        if payload_data.is_private is not None:
            body["is_private"] = payload_data.is_private
        
        if payload_data.status is not None:
            body["status"] = payload_data.status

        if payload_data.urgent is not None:
            body["urgent"] = payload_data.urgent

        if payload_data.assignees is not None:
            body["assigned_user_ids"] = payload_data.assignees

        if payload_data.due_on is not None:
            body["due_on"] = payload_data.due_on
 
        response = util.rest("POST", f"tasks", access_token, body)
        return json.loads(response.text)

    def create_tasklist(self, context, payload):
        """ Create TaskList"""

        access_token = util.get_authentication(context["headers"])
        payload_data = RedboothTaskslist(**payload)

        body = {
            "project_id" : payload_data.project_id,
            "name" : payload_data.name
        }     

        response = util.rest("POST", f"task_lists", access_token, body)
        return json.loads(response.text)

    def create_workspace(self, context, payload):
        """ Create Workspace"""

        access_token = util.get_authentication(context["headers"])
        payload_data = RedboothWorkspace(**payload)

        body = {
            "organization_id" : payload_data.organization_id,
            "name" : payload_data.name
        }     

        if payload_data.tracks_time is not None:
            body["tracks_time"] = payload_data.tracks_time

        if payload_data.publish_pages is not None:
            body["publish_pages"] = payload_data.publish_pages

        if payload_data.is_public is not None:
            body["public"] = payload_data.is_public

        response = util.rest("POST", f"projects", access_token, body)
        return json.loads(response.text)
