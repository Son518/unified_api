from unified.core.actions import Actions
from project_management.jira_software_cloud import util
from project_management.jira_software_cloud.entities.comment import JiraSoftwareCloudComment
from project_management.jira_software_cloud.entities.issue import JiraSoftwareCloudIssue


class JiraSoftwareCloudActions(Actions):

    def create_issue(self, context, payload):
        '''Creates a new issue.'''

        access_token = util.get_access_token(context['headers'])

        issue = JiraSoftwareCloudIssue(**payload)
        url = f'https://api.atlassian.com/ex/jira/{issue.site_id}/rest/api/3/issue'
        issue_body = {
            "fields": {
                "summary": issue.description,
                "project": {
                    "id": issue.project_id
                },
                "issuetype": {
                    "id": issue.issuetype_id
                },
                "assignee": {
                    "accountId": issue.assignee_id
                },
                "priority": {
                    "id": issue.priority_id
                }
            }
        }
        response = util.rest("POST", url, access_token, issue_body).text

        return response

    def update_issue(self, context, payload):
        '''Updates an existing issue.'''

        access_token = util.get_access_token(context['headers'])

        issue = JiraSoftwareCloudIssue(**payload)
        url = f'https://api.atlassian.com/ex/jira/{issue.site_id}/rest/api/3/issue/{issue.issue_id}'
        issue_body = {
            "fields": {
                "summary": issue.description,
                "project": {
                    "id": issue.project_id
                },
                "issuetype": {
                    "id": issue.issuetype_id
                },
                "assignee": {
                    "accountId": issue.assignee_id
                },
                "priority": {
                    "id": issue.priority_id
                }
            }
        }
        response = util.rest("PUT", url, access_token, issue_body).text

        return response

    def add_watcher(self, context, payload):
        '''Adds a new watcher to an issue.'''

        access_token = util.get_access_token(context['headers'])
        issue = JiraSoftwareCloudIssue(**payload)
        url = f'https://api.atlassian.com/ex/jira/{issue.site_id}/rest/api/3/issue/{issue.issue_id}/watchers'
        issue_body = issue.user_id
        response = util.rest("PUT", url, access_token, issue_body).text

        return response

    def add_comment(self, context, payload):
        '''Adds a new comment to an issue.'''

        access_token = util.get_access_token(context['headers'])
        comment = JiraSoftwareCloudComment(**payload)
        url = f'https://api.atlassian.com/ex/jira/{comment.site_id}/rest/api/3/issue/{comment.issue_id}/comment'
        comment_body = {
            "body": {
                "version": 1,
                "type": "doc",
                "content": [{
                        "type": "paragraph",
                        "content": [{
                                "type": "text",
                                "text": comment.comment_description,
                                "marks": [{
                                        "type": "strong"
                                }]
                        }]
                }]
            },
            "visibility": None
        }
        response = util.rest("POST", url, access_token, comment_body).text

        return response
