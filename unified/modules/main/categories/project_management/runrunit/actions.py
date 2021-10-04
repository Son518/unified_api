from unified.core.actions import Actions
from project_management.runrunit import util
from project_management.runrunit.entities.create_project import RunrunitProject
from project_management.runrunit.entities.create_task import RunrunitTask
from project_management.runrunit.entities.create_client import RunrunitClient
from project_management.runrunit.entities.post_on_enterprise_wall import RunrunitPostOnEnterpriseWall
from project_management.runrunit.entities.post_on_team_wall import RunrunitPostOnTeamWall
import datetime
import json


class RunrunitActions(Actions):

    def create_client(self, context, payload):
        '''create a client'''

        headers = context["headers"]
        payload_data = RunrunitClient(**payload)

        body = {"client": {

            "is_visible": payload_data.visible,
            "name": payload_data.name
        }
        }
        response = util.rest("POST", "clients", headers, body)
        return json.loads(response.text)

    def create_project(self, context, payload):
        '''create a project'''

        headers = context["headers"]

        payload_data = RunrunitProject(**payload)

        body = {
            "project": {

                "client_id": payload_data.client_id,
                "name": payload_data.project_name
            }
        }
        response = util.rest("POST", "projects", headers, body)
        return json.loads(response.text)

    def create_task(self, context, payload):
        '''create a task'''

        headers = context["headers"]

        payload_data = RunrunitTask(**payload)

        body = {
            "task": {
                "desired_date": payload_data.end_date,
                "on_going": payload_data.on_going,
                "project_id": payload_data.project_id,
                "scheduled_start_time": payload_data.start_date,
                "title": payload_data.title,
                "type_id": payload_data.type_id,
                "assignments": [
                    {
                        "assignee_id": payload_data.assignee,
                        "team_id": payload_data.team_id
                    }
                ]
            }
        }
        response = util.rest("POST", "tasks", headers, body)

        return json.loads(response.text)
    
    
    def post_on_enterprise_wall(self, context, payload):
        '''create a enterprise wall'''

        headers = context["headers"]

        payload_data = RunrunitPostOnEnterpriseWall(**payload)

        body = {
             "text": payload_data.text
            }
        
        response = util.rest("POST", "posts/enterprise", headers, body)
        
        return json.loads(response.text)
    
    def post_on_team_wall(self, context, payload):
        '''create a team wall'''

        headers = context["headers"]

        payload_data = RunrunitPostOnTeamWall(**payload)

        body = {
             "text": payload_data.text
            }
        
        response = util.rest("POST", "posts/teams/"f"{payload_data.team_id}", headers, body)

        return json.loads(response.text)

