from project_management.wrike import util
from project_management.wrike.entities.wrike_project import WrikeProject
from project_management.wrike.entities.wrike_task import WrikeTask
import json


class WrikeApi():

    def tasks(self, context, task_entity):
        ''' gets all tasks'''

        access_token = util.get_access_token(context['headers'])
        url = "https://www.wrike.com/api/v4/tasks"
        response = json.loads(util.rest("GET", url, {}, access_token).text)
        tasks = response.get('data')
        task_value = []

        for task in tasks:
            task_obj = WrikeTask(task_id=task['id'],
                                 updated_date=task['updatedDate'],
                                 created_date=task['createdDate'],
                                 name=task['title'],
                                 task_importance=task['importance'],
                                 task_type=task['scope'],
                                 attachment_url=task['permalink'])
            task_value.append(task_obj.__dict__)

        return json.dumps(task_value)

    def tasks_by_project_id(self, context, payload):
        ''' gets tasks based on project id'''

        access_token = util.get_access_token(context['headers'])
        url = f"https://www.wrike.com/api/v4/folders/{payload['project_id']}/tasks"
        tasks = json.loads(
            util.rest("GET", url, {}, access_token).text).get('data')
        task_value = []

        for task in tasks:
            task_obj = WrikeTask(task_id=task['id'],
                                 updated_date=task['updatedDate'],
                                 created_date=task['createdDate'],
                                 name=task['title'],
                                 task_importance=task['importance'],
                                 task_type=task['scope'],
                                 attachment_url=task['permalink'])
            task_value.append(task_obj.__dict__)

        return json.dumps(task_value)

    def task(self, context, payload):
        ''' gets task based on task_id'''

        access_token = util.get_access_token(context['headers'])
        url = "https://www.wrike.com/api/v4/tasks"
        response = json.loads(util.rest("GET", url, {}, access_token).text)
        tasks = response.get('data')
        task_value = []

        for task in tasks:
            if payload['task_id'] == task['id']:
                task_obj = WrikeTask(task_id=task['id'],
                                     updated_date=task['updatedDate'],
                                     created_date=task['createdDate'],
                                     name=task['title'],
                                     task_importance=task['importance'],
                                     task_type=task['scope'],
                                     attachment_url=task['permalink'])
                task_value.append(task_obj.__dict__)

        return json.dumps(task_value)

    def folders(self,context,payload):
        ''' gets all folders '''

        access_token = util.get_access_token(context['headers'])
        url = "https://www.wrike.com/api/v4/folders"
        folders = json.loads(util.rest("GET", url, {}, access_token).text)["data"]
        folder_value=[]
        for folder in folders:
            if "project" in folder.keys():
                folder_obj = WrikeProject(id=folder["id"],
                                    project_name=folder["title"],
                                    created_date=folder["project"]["createdDate"])
                folder_value.append(folder_obj.__dict__)
        return json.dumps(folder_value)
    
    def projects(self,context,payload):
        ''' gets all projects'''
        return self.folders(context,payload)

    def profile(self,context,payload):
        ''' gets all folders '''

        access_token = util.get_access_token(context['headers'])
        url = "https://www.wrike.com/api/v4/account"
        response = util.rest("GET", url, {}, access_token)
        result = (response.json())['data'][0]
        profile = {
            'id' : result['id'],
            'name': result['name']
        }
        return profile