from unified.core.triggers import Triggers
from project_management.clickup.api import ClickupApi


class ClickupTriggers(Triggers):

    def new_folder(self, context, payload):
        '''triggers when new folder is added '''
        
        params = {
            'folder_id': payload['folder_id']
        }

        return ClickupApi().folder(context, params)

    def new_list(self, context, payload):  
        '''Triggers when new list is added.'''

        params = {
            'tasklist_id': payload['list_id']
        }

        return ClickupApi().tasklist(context, params)

    def new_task(self, context, payload):
        '''Triggers when a new task is added.'''

        params = {
            'task_id': payload['task_id']
        }

        return ClickupApi().task(context, params)

    def task_changes(self, context, payload):
        '''Triggers when a task changes.'''

        params = {
            'task_id': payload['task_id']
        }

        return ClickupApi().task(context, params)
