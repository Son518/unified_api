from task_management.microsoft_to_do import util
from task_management.microsoft_to_do.entities.microsoft_to_do_create_task import  MicrosofttodoTask
import json

class MicrosofttodoApi:
     
    def task(self, context, params):
        '''Get tasks '''

        access_token = util.get_access_token(context['headers'])

        list_id = params.get("list_id")
        task_id = params.get("task_id") 
        url = f"https://graph.microsoft.com/v1.0/me/todo/lists/{list_id}/tasks/{task_id}"
        response = util.rest("GET", url, access_token)
        task = json.loads(response.text)
        task_obj = MicrosofttodoTask(
                                    task_id = task['id'],
                                    title = task['title'], 
                                    start_date = task['createdDateTime'],
                                    due_date = task['lastModifiedDateTime'],
                                    turn_reminder_on = task['isReminderOn'],
                                    importance = task['importance']
                                )                             
        return task_obj.__dict__