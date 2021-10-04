from datetime import time
import json
from time_tracking.clockify import util
from time_tracking.clockify.entities.clockify_create_project import ClockifyProject
from time_tracking.clockify.entities.clockify_create_client import ClockifyClient
from time_tracking.clockify.entities.clockify_create_tag import ClockifyTag
from time_tracking.clockify.entities.clockify_create_task import ClockifyTask
from time_tracking.clockify.entities.clockify_create_time_entry import ClockifyTimeEntry

class ClockifyApi():

    def project_by_name(self, context, params):
        '''get project by name'''

        response = util.rest("GET","projects",{},context["headers"]["api_key"],params['workspace_id'],name=params['name']).text
        project = json.loads(response)[0]
        project_obj = ClockifyProject(
                                        client_id = project['clientId'],
                                        is_project_public = project['public'],
                                        is_project_billable = project['billable'],
                                        name = project['name'],
                                        workspace_id = project['workspaceId']
                                    )                             
        return project_obj.__dict__
    
    def client_by_name(self, context, params):
        '''get client by name'''
        
        response = util.rest("GET","client",{},context["headers"]["api_key"],params['workspace_id'],name=params['name']).text
        client = json.loads(response)[0]
        client_obj = ClockifyClient(
                                        id = client['id'], 
                                        archived = client['archived'],
                                        name = client['name'],
                                        workspace_id = client['workspaceId']
                                    )                                
        return client_obj.__dict__

    def task_by_name(self, context, params):
        '''get task by name'''
        
        response = util.rest("GET","task",{},context["headers"]["api_key"],params['workspace_id'],id=params['project_id'],name=params['name']).text
        task = json.loads(response)[0]
        task_obj = ClockifyTask(
                                    status = task['status'],
                                    id = task['id'],
                                    project_id = task['projectId'],
                                    name=task['name'],
                                    estimate = task['estimate'],
                                    billable = task['billable'],
                                
                                )                                
        return task_obj.__dict__
    
    def tag_by_name(self, context, params):
        '''get tag by name'''

        response = util.rest("GET","tag",{},context["headers"]["api_key"],params['workspace_id'],name=params['name']).text
        tag = json.loads(response)[0] 
        tag_obj = ClockifyTag(
                                id = tag['id'], 
                                archived = tag['archived'],
                                name = tag['name'],
                                workspace_id = tag['workspaceId']               
                            )                                
        return tag_obj.__dict__

    def time_entry(self, context, params):
        '''get time entry'''

        response = util.rest("GET","time",{},context["headers"]["api_key"],params['workspace_id'],params['user_id']).text
        time = json.loads(response)[0]
        time_obj = ClockifyTimeEntry( 
                                        start_datetime = time['timeInterval']['start'],
                                        end_datetime = time['timeInterval']['end'],
                                        description = time['description'],
                                        project_id = time['projectId'],
                                        id = time['id'],
                                        billable = time['billable'],
                                        workspace_id = time['workspaceId']
                                    )                                
        return time_obj.__dict__