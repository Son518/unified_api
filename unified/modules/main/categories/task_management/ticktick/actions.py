import json
from requests.models import Response
from core.actions import Actions
from task_management.ticktick import util
from task_management.ticktick.entities.ticktick_task import TicktickTask

class TicktickActions(Actions):
    
    def add_task(self, context, payload):
        """
        Add new task
        context holds the headers 
        payload holds the request.body
        """
        access_token = context["headers"]["access_token"]
        task_entity = TicktickTask(**payload)
        endpoint = "open/v1/task"
        data = {
                "list_id": task_entity.list_id,
                "title": task_entity.name,
                "content": task_entity.content,
                "startDate": task_entity.start_date,
                "dueDate": task_entity.due_date,
                "priority": int(task_entity.priority),
                "timeZone": task_entity.timezone,
                "file": task_entity.file
            }
        response = util.rest("POST",endpoint,access_token,data)
        return json.loads(response.text)