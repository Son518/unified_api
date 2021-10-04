from unified.core.actions import Actions
from project_management.clickup import util
from project_management.entities.comment import Comment
from project_management.clickup.entities.clickup_time_tracked import ClikupTimeTracked
from project_management.clickup.entities.clickup_task import ClickupTask
from project_management.clickup.entities.clickup_folder import ClickupFolder
from project_management.clickup.entities.clikup_tasklist import ClickupTasklist
from project_management.clickup.entities.clickup_checklist import ClikupChecklist


class ClickupActions(Actions):

    def create_task(self, context, task_entity):
        '''Creates a new task'''

        task_entity = ClickupTask(**task_entity)

        url = f"https://api.clickup.com/api/v2/list/{task_entity.list_id}/task"

        clickup_task_body = {
            "name": task_entity.name,
            "assignees": [
                task_entity.assigned_to
            ],
            "due_date": task_entity.due_date,
            "description": task_entity.description,
            "tags": [
                task_entity.tag
            ],
            "priority": task_entity.priority,
            # "start_date_time": task_entity.start_date
        }

        response = util.rest("POST", url, clickup_task_body, context)

        return response.text, response.status_code

    def create_folder(self, context, payload):
        '''Creates a new folder'''

        folder_entity = ClickupFolder(**payload)

        url = f"https://api.clickup.com/api/v2/space/{folder_entity.space_id}/folder"

        clickup_folder_body = {
            "name": folder_entity.folder_name
        }
        response = util.rest("POST", url, clickup_folder_body, context)

        return response.text, response.status_code

    def create_list(self, context, payload):
        '''Creates a new list'''

        return self.create_tasklist(context, payload)

    def create_tasklist(self, context, payload):
        '''Creates a new list'''

        tasklist_entites = ClickupTasklist(**payload)

        url = f"https://api.clickup.com/api/v2/folder/{tasklist_entites.folder_id}/list"

        clickup_tasklist_body = {
            "name": tasklist_entites.name,
            "content": tasklist_entites.description,
            "due_date": tasklist_entites.due_date,
            "priority": tasklist_entites.priority,
            "assignee": tasklist_entites.assignee_to
        }
        response = util.rest("POST", url, clickup_tasklist_body, context)

        return response.text, response.status_code

    def update_task(self, context, payload):
        '''updates a task'''

        task_entity = ClickupTask(**payload)

        url = f"https://api.clickup.com/api/v2/task/{task_entity.task_id}"

        clickup_task_body = {
            "name": task_entity.name,
            "assignees": [
                task_entity.assigned_to
            ],
            "due_date": task_entity.due_date,
            "description": task_entity.description,
            "tags": [
                task_entity.tag
            ]
        }

        response = util.rest("PUT", url, clickup_task_body, context)

        return response.text, response.status_code

    def post_a_task_comment(self, context, payload):
        '''Post a comment to a task'''

        comment = Comment(**payload)

        url = f"https://api.clickup.com/api/v2/task/{comment.task_id}/comment"

        clickup_comment_body = {
            "comment_text": comment.comment_description
        }

        response = util.rest("POST", url, clickup_comment_body, context)

        return response.text, response.status_code

    def add_tag_to_task(self, context, payload):
        '''add tags a task'''

        task_entity = ClickupTask(**payload)

        url = f"https://api.clickup.com/api/v2/task/{task_entity.task_id}/tag/{task_entity.tag}/"

        response = util.rest("POST", url, context=context)

        return response.text, response.status_code

    def delete_task(self, context, payload):
        '''delete a task'''

        task_entity = ClickupTask(**payload)

        url = f"https://api.clickup.com/api/v2/task/{task_entity.task_id}/"

        response = util.rest(
            "DELETE", url, context=context)

        return response.text, response.status_code

    def create_subtask(self, context, payload):
        '''Creates a new subtask'''

        task_entity = ClickupTask(**payload)

        url = f"https://api.clickup.com/api/v2/list/{task_entity.list_id}/task"

        clickup_task_body = {
            "parent": task_entity.task_id,
            "name": task_entity.name,
            "assignees": [
                task_entity.assigned_to
            ],
            "due_date": task_entity.due_date,
            "description": task_entity.description,
            "tags": [
                task_entity.tag
            ],
            "priority": task_entity.priority,
        }

        response = util.rest("POST", url, clickup_task_body, context)

        return response.text, response.status_code

    def create_checklist(self, context, payload):
        '''Creates a new checklist in task'''

        checklist_entity = ClikupChecklist(**payload)

        url = f"https://api.clickup.com/api/v2/task/{checklist_entity.task_id}/checklist"

        clickup_checklist = {
            "name": checklist_entity.name
        }

        response = util.rest("POST", url, clickup_checklist, context)

        return response.text, response.status_code

    def time_tracked(self, context, payload):
        '''Add time tracked to a task'''

        timetracked_entity = ClikupTimeTracked(**payload)
        url = f"https://api.clickup.com/api/v2/task/{timetracked_entity.task_id}/time/"
        clickup_time_tracked = {
            "start": timetracked_entity.start_date,
            "end": timetracked_entity.due_date
        }
        response = util.rest("POST", url, clickup_time_tracked, context)

        return response.text, response.status_code
