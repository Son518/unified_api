# from dataclasses import asdict
import asana
import json

from project_management.entities.attachment import Attachment
from project_management.entities.comment import Comment
from project_management.entities.user import User
from project_management.entities.tag import Tag
from project_management.entities.workspace import Workspace
from project_management.entities.tasklist import Tasklist
from project_management.asana.entities.asana_task import AsanaTask
from project_management.asana.entities.asana_attachment import AsanaAttachment
from project_management.asana.entities.asana_project import AsanaProject
from project_management.asana.entities.asana_tag import AsanaTag
from project_management.asana import util

class AsanaApi():

    def tasks_by_project_id(self,context,params):
        '''get list of task by project id''' 
        
        return self.tasks(context, params)

    def tasks(self, context, params):
        '''get list of task in project'''

        asana_client = util.get_asana_client(context['headers'])

        if params.get("project_id"):
            task_data = asana_client.tasks.get_tasks(
                opt_pretty = True, project = params["project_id"])
        else:
            task_data = asana_client.tasks.get_tasks(
                opt_pretty = True, tag = params["tag_id"])

        tasks = []
        for task in task_data:
            asana_task = AsanaTask(
                id = task["gid"],
                name = task["name"]
            )
            tasks.append(asana_task.__dict__)
        return json.dumps(tasks)

    def projects(self, context, params):
        '''get list of projects by workspace'''

        asana_client = util.get_asana_client(context['headers'])

        project_data = asana_client.projects.get_projects_for_workspace(
            params["workspace_id"], opt_pretty=False)

        projects = []
        for project in project_data:
            asana_project = AsanaProject(
                id = project['gid'],
                project_name = project['name']
            )

            projects.append(asana_project.__dict__)

        return json.dumps(projects)
    
    def section(self, context, params):
        '''get section data'''

        return self.tasklist(context, params)
    
    def tasklist(self, context, params):   
        '''get specified tasklist data in your project '''

        tasklist_id = params.get('tasklist_id') or params.get('section_id')
        asana_client = util.get_asana_client(context['headers'])
        result = asana_client.sections.get_section(tasklist_id, opt_pretty=False)
        asana_tasklist = Tasklist(
                id = result['gid'],
                name = result['name'],
                project_id = result.get('project').get('gid') if result.get('project') else None 
            )        
        return asana_tasklist.__dict__

    def sections(self,context,params):
        '''get list of  sections in project'''

        return self.tasklists(context, params)

    def tasklists(self, context, params):       
        '''get list of  tasklist in project'''

        asana_client = util.get_asana_client(context['headers'])
        result = asana_client.sections.get_sections_for_project(params["project_id"], opt_pretty=False)
        tasklists=[]
        for tasklist in result:
            asana_tasklist=Tasklist(
                id = tasklist['gid'],
                name = tasklist['name']
            )
            tasklists.append(asana_tasklist.__dict__)
        
        return json.dumps(tasklists)
   
    def user(self, context, params):
        '''get user details'''
        asana_client = util.get_asana_client(context['headers'])
        result = asana_client.users.get_user(params['user_id'], opt_pretty=False)
        asana_user = User(
                avatar_url=result.get('photo'),
                email=result.get('email'),
                id = result['gid'],
                first_name = result['name']
            )
        
        return asana_user.__dict__

    def users(self, context, params):
        '''get list of users in a workspace'''

        asana_client = util.get_asana_client(context['headers'])
        if params.get('workspace_id'):
            result = asana_client.users.get_users_for_workspace(params['workspace_id'], opt_pretty=False)
        else:
            result = asana_client.users.get_users_for_team(params['team_id'], opt_pretty=False)
        users=[]
        for user in result:
            asana_user = User(
                id = user['gid'],
                first_name = user['name']
            )
            users.append(asana_user.__dict__)

        return json.dumps(users)
    
    def tags(self, context, params):
        '''get list of tags from workspace or tags'''

        asana_client = util.get_asana_client(context['headers'])
        # specified to workspace 
        if params.get('workspace_id'):
            result = asana_client.tags.get_tags(opt_pretty=True,workspace=params['workspace_id'])
         # specified to a single task
        else:
            result = asana_client.tags.get_tags_for_task(params['task_id'],opt_pretty=False)

        tags=[]
        for tag in result:
            asana_tag= Tag(
                id = tag['gid'],
                name = tag['name']
            )
            tags.append(asana_tag.__dict__)

        return json.dumps(tags)

    def workspace(self, context, params):
        '''get workspace data'''

        asana_client = util.get_asana_client(context['headers'])
        # Api
        result = asana_client.workspaces.get_workspace(params['workspace_id'],opt_pretty=False)
        asana_workspace = Workspace(
            id = result['gid'],
            name = result['name']
        )     
        return asana_workspace.__dict__

    def workspaces(self, context, params):
        '''get list of workpace'''
        asana_client = util.get_asana_client(context['headers'])
        # Api
        result = asana_client.workspaces.get_workspaces(opt_pretty=False)
        
        workspaces=[]
        for workspace in result:
            asana_workspace = Workspace(
                id = workspace['gid'],
                name = workspace['name']
            )
            workspaces.append(asana_workspace.__dict__)
             
        return json.dumps(workspaces)
    
    def subtasks(self, context, params):
        '''get list of subtasks'''

        asana_client = util.get_asana_client(context['headers'])
        # Api 
        result = asana_client.tasks.get_subtasks_for_task(params['task_id'], opt_pretty=False)

        subtasks = []
        for task in result:
            asana_subtask = AsanaTask(
                id = task["gid"],
                name = task["name"]
            )
            subtasks.append(asana_subtask.__dict__)

        return json.dumps(subtasks)
    
    def attachment(self, context, params):
        '''get  attachment details'''

        asana_client = util.get_asana_client(context['headers'])
        result = asana_client.attachments.get_attachment(params['attachment_id'], opt_pretty=False)
        asana_attachment = AsanaAttachment(
                download_url= result.get('download_url'),
                task_id=result.get('parent').get("gid") if result.get('parent') else None,
                task_name=result.get('parent').get("name") if result.get('parent') else None,
                permanent_url= result.get('permanent_url'),
                id = result['gid'],
                name = result['name']
            )

        return asana_attachment.__dict__

    def attachments(self, context, params):
        '''get list of attachments from a task'''

        asana_client = util.get_asana_client(context['headers'])
        result = asana_client.attachments.get_attachments_for_task(params['task_id'], opt_pretty=False)
        attachments=[]
        for attachment in result:
            asana_attachment = Attachment(
                id = attachment['gid'],
                name = attachment['name']
            )
            attachments.append(asana_attachment.__dict__)
        
        return json.dumps(attachments)

    def task(self, context, params):
        '''get task details'''

        asana_client = util.get_asana_client(context['headers'])

        result = asana_client.tasks.get_task(
            params['task_id'], opt_pretty=True)

        asana_task = AsanaTask(
            id = result["gid"],
            name = result["name"],
            description = result["notes"],
            project_id = result['projects'][0]['gid'],
            due_date = result['due_on'],
            assigned_to = result['assignee']['gid']
        )

        return asana_task.__dict__

    def create_webhook(self, context, payload):
        '''create a webhook in workspace'''

        asana_client = util.get_asana_client(context['headers'])

        result = asana_client.webhooks.create_webhook(payload, opt_pretty=True)
        return result, 200

    def project(self, context, params):
        '''get project details'''

        asana_client = util.get_asana_client(context['headers'])

        result = asana_client.projects.get_project(
            params['project_id'], opt_pretty=False)

        asana_project = AsanaProject(
            id = result['gid'],
            project_name = result['name'],
            project_description = result['notes'],
            end_date = result['due_date'],
            created_date = result['created_at'],
            updated_date = result['modified_at'],
            default_view = result['default_view'],
            team = result['team']['gid'],
            followers = result['followers'],
            is_template = result['is_template'],
            owner = result['owner']['gid']
        )
        # __dict__ in dataclass gives the dict with fields and their values
        return asana_project.__dict__

    def tag(self, context, params):
        '''get specified tag details'''

        asana_client = util.get_asana_client(context['headers'])

        result = asana_client.tags.get_tag(params['tag_id'], opt_pretty=False)

        asana_tag = AsanaTag(
            id = result['gid'],
            name = result['name'],
            notes = result['notes'],
            created_date = result['created_at'],
            color = result['color'],
            followers = result['followers'],
            workspace_id = result['workspace']['gid'],
            workspace_name = result['workspace']['name']
        )

        return asana_tag.__dict__
    
    def comment(self, context, params):
        '''get comment details'''

        asana_client = util.get_asana_client(context['headers'])
        result = asana_client.stories.get_story(
            params['comment_id'], opt_pretty=False)
        comment = Comment(
            id = result['gid'],
            comment_description = result['text'],
            task_id = result['target']['gid'],
            comment_by = result['created_by']['gid']
        )
        return comment.__dict__
        
    def task_stories(self, context, params):
        '''get list of task stories of task '''

        return self.comments(context, params)

    def comments(self, context, params):
        '''get list of comment from task'''
        
        asana_client = util.get_asana_client(context['headers'])
        comments_list = asana_client.stories.get_stories_for_task(
            params['task_id'], opt_pretty=False)
        comments=[]
        for comment_obj in comments_list:
            comment = Comment(
            id = comment_obj['gid'],
            comment_description = comment_obj['text'],
            comment_by = comment_obj['created_by']['gid']
            )
            comments.append(comment.__dict__)
        return json.dumps(comments)
    
    def profile(self, context, params):
        '''Details of authenticated user'''
        asana_client = util.get_asana_client(context['headers'])
        response = asana_client.users.me()
        profile = {
            'id':response['gid'],
            'email':response['email'],
            'name':response['name']
        }
        return profile
        