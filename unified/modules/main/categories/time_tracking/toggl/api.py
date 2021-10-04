import json

from time_tracking.toggl.entities.toggl_client import TogglClient
from time_tracking.toggl.entities.toggl_project import TogglProject
from time_tracking.toggl.entities.toggl_tag import TogglTag
from time_tracking.toggl.entities.toggl_task import TogglTask
from time_tracking.toggl.entities.toggl_time_entry import TogglTimeEntry
from time_tracking.toggl import util

class TogglApi():

    def task_by_name(self, context, params):
        '''Gets a task by name'''

        method = "GET"
        url = "/workspaces/{id}/tasks".format(id=params["workspace_id"])

        task_list = json.loads(util.get_toggl_request(method, url, context['headers']).text)
        tasks = []

        for task in task_list:
            if params["name"] == task["name"]:
                toggl_task = TogglTask(
                    name=task.get("name"),
                    task_id=task.get("id"),
                    workspace_id=task.get("wid"),
                    project_id=task.get("pid"),
                    is_active=task.get("active")
                )
                tasks.append(toggl_task.__dict__)
        return json.dumps(tasks)

    def project_by_name(self, context, params):
        '''Gets a project by name'''

        method = "GET"
        url = "/workspaces/{id}/projects".format(id=params["workspace_id"])

        project_list = json.loads(util.get_toggl_request(method, url, context['headers']).text)
        projects = []

        for project in project_list:
            if params["name"] == project["name"]:
                toggl_project = TogglProject(
                    name=project.get("name"),
                    project_id=project.get("id"),
                    workspace_id=project.get("wid"),
                    is_project_billable=project.get("billable"),
                    is_project_private=project.get("is_private"),
                    is_active=project.get("active"),
                    template_id=project.get("template")
                )
                projects.append(toggl_project.__dict__)
        return json.dumps(projects)

    def tag_by_name(self, context, params):
        '''Gets a tag by name'''

        method = "GET"
        url = "/workspaces/{id}/tags".format(id=params["workspace_id"])

        tag_list = json.loads(util.get_toggl_request(method, url, context['headers']).text)
        tags = []

        for tag in tag_list:
            if params["name"] == tag["name"]:
                toggl_tag = TogglTag(
                    name=tag.get("name"),
                    tag_id=tag.get("id"),
                    workspace_id=tag.get("wid")
                )
                tags.append(toggl_tag.__dict__)
        return json.dumps(tags)

    def client_by_name(self, context, params):
        '''Gets a client by name'''

        method = "GET"
        url = "/clients"

        client_list = json.loads(util.get_toggl_request(method, url, context['headers']).text)
        clients = []

        for client in client_list:
            if params["name"] == client["name"]:
                toggl_client = TogglClient(
                    name=client.get("name"),
                    client_id=client.get("id"),
                    workspace_id=client.get("wid")
                )
                clients.append(toggl_client.__dict__)
        return json.dumps(clients)

    def time_entry(self, context, params):
        '''Gets a time entries'''

        method = "GET"
        url = "/time_entries"
        params = {
            "start_date": util.epoch_to_format("%Y-%m-%dT%H:%M:%SZ", params["start_time"]),
            "end_date": util.epoch_to_format("%Y-%m-%dT%H:%M:%SZ", params["end_time"])
        }

        time_entry_list = json.loads(util.get_toggl_request(method, url, context['headers'], params=params).text)
        time_entries = []

        for time_entry in time_entry_list:
            toggl_time_entry = TogglTimeEntry(
                time_entry_id=time_entry.get("id"),
                workspace_id=time_entry.get("wid"),
                project_id=time_entry.get("pid"),
                task_id=time_entry.get("tid"),
                billable=time_entry.get("billable"),
                start_time=time_entry.get("start"),
                stop_time=time_entry.get("stop"),
                description=time_entry.get("description"),
                duration=time_entry.get("duration"),
                created_with=time_entry.get("created_with"),
            )
            time_entries.append(toggl_time_entry.__dict__)
        return json.dumps(time_entries)
