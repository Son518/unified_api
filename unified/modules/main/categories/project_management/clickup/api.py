from project_management.clickup import util
from project_management.clickup.entities.clickup_folder import ClickupFolder
from project_management.clickup.entities.clikup_tasklist import ClickupTasklist
from project_management.clickup.entities.clickup_task import ClickupTask
import json


class ClickupApi:
    def folder(self, context, params):
        '''gets a folder'''

        url = f"https://api.clickup.com/api/v2/folder/{params['folder_id']}"

        response = util.rest("GET", url, context=context)

        folder_obj = json.loads(response.text)

        folder = ClickupFolder(
            space_id=folder_obj['space']['id'],
            folder_name=folder_obj['name'],
            folder_id=folder_obj['id'],
            is_archived=folder_obj['archived'],
            task_count=folder_obj['task_count'],
        )

        return folder.__dict__

    def tasklist(self, context, params):
        '''gets a tasklist'''

        url = f"https://api.clickup.com/api/v2/list/{params['tasklist_id']}"
        response = util.rest("GET", url, context=context)

        tasklist_obj = json.loads(response.text)

        tasklist = ClickupTasklist(
            folder_id=tasklist_obj['folder']['id'],
            priority=tasklist_obj['priority'],
            assignee_to=tasklist_obj['assignee'],
            due_date=tasklist_obj['due_date'],
            id=tasklist_obj['id'],
            name=tasklist_obj['name'],
        )

        return tasklist.__dict__

    def task(self, context, params):
        '''get a task'''

        url = f"https://api.clickup.com/api/v2/task/{params['task_id']}"
        response = util.rest("GET", url, context=context)

        task_obj = json.loads(response.text)
        task = ClickupTask(
            due_date=task_obj['due_date'],
            list_id=task_obj['list']['id'],
            tag=task_obj['tags'],
            id=task_obj['id'],
            name=task_obj['name'],
            description=task_obj['description'],
            task_id=task_obj['id'],
            assigned_to=task_obj['assignees'],
        )

        return task.__dict__

    def tasks(self, context, params):
        '''get list of task in list or team '''

        if params.get('list_id'):
            url = f"https://api.clickup.com/api/v2/list/{params['list_id']}/task"
        else:
            url = f"https://api.clickup.com/api/v2/team/{params['team_id']}/task"

        response = util.rest("GET", url, context=context)

        task_list = json.loads(response.text)['tasks']

        tasks = []

        for task_obj in task_list:
            task = ClickupTask(
                due_date=task_obj['due_date'],
                list_id=task_obj['list']['id'],
                tag=task_obj['tags'],
                id=task_obj['id'],
                name=task_obj['name'],
                description=task_obj['description'],
                task_id=task_obj['id'],
                assigned_to=task_obj['assignees'],
            )
            tasks.append(task.__dict__)

        return json.dumps(tasks)
    
    def profile(self, context, payload):
        url = "https://api.clickup.com/api/v2/user"
        response_data = util.rest("GET", url, context=context)
        response = response_data.json()['user']
        profile = {
            'id':response['id'],
            'email':response['email'],
            'name':response['username']
        }
        return profile, response_data.status_code

    def verify(self, context, payload):
        url = "https://api.clickup.com/api/v2/team"
        response_data = util.rest("GET", url, context=context)
        response = response_data.json()
        return response, response_data.status_code
