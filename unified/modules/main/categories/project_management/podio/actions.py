from project_management.podio import util
from project_management.podio.entities.podio_item import PodioItem
from project_management.podio.entities.podio_task import PodioTask
from project_management.podio.entities.podio_file import PodioFile
from project_management.podio.entities.podio_comment import PodioComment
from unified.core.actions import Actions
import json


class PodioActions(Actions):

    def create_task(self, context, task_entity):
        ''' creates new task'''

        task_schema = PodioTask(**task_entity)
        task_data = {
            "text": task_schema.text,
            "description": task_schema.description,
            "due_date": task_schema.due_on,
            "org_id": task_schema.organization_id,
            "labels": [task_schema.labels],
            "space_id": task_schema.workspace_id,
            "user_id": task_schema.responsible_user,
            "remainder": task_schema.remainder
        }

        podio_task = util.podio_oauth(context["headers"])
        response = podio_task.Task.create(task_data)

        return response

    def mark_task_as_complete(self, context, task_entity):
        ''' marks task as completed'''
    
        podio_task = util.podio_oauth(context["headers"])
        response = podio_task.Task.complete(task_entity["task_id"])

        return response

    def delete_task(self, context, task_entity):
        ''' deletes task'''
        
        podio_task = util.podio_oauth(context["headers"])
        response = podio_task.Task.delete(task_entity["task_id"])

        return response

    def update_item(self, context, item_entity):
        ''' updates item'''
        
        item_schema = PodioItem(**item_entity)
        item_data = {
            "fields": {
                "title": item_schema.title}
        }

        podio_item = util.podio_oauth(context["headers"])
        response = podio_item.Item.update(int(item_schema.item_id), item_data)

        return response

    def create_item(self, context, item_entity):
        ''' creates new item'''
        
        item_schema = PodioItem(**item_entity)
        item_data = {
            "fields": {
                "title": item_schema.title
            }
        }
        
        podio_item = util.podio_oauth(context["headers"])
        response = podio_item.Item.create(
            int(item_schema.application_id), item_data)

        return response

    def add_a_comment_to_task(self, context, comment_entity):
        ''' adds comment to task'''
        
        access_token = util.get_access_token(context["headers"])
        comment_schema = PodioComment(**comment_entity)
        url = f"https://api.podio.com/comment/task/{comment_schema.task_id}"
        
        comment_data = {
            "value": comment_schema.comment_text
        }

        response = util.rest("POST", url, json.dumps(
            comment_data), access_token).text
            
        return json.loads(response)
