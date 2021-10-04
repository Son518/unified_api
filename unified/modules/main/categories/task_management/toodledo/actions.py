import json
from unified.core.actions import Actions
from task_management.toodledo import util
from task_management.toodledo.entities.toodledo_folder import ToodledoFolder
from task_management.toodledo.entities.toodledo_note import ToodledoNote
from task_management.toodledo.entities.toodledo_task import ToodledoTask


class ToodledoActions(Actions):

    def create_folder(self, context, payload):
        """
        creates a folder 
        context holds the headers 
        payloads holds the request.body  
        """
        access_token = util.get_access_token(context["headers"])
        endpoint = "folders/add.php"
        folder_entity = ToodledoFolder(**payload)
        data = {
            "name": folder_entity.name,
            "private": folder_entity.private
        }
        response = util.rest("POST", endpoint, access_token, data)
        if type(json.loads(response.text)) == list:
            return json.loads(response.text)[0]
        elif type(json.loads(response.text)) == dict:
            return json.loads(response.text)

    def create_note(self, context, payload):
        """
        creates a notes 
        context holds the headers 
        payloads holds the request.body  
        """
        access_token = util.get_access_token(context["headers"])
        endpoint = "notes/add.php"
        note_entity = ToodledoNote(**payload)
        notes = [
            {
                "folder": note_entity.folder_id,
                "title": note_entity.note_title,
                "private": note_entity.private,
                "text": note_entity.note_text
            }
        ]
        data = {"notes": json.dumps(notes)}
        response = util.rest("POST", endpoint, access_token, data)
        return json.loads(response.text)[0]

    def create_task(self, context, payload):
        """
        creates a tasks 
        context holds the headers 
        payloads holds the request.body  
        """
        endpoint = "tasks/add.php"
        access_token = util.get_access_token(context["headers"])
        task_entity = ToodledoTask(**payload)
        tasks = [
            {
                "ref": task_entity.folder_id,
                "title": task_entity.name,
                "context_id": task_entity.context_id,
                "priority": task_entity.priority,
                "star": task_entity.starred_task,
                "note": task_entity.Note,
                "status": task_entity.status,
                "tags": task_entity.tags
            }
        ]
        data = {"tasks": json.dumps(tasks)}
        response = util.rest("POST", endpoint, access_token, data)
        return json.loads(response.text)[0]
