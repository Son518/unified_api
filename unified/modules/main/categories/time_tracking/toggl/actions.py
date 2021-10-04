import json

from unified.core.actions import Actions
from time_tracking.toggl import util
from time_tracking.toggl.entities.toggl_client import TogglClient
from time_tracking.toggl.entities.toggl_project import TogglProject
from time_tracking.toggl.entities.toggl_tag import TogglTag
from time_tracking.toggl.entities.toggl_task import TogglTask
from time_tracking.toggl.entities.toggl_time_entry import TogglTimeEntry

class TogglActions(Actions):

    def create_client(self, context, task_entity):
        '''Creates a new client'''

        task_schema = TogglClient(**task_entity)
        method = "POST"
        url = "/clients"

        task_data = {
            "client": {
                "wid": task_schema.workspace_id,
                "name": task_schema.name
                }
            }

        result = util.get_toggl_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_project(self, context, task_entity):
        '''Creates a new project'''

        task_schema = TogglProject(**task_entity)
        method = "POST"
        url = "/projects"

        task_data = {
            "project": {
                "wid": task_schema.workspace_id,
                "name": task_schema.name,
                "cid": task_schema.client_id,
                "template_id": task_schema.template_id,
                }
            }
        if task_schema.is_project_private:
            task_data["project"]["is_private"] = task_schema.is_project_private
        if task_schema.is_project_billable:
            task_data["project"]["billable"] = task_schema.is_project_billable

        result = util.get_toggl_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_tag(self, context, task_entity):
        '''Creates a new tag'''

        task_schema = TogglTag(**task_entity)
        method = "POST"
        url = "/tags"

        task_data = {
            "tag": {
                "wid": task_schema.workspace_id,
                "name": task_schema.name
                }
            }

        result = util.get_toggl_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_task(self, context, task_entity):
        '''Creates a new task'''

        task_schema = TogglTask(**task_entity)
        method = "POST"
        url = "/tasks"

        task_data = {
            "task":{
                "wid": task_schema.workspace_id,
                "name": task_schema.name,
                "pid": task_schema.project_id
                }
            }
        if task_schema.is_active:
            task_data["task"]["active"] = task_schema.is_active

        result = util.get_toggl_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_time_entry(self, context, task_entity):
        '''Creates a new time entry'''

        task_schema = TogglTimeEntry(**task_entity)
        method = "POST"
        url = "/time_entries"

        task_data = {
            "time_entry": {
                "wid": task_schema.workspace_id,
                "pid": task_schema.project_id,
                "tid": task_schema.task_id,
                "duration": task_schema.duration,
                "start": task_schema.start_time,
                "stop": task_schema.stop_time,
                "description": task_schema.description,
                "created_with": task_schema.created_with
                }
            }
        if task_schema.billable:
            task_data["time_entry"]["billable"] = task_schema.billable

        result = util.get_toggl_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def start_time_entry(self, context, task_entity):
        '''Starts a new time entry'''

        task_schema = TogglTimeEntry(**task_entity)
        method = "POST"
        url = "/time_entries/start"

        task_data = {
            "time_entry": {
                "wid": task_schema.workspace_id,
                "pid": task_schema.project_id,
                "tid": task_schema.task_id,
                "duration": task_schema.duration,
                "start": task_schema.start_time,
                "stop": task_schema.stop_time,
                "description": task_schema.description,
                "created_with": task_schema.created_with
                }
            }
        if task_schema.billable:
            task_data["time_entry"]["billable"] = task_schema.billable

        result = util.get_toggl_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def stop_time_entry(self, context, task_entity):
        '''Stops an existing time entry'''

        task_schema = TogglTimeEntry(**task_entity)
        method = "PUT"
        url = "/time_entries/{id}/stop".format(id=task_schema.time_entry_id)

        result = util.get_toggl_request(method, url, context['headers'])
        return json.loads(result.text)
