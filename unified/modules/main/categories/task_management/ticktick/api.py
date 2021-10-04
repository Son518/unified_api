from task_management.ticktick import util
from task_management.ticktick.entities.ticktick_task import TicktickTask
import json

class TicktickApi:
     
    def task(self, context, params):
        '''Get tasks '''

        access_token = context["headers"]["access_token"]
        project_id = params.get("project_id")
        task_id = params.get("task_id") 
        endpoint = f"open/v1/project/{project_id}/task/{task_id}"
        response = json.loads(util.rest("GET", endpoint, access_token).text)
        task_obj = TicktickTask(
                                task_id=response.get('id'),
                                name=response.get('title'), 
                                content=response.get('content'),
                                start_date=response.get('startDate'),
                                due_date=response.get('dueDate'),
                                priority=response.get('priority'),
                                timezone=response.get('timeZone')
                            )                       
        return task_obj.__dict__