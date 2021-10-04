from task_management.microsoft_to_do import util
from unified.core.actions import Actions
from task_management.microsoft_to_do.entities.microsoft_to_do_create_list import MicrosofttodoList
from task_management.microsoft_to_do.entities.microsoft_to_do_create_task import MicrosofttodoTask
from task_management.microsoft_to_do.entities.microsoft_to_do_complete_task import MicrosofttodoCompleteTask
import json

class MicrosofttodoActions(Actions):

    def create_list(self, context, payload):
        '''creates a new list'''

        access_token = util.get_access_token(context['headers'])
        list_entity = MicrosofttodoList(**payload)
        data = {
                "displayName": list_entity.title
            }
        response = util.rest("POST", "", access_token, data)
        return json.loads(response.text) 

    def create_task(self, context, payload):
        '''creates a new task'''

        access_token = util.get_access_token(context['headers'])
        task_entity = MicrosofttodoTask(**payload) 
        list_id = task_entity.list_id
        data = {
                "title": task_entity.title,
                "list_id": task_entity.list_id,
                "note": task_entity.note,
                "createdDateTime": task_entity.start_date,
                "lastModifiedDateTime": task_entity.due_date,
                "reminderDateTime": task_entity.reminder_date,
                "isReminderOn": task_entity.turn_reminder_on,
                "importance": task_entity.importance
            }
        response = util.rest("POST",f"/{list_id}/tasks", access_token, data)
        return json.loads(response.text) 

    def complete_task(self, context, payload):
        '''completes a  task'''

        access_token = util.get_access_token(context['headers'])
        task_entity =MicrosofttodoCompleteTask(**payload)
        list_id = task_entity.list_id
        task_id = task_entity.task_id
        data = {
                "list_id": task_entity.list_id,
                "task_id": task_entity.task_id     
            }
        response = util.rest("PATCH",f"/{list_id}/tasks/{task_id}", access_token, data)
        return json.loads(response.text) 