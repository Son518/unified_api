import json
from project_management.teamwork.entities.teamwork_task import TeamworkTask
from project_management.teamwork.entities.teamwork_project import TeamworkProject
from project_management.teamwork.entities.teamwork_comment import TeamworkComment
from project_management.teamwork.entities.teamwork_milestone import TeamworkMilestone
from project_management.teamwork.entities.teamwork_timeentry import TeamworkTimeentry
from project_management.teamwork.entities.teamwork_column import TeamworkColumn
from project_management.teamwork import util
from unified.core.actions import Actions


class TeamworkActions(Actions):

    def create_task(self, context, task_entities):
        ''' creates a new task  '''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        task_schema = TeamworkTask(**task_entities)

        url = f"https://{domain_name}.teamwork.com/tasklists/{task_schema.tasklist_id}/tasks.json"
        task_data = {
            "todo-item": {
                "content": task_schema.task_name,
                "tasklistId": task_schema.tasklist_id,
                "description": task_schema.task_description,
                "start_date": task_schema.start_date,
                "due_date": task_schema.due_date,
                "tags": task_schema.tag
            }
        }

        response = util.rest("POST", url, json.dumps(
            task_data), access_token).text
        return json.loads(response)

    def create_project(self, context, project_entities):
        ''' creates a new project '''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        project_schema = TeamworkProject(**project_entities)
        url = f"https://{domain_name}.teamwork.com/projects.json"

        project_data = {
            "project": {
                "name": project_schema.project_name,
                "description": project_schema.project_description,
                "start_date": project_schema.start_date,
                "due_date": project_schema.due_date,
                "company_id": project_schema.company_id,
                "category_id": project_schema.category_id,
                "project_owner_id": project_schema.owner_id,
                "tags": project_schema.tags
            }
        }

        response = util.rest("POST", url, json.dumps(
            project_data), access_token).text
        return json.loads(response)

    def add_a_comment_to_task(self, context, comment_entities):
        '''creates a new comment to task '''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        comment_schema = TeamworkComment(**comment_entities)
        url = f"https://{domain_name}.teamwork.com/tasks/{comment_schema.task_id}/comments.json"

        comment_data = {
            "comment": {
                "body": comment_schema.comment_description,
                "notify": comment_schema.notify,
                "isprivate": comment_schema.private,
                "content-type": comment_schema.content_type if comment_schema.content_type else 'Text'
            }
        }

        headers = context["headers"]
        response = json.loads(util.rest("POST", url, json.dumps(
            comment_data), access_token).text)
        return response

    def create_subtask(self, context, subtask_entities):
        ''' creates a new sub task '''
        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        subtask_schema = TeamworkTask(**subtask_entities)
        url = f"https://{domain_name}.teamwork.com/tasks/{subtask_schema.task_id}.json"

        subtask_data = {
            "todo-item": {
                "content": subtask_schema.subtask_name,
                "description": subtask_schema.subtask_description,
                "startDate": subtask_schema.start_date,
                "dueDate": subtask_schema.due_date,
            }
        }

        headers = context["headers"]
        response = util.rest("POST", url, json.dumps(
            subtask_data), access_token).text
        return json.loads(response)

    def create_milestone(self, context, milestone_entities):
        ''' creates a new milestone '''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        milestone_schema = TeamworkMilestone(**milestone_entities)
        url = f"https://{domain_name}.teamwork.com/projects/{milestone_schema.project_id}/milestones.json"

        milestone_data = {
            "milestone": {
                "title": milestone_schema.title,
                "deadline": milestone_schema.end_date,
                "responsible-party-id": milestone_schema.responsible_party_id
            }
        }
        headers = context["headers"]
        response = util.rest("POST", url, json.dumps(
            milestone_data), access_token).text
        return json.loads(response)

    def mark_task_complete(self, context, mark_task_complete_entities):
        ''' marks task as completed '''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])

        mark_task_complete_schema = TeamworkTask(**mark_task_complete_entities)
        url = f"https://{domain_name}.teamwork.com/tasks/{mark_task_complete_schema.task_id}/complete.json"

        response = util.rest("PUT", url, {}, access_token).text
        return json.loads(response)

    def update_project(self, context, update_project_entities):
        ''' updates the project new values'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        update_project_schema = TeamworkProject(**update_project_entities)
        url = f"https://{domain_name}.teamwork.com/projects/{update_project_schema.id}.json"

        update_project_data = {
            "project": {
                "name": update_project_schema.project_name,
                "content": update_project_schema.content,
                "description": update_project_schema.project_description
            }
        }

        response = util.rest("PUT", url, json.dumps(
            update_project_data), access_token).text
        return json.loads(response)

    def update_task(self, context, update_task_entities):
        ''' updates task with new values'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        update_task_schema = TeamworkTask(**update_task_entities)
        url = f"https://{domain_name}.teamwork.com/tasks/{update_task_schema.task_id}.json"

        update_task_data = {
            "todo-item": {
                "content": update_task_schema.content,
                "description": update_task_schema.description,
                "tasklist-id": update_task_schema.tasklist_id,
                "taskId": update_task_schema.task_id
            }
        }

        response = util.rest("PUT", url, json.dumps(
            update_task_data), access_token).text
        return json.loads(response)

    def create_column(self, context, column_entities):
        ''' creates new column '''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        column_schema = TeamworkColumn(**column_entities)
        url = f"https://{domain_name}.teamwork.com/projects/{column_schema.project_id}/boards/columns.json"

        column_data = {
            "column": {
                "name": column_schema.column_name,
                "color": column_schema.color
            }
        }

        response = util.rest("POST", url, json.dumps(
            column_data), access_token).text
        return json.loads(response)

    def create_timesheet_entry(self, context, timesheet_entities):
        ''' creates new time sheet entry'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        timesheet_schema = TeamworkTimeentry(**timesheet_entities)
        url = f"https://{domain_name}.teamwork.com/projects/{timesheet_schema.project_id}/time_entries.json"

        timesheet_data = {
            "time-entry": {
                "date": timesheet_schema.date,
                "description": timesheet_schema.description,
                "hours": timesheet_schema.hours
            }
        }
        
        response = util.rest("POST", url, json.dumps(
            timesheet_data), access_token).text
        return json.loads(response)

    def create_tasklist(self, context, tasklist_entity):
        ''' creates new task list '''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        tasklist_schema = TeamworkTask(**tasklist_entity)
        url = f"https://{domain_name}.teamwork.com/projects/{tasklist_schema.project_id}/tasklists.json"

        tasklist_data = {
            "todo-list": {
                "tasklist_name": tasklist_schema.tasklist_name,
                "private": tasklist_schema.private,
                "content": tasklist_schema.content,
                "description": tasklist_schema.tasklist_description,
                "start-date-offset": tasklist_schema.start_date,
                "due-date-offset": tasklist_schema.due_date
            }
        }

        response = util.rest("POST", url, json.dumps(
            tasklist_data), access_token).text
        return json.loads(response)
