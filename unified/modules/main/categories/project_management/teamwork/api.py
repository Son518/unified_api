import json
from project_management.teamwork.entities.teamwork_task import TeamworkTask
from project_management.teamwork.entities.teamwork_project import TeamworkProject
from project_management.teamwork.entities.teamwork_comment import TeamworkComment
from project_management.teamwork.entities.teamwork_message import TeamworkMessage
from project_management.teamwork.entities.teamwork_user import TeamworkUser
from project_management.teamwork.entities.teamwork_timeentry import TeamworkTimeentry
from project_management.teamwork import util


class TeamworkApi():

    def project(self, context, params):
        ''' gets project by project id'''

        domain = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain}.teamwork.com/projects/{params['project_id']}.json"
        project = json.loads(util.rest("GET", url, {}, access_token).text)
        project_value = project.get('project') or {}
        
        project_obj = TeamworkProject(
            id=project_value.get('id'),
            project_name=project_value.get('name'),
            project_description=project_value.get('description'),
            status=project_value.get('status'),
            start_date=project_value.get('startDate'),
            end_date=project_value.get('endDate'),
            tags=project_value.get('tags'),
            created_date=project_value.get('created-on'),
            company_id=(project_value.get('company')).get('id'),
            category_id=(project_value.get('category')).get('id')
        )     
        return project_obj.__dict__

    def task(self, context, params):
        ''' gets tasks by task id'''

        domain = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain}.teamwork.com/tasks/{params['task_id']}.json"
        task = json.loads(util.rest("GET", url, {}, access_token).text)
        task_value = task.get('todo-item') or {}

        task_obj = TeamworkTask(
            task_id=task_value.get('id'),
            name=task_value.get('name'),
            description=task_value.get('description'),
            start_date=task_value.get('created-on'),
            end_date=task_value.get('completed_on'),
            tags=task_value.get('tags'),
            priority=task_value.get('priority'),
            avatar=task_value.get('creator-avatar-url')
        )
        return task_obj.__dict__

    def comment(self, context, params):
        ''' gets comment by comment id'''

        domain = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain}.teamwork.com/comments/{params['comment_id']}.json"
        comment = json.loads(util.rest("GET", url, {}, access_token).text)
        comment_value = comment.get('comment') or {}

        comment_obj = TeamworkComment(
            comment_id=comment_value.get('id'),
            comment_description=comment_value.get('body'),
            body=comment_value.get('html-body'),
            project_id=comment_value.get('project-id'),
            avatar=comment_value.get('author-avatar-url'),
            created_date=comment_value.get('datetime'),
            updated_after_date=comment_value.get('last-changed-on')
        )
        return comment_obj.__dict__

    def message(self, context, params):
        ''' gets message by message by id'''

        domain = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain}.teamwork.com/posts/{params['message_id']}.json"

        message = json.loads(util.rest("GET", url, {}, access_token).text)
        message_value = message.get('post') or {}
        message_obj = TeamworkMessage(
            message_id=message_value.get('id'),
            description=message_value.get('body'),
            tags=message_value.get('tags'),
            body=message_value.get('display-body'),
            project_id=message_value.get('project-id'),
            avatar=message_value.get('author-avatar-url')
        )
        return message_obj.__dict__

    def tasks(self, context, params):
        ''' gets all tasks '''

        domain = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain}.teamwork.com/tasks.json"
        tasks_list = json.loads(util.rest("GET", url, {}, access_token).text)

        tasks = []
        task_value = tasks_list.get('todo-items') or {}
        for task in task_value:
            task_obj = TeamworkTask(
                task_id=task.get('id'),
                name=task.get('todo-list-name'),
                description=task.get('description'),
                project_id=task.get('project-id'),
                avatar=task.get('creator-avatar-url'),
                start_date=task.get('start-date') or None,
                due_date=task.get('due-date') or None,
                status=task.get('status'),
                progress=task.get('progress'),
                estimated_minutes=task.get('estimated-minutes'),
                content=task.get('content'),
                date_created=task.get('created-on')
            )
            tasks.append(task_obj.__dict__)
        return json.dumps(tasks)

    def tasks_by_project_id(self, context, params):
        '''gets all tasks by project id'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain_name}.teamwork.com/projects/{params['project_id']}/tasks.json"

        tasks_list = json.loads(util.rest("GET", url, {}, access_token).text)
        tasks = []
        task_value = tasks_list.get('todo-items') or {}
        for task in task_value:
            task_obj = TeamworkTask(
                task_id=task.get('id'),
                description=task.get('description'),
                project_id=task.get('project-id'),
                avatar=task.get('creator-avatar-url'),
                start_date=task.get('start-date') or None,
                due_date=task.get('due-date') or None,
                status=task.get('status'),
                progress=task.get('progress'),
                estimated_minutes=task.get('estimated-minutes'),
                name=task.get('content'),
                date_created=task.get('created-on')
            )
            tasks.append(task_obj.__dict__)
        return json.dumps(tasks)

    def projects(self, context, params):
        ''' gets all projects'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain_name}.teamwork.com/projects.json"
        projects_list = json.loads(
            util.rest("GET", url, {}, access_token).text)

        projects = []
        project_value = projects_list.get('projects') or {}
        for project in project_value:
            project_obj = TeamworkProject(
                id=project.get('id'),
                project_name=project.get('name'),
                project_description=project.get('description'),
                status=project.get('status'),
                start_date=project.get('startDate') or None,
                end_date=project.get('endDate') or None,
                tags=project.get('tags'),
                created_date=project.get('created-on'),
                company_id=(project.get('company')).get('id'),
                category_id=(project.get('category')).get('id')
            )
            projects.append(project_obj.__dict__)
        return json.dumps(projects)

    def task_comments(self, context, params):
        ''' gets all task comments'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain_name}.teamwork.com/comments.json"
        comments_list = json.loads(
            util.rest("GET", url, {}, access_token).text)

        comments = []
        comments_value = comments_list.get('comments') or {}
        for comment in comments_value:
            comment_obj = TeamworkComment(
                comment_id=comment.get('id'),
                comment_description=comment.get('body'),
                body=comment.get('html-body'),
                project_id=comment.get('project-id'),
                avatar=comment.get('author-avatar-url'),
                created_date=comment.get('datetime'),
                updated_after_date=comment.get('last-changed-on')
            )
            comments.append(comment_obj.__dict__)
        return json.dumps(comments)

    def users(self, context, params):
        '''gets all users'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain_name}.teamwork.com/people.json"
        user = json.loads(util.rest("GET", url, {}, access_token).text)

        users = []
        users_value = user.get('people') or {}
        for user in users_value:
            user_obj = TeamworkUser(
                avatar_url=user.get('avatar-url'),
                people_id=user.get('id'),
                email=user.get('email-address'),
                first_name=user.get('first-name')
            )
            users.append(user_obj.__dict__)
        return json.dumps(users)

    def user(self, context, params):
        ''' gets user by user id'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain_name}.teamwork.com/people/{params['user_id']}.json"
        user = json.loads(util.rest("GET", url, {}, access_token).text)

        user_value = user.get("person") or {}
        user_obj = TeamworkUser(
            avatar_url=user_value.get('avatar-url'),
            people_id=user_value.get('id'),
            email=user_value.get('email-address'),
            first_name=user_value.get('first-name')
        )
        return user_obj.__dict__

    def time_entry(self, context, params):
        ''' gets time entry for task'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain_name}.teamwork.com/time_entries/{params['time_entries_id']}.json"
        time_entry = json.loads(util.rest("GET", url, {}, access_token).text)

        time_entry_value = time_entry.get('time-entry') or {}
        time_entry_obj = TeamworkTimeentry(
            hours=time_entry_value.get('hours'),
            date=time_entry_value.get('date'),
            description=time_entry_value.get('description'),
            time_entries_id=time_entry_value.get('id'),
            minutes=time_entry_value.get('minutes'),
            project_id=time_entry_value.get('project-id'),
            created_date=time_entry_value.get('createdAt'),
            updated_date=time_entry_value.get('updated-date'),
            task_id=time_entry_value.get('todo-item-id'),
            name=time_entry_value.get('todo-item-name')
        )
        return time_entry_obj.__dict__

    def projects_by_created_time(self, context, params):
        ''' gets projects by created time'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        start_date_time = util.epoch_to_format("%Y-%m-%d",params["start_date_time"])
        url = f"https://{domain_name}.teamwork.com/projects.json?createdAfterDate={start_date_time}&orderMode=asc&orderby=name&pageSize=500&status=active"

        projects_list = json.loads(
            util.rest("GET", url, {}, access_token).text)
        project_value = projects_list.get('projects') or {}
        projects = []
        for project in project_value:
            project_obj = TeamworkProject(
                id=project.get('id'),
                project_name=project.get('name'),
                project_description=project.get('description'),
                status=project.get('status'),
                start_date=project.get('startDate') or None,
                end_date=project.get('endDate') or None,
                tags=project.get('tags'),
                created_date=project.get('created-on'),
                company_id=(project.get('company')).get('id'),
                category_id=(project.get('category')).get('id'),
                avatar=project.get('avatar-url'),
            
            )
            projects.append(project_obj.__dict__)
        return json.dumps(projects)

    def tasks_by_created_time(self, context, params):
        ''' gets tasks by created time'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        start_date_time = util.epoch_to_format("%Y-%m-%d",params["start_date_time"])
        url = f"https://{domain_name}.teamwork.com/tasks.json?createdAfterDate={start_date_time}"

        tasks_list = json.loads(util.rest("GET", url, {}, access_token).text)
        tasks = []
        task_value = tasks_list.get('todo-items') or {}
        for task in task_value:
            task_obj = TeamworkTask(
                task_id=task.get('id'),
                name=task.get('todo-list-name'),
                description=task.get('description'),
                project_id=task.get('project-id'),
                avatar=task.get('creator-avatar-url'),
                start_date=task.get('start-date') or None,
                due_date=task.get('due-date') or None,
                status=task.get('status'),
                progress=task.get('progress'),
                estimated_minutes=task.get('estimated-minutes'),
                content=task.get('content'),
                date_created=task.get('created-on')
            )
            tasks.append(task_obj.__dict__)
        return json.dumps(tasks)

    def task_comments_by_created_time(self, context, params):
        ''' gets task comments by created time'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        start_date_time = util.epoch_to_format("%Y-%m-%d",params["start_date_time"])
        url = f"https://{domain_name}.teamwork.com/comments.json?createdAfterDate={start_date_time}"
        comments_list = json.loads(
            util.rest("GET", url, {}, access_token).text)

        comments = []
        comments_value = comments_list.get('comments') or {}
        for comment in comments_value:
            comment_obj = TeamworkComment(
                comment_id=comment.get('id'),
                comment_description=comment.get('body'),
                body=comment.get('html-body'),
                project_id=comment.get('project-id'),
                avatar=comment.get('author-avatar-url'),
                created_date=comment.get('datetime'),
                updated_after_date=comment.get('last-changed-on')
            )
            comments.append(comment_obj.__dict__)
        return json.dumps(comments)

    def projects_by_updated_time(self, context, params):
        ''' gets projects by updated time'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        start_date_time = util.epoch_to_format("%Y-%m-%d",params["start_date_time"])

        url = f"https://{domain_name}.teamwork.com/projects.json?orderMode=asc&orderby=name&pageSize=500&status=active&updatedAfterDate={start_date_time}"
        projects_list = json.loads(
            util.rest("GET", url, {}, access_token).text)
        project_value = projects_list.get('projects') or {}
        projects = []
        for project in project_value:
            project_obj = TeamworkProject(
                id=project.get('id'),
                project_name=project.get('name'),
                project_description=project.get('description'),
                status=project.get('status'),
                start_date=project.get('startDate') or None,
                end_date=project.get('endDate') or None,
                tags=project.get('tags'),
                created_date=project.get('created-on'),
                company_id=(project.get('company')).get('id'),
                category_id=(project.get('category')).get('id'),
                avatar=project.get('avatar-url')
            )
            projects.append(project_obj.__dict__)
        return json.dumps(projects_list)

    def tasks_by_updated_time(self, context, params):
        ''' gets tasks by updated time'''

        domain_name = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        start_date_time = util.epoch_to_format("%Y-%m-%d",params["start_date_time"])

        url = f"https://{domain_name}.teamwork.com/tasks.json?updatedAfterDate={start_date_time}"
        tasks_list = json.loads(util.rest("GET", url, {}, access_token).text)
        tasks = []
        task_value = tasks_list.get('todo-items') or {}
        for task in task_value:
            task_obj = TeamworkTask(
                task_id=task.get('id'),
                name=task.get('todo-list-name'),
                description=task.get('description'),
                project_id=task.get('project-id'),
                avatar=task.get('creator-avatar-url'),
                start_date=task.get('start-date') or None,
                due_date=task.get('due-date') or None,
                status=task.get('status'),
                progress=task.get('progress'),
                estimated_minutes=task.get('estimated-minutes'),
                content=task.get('content'),
                date_created=task.get('created-on')
            )
            tasks.append(task_obj.__dict__)
        return json.dumps(tasks)

    def verify(self, context, params):
        """
        get call to verify user authenticated information
        """
        domain = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain}.teamwork.com/people.json"
        response = util.rest("GET", url, {}, access_token)
        return response.json()

    def profile(self,context,params):
        """
        get call to show user authenticated information
        """
        domain = context["headers"]["domain"]
        access_token = util.get_basic_token(context["headers"])
        url = f"https://{domain}.teamwork.com/account.json"
        response = util.rest("GET", url, {}, access_token)
        if not response.ok:
            return {'status':'invalid details'}, response.status_code
        result = response.json()
        profile = {
            'id':result['account']['id'],
            'email':result['account']['siteOwnerEmail'],
            'name':result['account']['siteOwnerName']
        }
        return profile