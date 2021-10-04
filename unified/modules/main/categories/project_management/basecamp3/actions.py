from basecampy3 import Basecamp3
from unified.core.actions import Actions
from project_management.basecamp3 import util
from project_management.entities.project import Project
from project_management.basecamp3.entities.basecamp3_tasklist import Basecamp3Tasklist
from project_management.basecamp3.entities.basecamp3_task import Basecamp3Task
from project_management.basecamp3.entities.basecamp3_comment import Basecamp3Comment
from project_management.basecamp3.entities.basecamp3_message import Basecamp3Message
from project_management.basecamp3.entities.basecamp3_schedule_entry import Basecamp3ScheduleEntry
from project_management.basecamp3.entities.basecamp3_document import Basecamp3Document

import json


class Basecamp3Actions(Actions):

    def create_project(self, context, project_entity):
        '''creates new projects'''

        bc3 = util.basecamp3_client(context['headers'])

        project_schema = Project(**project_entity)
        project_body = {
            "name": project_schema.project_name,
            "description": project_schema.project_description
        }

        # Api
        project = bc3.projects.create(**project_body)

        return project.__dict__['_values']
    
    def create_to_do_list(self,context,payload):
        '''creates new to do list '''

        return self.create_tasklist(context, payload)

    def create_tasklist(self, context, tasklist_entity):
        '''creates new tasklist '''

        bc3 = util.basecamp3_client(context['headers'])

        tasklist_entities = Basecamp3Tasklist(**tasklist_entity)

        tasklist = {
            "name": tasklist_entities.name,
            "description": tasklist_entities.description,
            "project": tasklist_entities.project_id,
            "todoset": tasklist_entities.todoset_id,
        }
        response = bc3.todolists.create(**tasklist)

        return response.__dict__['_values']
    
    def create_task(self,context,payload):
        '''creates new task '''

        return self.create_to_do(context, payload)

    def create_to_do(self, context, task_entities):
        '''creates new to do'''

        bc3 = util.basecamp3_client(context['headers'])

        task_entities = Basecamp3Task(**task_entities)

        task = {
            "content": task_entities.name,
            "description": task_entities.description,
            "todolist": task_entities.tasklist_id,
            "project": task_entities.project_id,
            "due_on": task_entities.due_date
        }
        if task_entities.assigned_to:
            task['assignee_ids'] = [task_entities.assigned_to]
        response = bc3.todos.create(**task)

        return response.__dict__['_values']
    
    def add_comment_in_to_do(self,context, comment_entity):
        '''adds new comment in todo '''

        comment_entity['task_id'] = comment_entity.get('todo_id')
        comment_entity.pop('todo_id', 'no todo_id found')
        return self.create_comment(context, comment_entity)

    def create_comment(self, context, comment_entity):
        '''creates comments'''
        
        access_token = util.get_access_token(context['headers'])

        comment_entities = Basecamp3Comment(**comment_entity)
        # NO support in SDk. Used Rest API
        url = f"https://3.basecampapi.com/{comment_entities.account_id}/buckets/{comment_entities.project_id}/recordings/{comment_entities.task_id}/comments.json"

        comment = {
            "content": comment_entities.comment_description
        }

        response = util.rest("POST", url, comment, access_token).text

        return response

    def create_message(self, context, message_entity):
        '''creates new message'''

        bc3 = util.basecamp3_client(context['headers'])

        message_entities = Basecamp3Message(**message_entity)

        message = {
            "project": message_entities.project_id,
            "board": message_entities.message_board_id,
            "subject": message_entities.subject,
            "content": message_entities.content,
            "status": message_entities.status
        }
        response = bc3.messages.create(**message)
        
        print(response)

        return response.__dict__['_values']

    def update_tasklist(self, context, tasklist_entity):
        '''updates new tasklist '''

        bc3 = util.basecamp3_client(context['headers'])

        tasklist_entities = Basecamp3Tasklist(**tasklist_entity)

        tasklist = {
            "todolist": tasklist_entities.id,
            "name": tasklist_entities.name,
            "description": tasklist_entities.description,
            "project": tasklist_entities.project_id,
        }
        response = bc3.todolists.update(**tasklist)

        return response.__dict__['_values']
    
    def create_schedule_entry(self,context,time_entry):
        '''creates new schedule entry '''

        return self.create_time_entry(context, time_entry)
    
    def create_time_entry(self, context, time_entry):
        '''creates new time entry '''

        access_token = util.get_access_token(context['headers'])
        time_entry = Basecamp3ScheduleEntry(**time_entry)
        url = f"https://3.basecampapi.com/{time_entry.account_id}/buckets/{time_entry.project_id}/schedules/{time_entry.schedule_id}/entries.json"

        time_entry_body = {
            "summary": time_entry.event_name,
            "description": time_entry.event_description,
            "participant_ids":[time_entry.participant_id],
            "starts_at": time_entry.start_date,
            "ends_at": time_entry.end_date
        }

        response = util.rest("POST", url, time_entry_body, access_token).text

        return response

    def create_document(self, context, document):
        '''creates new documents '''

        access_token = util.get_access_token(context['headers'])
        document = Basecamp3Document(**document)
        url = f"https://3.basecampapi.com/{document.account_id}/buckets/{document.project_id}/vaults/{document.folder_id}/documents.json"
        document_body = {
            "title": document.title,
            "content": document.content,
            "status": document.status
        }

        response = util.rest("POST", url, document_body, access_token).text

        return response
