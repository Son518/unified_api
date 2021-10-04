import json
from project_management.redbooth import util
from project_management.redbooth.entities.redbooth_task import RedboothTask


class RedboothApi:
     
    def task(self, context, params):
        """ Create task"""

        access_token = util.get_authentication(context["headers"])
        id = params.get("task_id")
        response = util.rest("GET", f"tasks/{id}", access_token)
        response = json.loads(response.text)
        if response:
            data = RedboothTask(
                name= response["name"],
                project_id= response["project_id"],
                tasklist_id= response["task_list_id"],
                is_private= response["is_private"],
                description= response["description"],
                assignees= response["assigned_user_ids"],
                status= response["status"],
                due_on= response.get("due_on"),
                urgent= response["urgent"]
            )
        return data.__dict__

    def profile(self, context, params):
        """ Get Profile"""

        access_token = util.get_authentication(context["headers"])
        response = util.rest("GET", f"me", access_token)
        response = json.loads(response.text)
        if response:
            data = {
                "id": response["id"],
                "name": response["first_name"]+" "+response["last_name"],
                "email": response["email"]
            }
        return data