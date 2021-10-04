from unified.core.actions import Actions
from task_management.googletasks import util
from task_management.googletasks.entities.task import Googletasks_task
from task_management.googletasks.entities.list import Googletasks_list
import datetime
import json


class GoogletasksActions(Actions):

    def create_task(self, context, payload):
        """ Create task"""

        access_token = util.get_authentication(context["headers"])
        task_data = Googletasks_task(**payload)

        body = {
            "title": task_data.title,
            "task_list_id": task_data.task_list_id
        }

        if task_data.notes is not None:
            body["notes"] = task_data.notes

        if task_data.due_on is not None:
            body["due_date"] = task_data.due_on

        response = util.rest("POST", f"lists/{task_data.task_list_id}/tasks", access_token, body)
        return json.loads(response.text)

    def create_task_list(self, context, payload):
        """ Create a task list"""

        access_token = util.get_authentication(context["headers"])
        task_data = Googletasks_list(**payload)
        body = {"title": task_data.list_title}
        response = util.rest("POST", f"users/@me/lists", access_token, body)
        return json.loads(response.text)

    def update_task(self, context, payload):
        """ Create task"""

        access_token = util.get_authentication(context["headers"])
        task_data = Googletasks_task(**payload)

        body = {
            "title": task_data.title,
            "task_list_id": task_data.task_list_id,
            "id": task_data.task_id
        }

        if task_data.notes is not None:
            body["notes"] = task_data.notes

        if task_data.due_on is not None:
            body["due_date"] = task_data.due_on
        
        if task_data.status is not None:
            body["status"] = task_data.status

        response = util.rest("PUT", f"lists/{task_data.task_list_id}/tasks/{task_data.task_id}", access_token, body)
        response = json.loads(response.text)
        response["id"] = task_data.task_id
        return response  
