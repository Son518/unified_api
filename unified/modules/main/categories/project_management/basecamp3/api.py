from project_management.basecamp3 import util
from project_management.basecamp3.entities.basecamp3_project import Basecamp3Project
from project_management.basecamp3.entities.basecamp3_task import Basecamp3Task
from project_management.basecamp3.entities.basecamp3_message import Basecamp3Message
from project_management.basecamp3.entities.basecamp3_comment import Basecamp3Comment
from project_management.basecamp3.entities.basecamp3_user import Basecamp3User
from project_management.basecamp3.entities.basecamp3_schedule_entry import Basecamp3ScheduleEntry
from project_management.basecamp3.entities.basecamp3_tasklist import Basecamp3Tasklist
import json


class Basecamp3Api():

    def project(self, context, params):
        '''get project details'''

        bc3 = util.basecamp3_client(context['headers'])
        if 'project_id' not in params:
            raise KeyError('Required project_id not found')
        try:
            project = bc3.projects.get(
                params["project_id"]).__dict__['_values']
        except Exception as err:
            raise Exception(f'Provided project_id mismatch {err}')

        project_obj = Basecamp3Project(
            id=project["id"],
            project_name=project["name"],
            project_description=project["description"],
            status=project["status"],
            created_date=project["created_at"],
            updated_date=project["updated_at"],
            message_board_id=project["dock"][0]["id"],
            todoset_id=project["dock"][1]["id"],
            file_id=project["dock"][2]["id"],
            chat_id=project["dock"][3]["id"],
            schedule_id=project["dock"][4]["id"],
            questionnaire_id=project["dock"][5]["id"]
        )

        return project_obj.__dict__

    def projects(self, context, params):
        '''get list of projects'''
        bc3 = util.basecamp3_client(context['headers'])
        try:
            projects_list = bc3.projects.list()
        except Exception as err:
            raise Exception(f'please check headers {err}')

        projects = []
        for project in projects_list:
            project = project.__dict__['_values']

            project_obj = Basecamp3Project(
                id=project["id"],
                project_name=project["name"],
                project_description=project["description"],
                status=project["status"],
                created_date=project["created_at"],
                updated_date=project["updated_at"],
                message_board_id=project["dock"][0]["id"],
                todoset_id=project["dock"][1]["id"],
                file_id=project["dock"][2]["id"],
                chat_id=project["dock"][3]["id"],
                schedule_id=project["dock"][4]["id"],
                questionnaire_id=project["dock"][5]["id"]
            )

            projects.append(project_obj.__dict__)
        return json.dumps(projects)

    def projectbyname(self, context, params):
        '''project by name '''
        bc3 = util.basecamp3_client(context['headers'])

        if 'name' not in params:
            raise KeyError('Required project name not found')

        try:
            projects_list = bc3.projects.find(params['name'])
        except Exception as err:
            raise Exception(f'Provided project name mismatch {err}')

        projects = []

        for project in projects_list:
            project = project.__dict__['_values']
            project_obj = Basecamp3Project(
                id=project["id"],
                project_name=project["name"],
                project_description=project["description"],
                status=project["status"],
                created_date=project["created_at"],
                updated_date=project["updated_at"],
                message_board_id=project["dock"][0]["id"],
                todoset_id=project["dock"][1]["id"],
                file_id=project["dock"][2]["id"],
                chat_id=project["dock"][3]["id"],
                schedule_id=project["dock"][4]["id"],
                questionnaire_id=project["dock"][5]["id"]
            )

            projects.append(project_obj.__dict__)

        return json.dumps(projects)

    def todos(self, context, params):
        '''get list of todos'''

        bc3 = util.basecamp3_client(context['headers'])

        if 'todolist_id' not in params or 'project_id' not in params:
            raise KeyError('Required project_id or todolist_id not found')

        try:
            task_list = bc3.todos.list(
                todolist=params['todolist_id'], project=params["project_id"])
        except Exception as err:
            raise Exception(
                f'Provided project_id or todolist_id mismatch {err}')
        tasks = []

        for task in task_list:
            task = task.__dict__['_values']
            task_obj = Basecamp3Task(
                id=task["id"],
                description=task["description"],
                name=task["title"],
                project_id=task["bucket"]["id"],
                task_id=task["id"],
                assigned_to=task["assignees"][0]["id"],
                tasklist_id=task["parent"]["id"],
                created_date=task["created_at"],
                due_date=task["due_on"]
            )
            tasks.append(task_obj.__dict__)

        return json.dumps(tasks)

    def todo(self, context, params):
        '''get todo details'''

        bc3 = util.basecamp3_client(context['headers'])

        if 'project_id' not in params or 'todo_id' not in params:
            raise KeyError('Required project_id or todo_id not found')

        try:
            task = bc3.todos.get(
                project=params['project_id'], todoitem=params['todo_id']).__dict__['_values']
        except Exception as err:
            raise Exception(f'Provided project_id or mismatch {err}')

        task_obj = Basecamp3Task(
            id=task["id"],
            description=task["description"],
            name=task["title"],
            project_id=task["bucket"]["id"],
            task_id=task["id"],
            assigned_to=task["assignees"][0]["id"],
            tasklist_id=task["parent"]["id"],
            created_date=task["created_at"],
            due_date=task["due_on"]
        )

        return task_obj.__dict__

    def message(self, context, params):
        '''get message details'''

        bc3 = util.basecamp3_client(context['headers'])

        if 'message_id' not in params or 'project_id' not in params:
            raise KeyError('Required project_id or message_id not found')

        try:
            message_obj = bc3.messages.get(
                project=params["project_id"], message=params["message_id"]).__dict__['_values']
        except Exception as err:
            raise Exception(
                f'Provided project_id or message_id mismatch {err}')

        message = Basecamp3Message(
            project_id=message_obj["id"],
            message_board_id=message_obj["parent"]["id"],
            subject=message_obj["title"],
            content=message_obj["content"],
            status=message_obj["status"],
            created_date=message_obj["created_at"],
        )
        return message.__dict__

    def comment(self, context, params):
        '''get comment details '''

        access_token = util.get_access_token(context['headers'])
        if 'account_id' not in params or 'project_id' not in params or 'comment_id' not in params:
            raise KeyError(
                'Required account_id or project_id or comment_id not found')

        url = f"https://3.basecampapi.com/{params['account_id']}/buckets/{params['project_id']}/comments/{params['comment_id']}.json"

        response = util.rest("GET", url, access_token=access_token)
        comment_obj = json.loads(response.text)

        if response.status_code != 200:
            raise Exception(
                f'Something went wrong.Check ids provided {response.text}')

        comment = Basecamp3Comment(
            id=comment_obj["id"],
            comment_description=comment_obj["content"],
            task_id=comment_obj["parent"]["id"],
            project_id=comment_obj["bucket"]["id"],
            created_date=comment_obj["created_at"],
            comment_by=comment_obj["creator"]["id"]
        )

        return comment.__dict__

    def user(self, context, params):
        '''get user details'''

        bc3 = util.basecamp3_client(context['headers'])

        if 'user_id' not in params:
            raise KeyError('Required user_id not found')
        try:
            people_obj = bc3.people.get(params['user_id']).__dict__['_values']
        except Exception as err:
            raise Exception(f'Provided user_id mismatch {err}')

        people = Basecamp3User(
            id=people_obj['id'],
            first_name=people_obj['name'],
            email=people_obj['email_address'],
            avatar_url=people_obj['avatar_url'],
            account_id=people_obj['company']['id'],
            title=people_obj['title'],
            created_date=people_obj['created_at']

        )
        return people.__dict__

    def time_entry(self, context, params):
        '''get time enty details '''

        access_token = util.get_access_token(context['headers'])

        if 'account_id' not in params or 'project_id' not in params or 'schedule_id' not in params:
            raise KeyError(
                'Required account_id or project_id or schedule_id or not found')

        url = f"https://3.basecampapi.com/{params['account_id']}/buckets/{params['project_id']}/schedule_entries/{params['schedule_id']}.json"

        response = util.rest("GET", url, access_token=access_token)
        entry_object = json.loads(response.text)

        if response.status_code != 200:
            raise Exception(
                f'Something went wrong.Check ids provided {response.text}')

        schedule = Basecamp3ScheduleEntry(
            account_id=entry_object['creator']['company']['id'],
            start_date=entry_object['starts_at'],
            end_date=entry_object['ends_at'],
            id=entry_object["id"],
            event_name=entry_object["title"],
            event_description=entry_object["description"],
            schedule_id=entry_object["parent"]["id"],
            project_id=entry_object["bucket"]["id"],
            created_by=entry_object["creator"]["id"],
            created_date=entry_object["created_at"],
        )

        return schedule.__dict__

    def comments(self, context, params):
        '''get list of comments '''

        access_token = util.get_access_token(context['headers'])

        if 'account_id' not in params or 'project_id' not in params or 'task_id' not in params:
            raise KeyError(
                'Required project_id or task_id or account_id not found')

        url = f"https://3.basecampapi.com/{params['account_id']}/buckets/{params['project_id']}/recordings/{params['task_id']}/comments.json"

        response = util.rest("GET", url, access_token=access_token)
        comment_list = json.loads(response.text)

        if response.status_code != 200:
            raise Exception(
                f'Something went wrong.Check ids provided {response.text}')

        comments = []

        for comment_obj in comment_list:
            comment = Basecamp3Comment(
                account_id=comment_obj['creator']['company']['id'],
                id=comment_obj["id"],
                comment_description=comment_obj["content"],
                task_id=comment_obj["parent"]["id"],
                project_id=comment_obj["bucket"]["id"],
                created_date=comment_obj["created_at"],
                comment_by=comment_obj["creator"]["id"]
            )
            comments.append(comment.__dict__)

        return json.dumps(comments)

    def users(self, context, params):
        '''get list of users from your project'''

        bc3 = util.basecamp3_client(context['headers'])
        if 'project_id' not in params:
            raise KeyError('Required project_id not found')

        try:
            people_list = bc3.people.list(params['project_id'])
        except Exception as err:
            raise Exception(
                f'Something went wrong,check with ids provided {err}')
        users = []

        for people in people_list:

            people_obj = people.__dict__['_values']

            people = Basecamp3User(
                id=people_obj['id'],
                first_name=people_obj['name'],
                email=people_obj['email_address'],
                avatar_url=people_obj['avatar_url'],
                account_id=people_obj['company']['id'],
                title=people_obj['title'],
                created_date=people_obj['created_at']
            )
            users.append(people.__dict__)

        return json.dumps(users)

    def to_do_list(self, context, params):
        '''get to do list details'''

        bc3 = util.basecamp3_client(context['headers'])
        if 'project_id' not in params or 'todo_list_id' not in params:
            raise KeyError('Required project_id not found')

        try:
            todolist_get = bc3.todolists.get(
                params['todo_list_id'], project=params['project_id'])
        except Exception as err:
            raise Exception(
                f'Something went wrong,check with ids provided {err}')

        todolist_obj = todolist_get.__dict__['_values']
        todolist = Basecamp3Tasklist(
            id=todolist_obj.get('id'),
            name=todolist_obj.get('title'),
            description=todolist_obj.get('description'),
            project_id=todolist_obj.get('bucket').get('id'),
            todoset_id=todolist_obj.get('parent').get('id')
        )

        return todolist.__dict__

    def profile(self, context, payload):
        '''Details of authenticated user'''

        url = "https://launchpad.37signals.com/authorization.json"
        access_token = util.get_access_token(context['headers'])
        response = util.rest("GET", url, access_token=access_token).json()
        response = response['identity']
        profile = {
            'email':response['email_address'],
            'id':response['id'],
            'name':response['first_name']
        }
        return profile
        
