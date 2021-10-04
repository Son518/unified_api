import json
from task_management.googletasks import util
from task_management.googletasks.entities.task import Googletasks_task
from unified.core.util import google_profile


class GoogletasksApi:

    def task(self, context, params):
        """ Get task"""

        access_token = util.get_authentication(context["headers"])
        list_id = params.get("task_list_id")
        task_id = params.get("task_id")
        response = util.rest("GET", f"lists/{list_id}/tasks/{task_id}", access_token)
        response = json.loads(response.text)
        data = Googletasks_task(
            task_id = response["id"],
            title = response["title"],
            status = response["status"],
            task_list_id = list_id,
            notes = response.get("notes")
        )
        return data.__dict__

    def tasks_by_project_id(self, context, params):
        """ Get tasks by projectid"""

        access_token = util.get_authentication(context["headers"])
        list_id = params.get("project_id")
        response = util.rest("GET", f"lists/{list_id}/tasks", access_token)
        response = json.loads(response.text)
        if len(response.get("items")):
            items = response.get("items")
            data_list = []
            for item in items:
                data = Googletasks_task(
                    task_id = item["id"],
                    name = item["title"],
                    status = item["status"],
                    task_list_id = list_id,
                    notes = item.get("notes")
                )
                data_list.append(data.__dict__)
            return json.dumps(data_list)
        return response

    def projects(self, context, params):
        """ Get projects"""

        access_token = util.get_authentication(context["headers"])
        response = util.rest("GET", f"users/@me/lists", access_token)
        response = json.loads(response.text)
        if len(response.get("items")):
            items = response.get("items")
            data_list = []
            for item in items:
                data = {
                    "id": item["id"],
                    "project_name": item["title"]
                }
                data_list.append(data)
            return json.dumps(data_list)
        return json.dumps(response)     

    def profile(self, context, params):
        """Get Profile details"""

        return google_profile(context, params)
