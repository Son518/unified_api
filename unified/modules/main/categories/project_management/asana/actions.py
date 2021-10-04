# AsanaActions.py extends core/actions/Actionsd

import asana

from project_management.asana import util
from project_management.asana.entities.asana_task import AsanaTask
from project_management.asana.entities.asana_project import AsanaProject
from project_management.entities.comment import Comment
from project_management.entities.task import Task
from unified.core.actions import Actions


class AsanaActions(Actions):

    def create_task(self, context, task_entity):
        '''Adds a new task.'''

        asana_client = util.get_asana_client(context['headers'])
        task_schema = AsanaTask(**task_entity)
        task_data = {
            "priority": task_schema.priority,
            "due_on": task_schema.due_date,
            "name": task_schema.name,
            "projects": [task_schema.project_id],
            "assignee": task_schema.assigned_to,
            "resource_subtype": "default_task"
        }
        if task_schema.description:
            task_data['notes'] = task_schema.description

        if task_schema.tag:
            task_data['tags'] = [task_schema.tag]

        result = asana_client.tasks.create_task(task_data, opt_pretty=False)

        return result

    def create_project(self, context, project_entity):
        '''Adds a new project'''

        asana_client = util.get_asana_client(context['headers'])
        project_schema = AsanaProject(**project_entity)
        project_data = {
            "name": project_schema.project_name,
            "notes": project_schema.project_description,
            "team": project_schema.team
            # "is_template": project_schema.is_template,
            # "followers": project_schema.followers,
            # "options": {
            #     "pretty": "true",
            #     "fields": ["followers"]
            # }
            # "start_on": project_schema.start_date
        }

        if project_schema.end_date:
            project_data['due_on'] = project_schema.end_date

        if project_schema.owner:
            project_data['owner'] = project_schema.owner

        if project_schema.public:
            project_data['public'] = project_schema.public

        if project_schema.default_view:
            project_data['default_view'] = project_schema.default_view

        result = asana_client.projects.create_project(
            project_data, opt_pretty=False)

        return result

    def create_comment(self, context, comment_entity):
        '''Adds a new comment in task.'''

        asana_client = util.get_asana_client(context['headers'])

        comment_schema = Comment(**comment_entity)

        comment_data = {
            "text": comment_schema.comment_description
        }

        result = asana_client.stories.create_story_for_task(
            comment_schema.task_id, comment_data, opt_pretty=False)

        return result

    def create_subtask(self, context, subtask_entity):
        '''Adds a new subtask in task'''

        asana_client = util.get_asana_client(context['headers'])

        subtask_schema = AsanaTask(**subtask_entity)

        task_data = {
            "due_on": subtask_schema.due_date,
            "name": subtask_schema.name,
            "assignee": subtask_schema.assigned_to,
            "resource_subtype": "default_task"
        }

        if subtask_schema.description:
            task_data['notes'] = subtask_schema.description

        result = asana_client.tasks.create_subtask_for_task(
            subtask_schema.task_id, task_data, opt_pretty=False)

        return result

    def update_task(self, context, task_entity):
        '''Updates an existing Task.'''

        asana_client = util.get_asana_client(context['headers'])

        task_schema = AsanaTask(**task_entity)

        task_data = {
            "due_on": task_schema.due_date,
            "name": task_schema.name,
            "assignee": task_schema.assigned_to,
            "completed": task_schema.task_completed,
            "resource_subtype": "default_task"
        }
        if task_schema.description:
            task_data['notes'] = task_schema.description

        result = asana_client.tasks.update_task(
            task_schema.task_id, task_data, opt_pretty=False)

        return result

    def add_task_to_section(self, context, task_entity):
        '''Adds a task to a section of a project'''

        asana_client = util.get_asana_client(context['headers'])

        task_schema = AsanaTask(**task_entity)

        task_data = {
            "task": task_schema.task_id
        }
        result = asana_client.sections.add_task_for_section(
            task_schema.section_id, task_data, opt_pretty=False)

        return result

    def update_project(self, context, payload):
        '''updates a projects'''

        asana_client = util.get_asana_client(context['headers'])
        project_schema = AsanaProject(**project_entity)
        project_data = {
            "name": project_schema.project_name,
            "notes": project_schema.project_description,
            "team": project_schema.team
        }

        if project_schema.end_date:
            project_data['due_on'] = project_schema.end_date

        if project_schema.owner:
            project_data['owner'] = project_schema.owner

        if project_schema.public:
            project_data['public'] = project_schema.public

        if project_schema.default_view:
            project_data['default_view'] = project_schema.default_view

        result = asana_client.projects.update_project(project_schema.id,
                                                      project_data, opt_pretty=False)

        return result
