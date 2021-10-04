from unified.core.triggers import Triggers
from project_management.jira_software_cloud.entities.issue import JiraSoftwareCloudIssue


class JiraSoftwareCloudTriggers(Triggers):

    def new_issue(self, context, payload):
        '''Triggers when a new issue is created.'''

        issue = JiraSoftwareCloudIssue(
            issue_id = payload.get('issue').get('id'),
            project_id = payload.get('issue').get('fields').get('project').get('id'),
            assignee_id = payload.get('issue').get('fields').get('assignee').get('accountId') if payload.get('issue').get('fields').get('assignee') else None,
            priority_id = payload.get('issue').get('fields').get('priority').get('id'),
            issuetype_id = payload.get('issue').get('fields').get('issuetype').get('id'),
            description = payload.get('issue').get('fields').get('summary')
        )

        return issue.__dict__

    def issue_updated(self, context, payload):
        '''Triggers when an existing issue is updated.'''

        issue = JiraSoftwareCloudIssue(
            issue_id = payload.get('issue').get('id'),
            project_id = payload.get('issue').get('fields').get('project').get('id'),
            assignee_id = payload.get('issue').get('fields').get('assignee').get('accountId') if payload.get('issue').get('fields').get('assignee') else None,
            priority_id = payload.get('issue').get('fields').get('priority').get('id'),
            issuetype_id = payload.get('issue').get('fields').get('issuetype').get('id'),
            description = payload.get('issue').get('fields').get('summary')
        )
        
        return issue.__dict__
