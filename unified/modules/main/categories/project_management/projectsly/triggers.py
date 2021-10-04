from project_management.projectsly.entities.projectsly_projects import ProjectslyProjects
from project_management.projectsly.entities.projectsly_task import ProjectslyTask
from unified.core.triggers import Triggers

import json


class ProjectslyTriggers:
    def new_project(self, context, payload):
        '''Trigger when new project is created'''

        project = self.mappings_of_project(payload)
        return project

    def updated_project(self, context, payload):
        '''Trigger when project is updated'''

        project = self.mappings_of_project(payload)
        return project

    def mappings_of_project(self, project):
        data = json.loads(project['data']['config']['data'])
        projects = ProjectslyProjects(
            id=project['data']['data']['message'][0]['message']['insertdata'][0]['GENERATED_KEY'] if project['data']['data'].get(
                'message') else None,
            project_name=data.get('name'),
            project_description=data.get('description'),
            icon=data.get('icon'),
            color=data.get('color'),
            member_id=data.get('member_id'),
            is_public=data.get('is_public')
        )
        return projects.__dict__

    def new_task(self, context, payload):
        id = payload['data']['data'][0]['GENERATED_KEY'] if payload['data']['data'] else None
        data = json.loads(payload['data']['config']['data'])['data'][0]
        task = self.mappings_of_task(data,id)
        return task

    def updated_task(self, context, payload):
        data = json.loads(payload['data']['config']['data'])
        task = self.mappings_of_task(data)
        return task

    def mappings_of_task(self,data, id=None):
        task_obj = ProjectslyTask(
            id=id if id else data.get('id'),
            name=data.get('name'),
            assigned_to=data.get('assignee_id'),
            project_id=data.get('project_id'),
            due_date=data.get('due_date'),
            priority_id=data.get('priority_id'),
            status_id=data.get('status_id'),
            group_id=data.get('group_id')
        ).__dict__
        return task_obj
