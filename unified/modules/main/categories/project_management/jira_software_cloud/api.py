from project_management.jira_software_cloud.entities.comment import JiraSoftwareCloudComment
from project_management.jira_software_cloud.entities.user import JiraSoftwareCloudUsers
from project_management.jira_software_cloud.entities.issue import JiraSoftwareCloudIssue
from project_management.jira_software_cloud import util
import json


class JiraSoftwareCloudApi:

    def comments(self, context, params):
        '''Get list of comments from a issue'''

        access_token = util.get_access_token(context['headers'])
        url = f'https://api.atlassian.com/ex/jira/{params["site_id"]}/rest/api/3/issue/{params["issue_id"]}/comment'
        comments_list = json.loads(
            util.rest("GET", url, access_token).text)['comments']

        comments = []
        for comment in comments_list:
            comment_obj = JiraSoftwareCloudComment(
                comment_id = comment.get('id'),
                comment_description = comment.get('body').get('content')[0].get('content')[0].get('text'),
                author_id = comment.get('author').get('accountId')
            )
            comments.append(comment_obj.__dict__)

        return json.dumps(comments)

    def user_by_email_or_name(self, context, params):
        '''Get user by email or name'''

        access_token = util.get_access_token(context['headers'])
        query = params.get("name") or params.get("email")
        url = f'https://api.atlassian.com/ex/jira/{params["site_id"]}/rest/api/2/user/viewissue/search?query={query}&projectKey={params["project_key"]}'
        users_list = json.loads(util.rest("GET", url, access_token).text)

        users = []
        for user in users_list:
            user_obj = JiraSoftwareCloudUsers(
                user_id = user.get('accountId'),
                email = user.get('emailAddress'),
                name = user.get('displayName'),
                is_active = user.get('active')
            )
            users.append(user_obj.__dict__)

        return json.dumps(users)

    def user(self, context, params):
        '''get information of specified user'''

        access_token = util.get_access_token(context['headers'])
        url = f'https://api.atlassian.com/ex/jira/{params["site_id"]}/rest/api/2/user?accountId={params["user_id"]}'
        user = json.loads(util.rest("GET", url, access_token).text)
        user_obj = JiraSoftwareCloudUsers(
            user_id = user.get('accountId'),
            email = user.get('emailAddress'),
            name = user.get('displayName'),
            is_active = user.get('active')
        )
        
        return user_obj.__dict__

    def issue_by_key(self, context, params):
        '''get information of specifed issue by key'''

        access_token = util.get_access_token(context['headers'])
        url = f'https://api.atlassian.com/ex/jira/{params["site_id"]}/rest/api/3/issue/{params["key"]}'
        payload = json.loads(util.rest("GET", url, access_token).text)
        issue = JiraSoftwareCloudIssue(
            issue_id = payload.get('id'),
            project_id = payload.get('fields').get('project').get('id'),
            assignee_id = payload.get('fields').get('assignee').get('accountId') if payload.get('fields').get('assignee') else None,
            priority_id = payload.get('fields').get('priority').get('id'),
            issuetype_id = payload.get('fields').get('issuetype').get('id'),
            description = payload.get('fields').get('summary')
        )

        return issue.__dict__

    def profile(self, context, payload):
        url = "https://api.atlassian.com/me"
        access_token = util.get_access_token(context['headers'])
        response = (util.rest("GET", url, access_token = access_token).json())
        profile = {
            'id':response['account_id'],
            'email':response['email'],
            'name':response['name']
        }
        return profile