from unified.core.actions import Actions
from project_management.wrike import util
from project_management.wrike.entities.wrike_project import WrikeProject
from project_management.wrike.entities.wrike_task import WrikeTask
from project_management.wrike.entities.wrike_comment import WrikeComment
import json


class WrikeActions(Actions):

    def create_folder(self, context, folder_entity):
        ''' creates new folder'''

        access_token = util.get_access_token(context['headers'])
        folder_schema = WrikeProject(**folder_entity)
        folder_data = {
            "title": folder_schema.folder_name,
            "description": folder_schema.folder_description
        }
        url = f"https://www.wrike.com/api/v4/folders/{folder_schema.parent_folder_id}/folders"
        response = util.rest("POST", url, folder_data, access_token).text

        return json.loads(response)

    def create_task(self, context, task_entity):
        ''' creates new task'''

        access_token = util.get_access_token(context['headers'])
        task_schema = WrikeTask(**task_entity)
        task_data = {
            "title": task_schema.task_name,
            "description": task_schema.task_description

        }
        url = f"https://www.wrike.com/api/v4/folders/{task_schema.folder_id}/folders"
        response = util.rest("POST", url, task_data, access_token).text

        return json.loads(response)

    def add_a_comment_to_task(self, context, comment_entity):
        ''' adds new comment to task'''

        access_token = util.get_access_token(context['headers'])
        comment_schema = WrikeComment(**comment_entity)
        comment_data = {
            "title": comment_schema.comment_text

        }
        url = f"https://www.wrike.com/api/v4/folders/{comment_schema.folder_id}/folders"
        response = util.rest("POST", url, comment_data, access_token).text

        return json.loads(response)


