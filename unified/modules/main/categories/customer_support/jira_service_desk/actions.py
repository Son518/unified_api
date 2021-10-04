import json 

from unified.core.actions import Actions
from customer_support.jira_service_desk import util
from customer_support.jira_service_desk.entities.jira_service_desk_request import JiraservicedeskRequest



class JiraservicedeskActions(Actions):

    def create_request(self, context, payload):
        """Creates a new issue."""

        request_entity = JiraservicedeskRequest(**payload)
        request_data = {
            "serviceDeskId": request_entity.service_desk_id,
            "requestTypeId": request_entity.type_id,
            "requestFieldValues" : {
                "summary": request_entity.summary,
                "description": request_entity.description,
            }
        }

        url = util.get_url(request_entity.site_id, 'request')
        access_token = util.get_access_token(context['headers'])
        response = util.rest("POST", url, access_token, request_data)

        return json.loads(response.text)
