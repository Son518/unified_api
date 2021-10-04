from unified.core.triggers import Triggers
from customer_support.jira_service_desk import util
from customer_support.jira_service_desk.entities.jira_service_desk_request import JiraservicedeskRequest

class JiraservicedeskTriggers:

    def new_request(self, context, payload):
        """New request created."""

        fields = payload['fields']
        request_entity = JiraservicedeskRequest(
            id = payload['id'],
            project_id = fields['project']['id'],
            type_id = fields['issuetype']['id'],
            summary = fields['summary'],
            description = fields['description']
        )

        return request_entity.__dict__


    def updated_request(self, context, payload):
        """Existing request updated."""

        fields = payload['fields']
        request_entity = JiraservicedeskRequest(
            id = payload['id'],
            project_id = fields['project']['id'],
            type_id = fields['issuetype']['id'],
            summary = fields['summary'],
            description = fields['description']
        )

        return request_entity.__dict__
