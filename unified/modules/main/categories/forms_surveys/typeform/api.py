# from unified.core.api import Api

from typeform import Typeform
import json

from unified.core.actions import Actions
from forms_surveys.entities.form import Form
from . import util

class TypeformApi:

    def form(self, context, payload):
        """Get a form, with given 'id of the form"""

        typeform = Typeform(context['headers']['api_key'])

        resp = typeform.forms.get(payload['id'])

        return resp


    def forms(self, context, payload):
        """Get a list of forms, with given 'workspace_id' of the workspace. 'limit' is maximum items to list."""

        typeform = Typeform(context['headers']['api_key'])

        params = {
            'workspaceId': payload['workspace_id'],
            'pageSize': int(payload.get('limit'))
        }

        resp = typeform.forms.list(**params)

        return resp

    def lookup_response(self, context, payload):
        """Get list of responses for the form with given form_id"""

        responses = Typeform(context['headers']['api_key']).responses

        params = {
            'uid': payload['form_id'],
        }

        if payload.get('limit'):
            params['pageSize'] = int(payload['limit'])

        if payload.get('submitted_since'):
            params['since'] = int(payload['submitted_since'][:10])

        if payload.get('submitted_until'):
            params['until'] = int(payload['submitted_until'][:10])

        if (c := payload.get('response_completed')) is not None:
            params['completed'] = (c.lower() not in ['no', 'false', '0', ''])

        return responses.list(**params)

    def webhook(self, context, payload):
        """Get details of a webhook for the form with given form_id and tag"""

        return self.webhooks(context, payload)


    def webhooks(self, context, payload):
        """Get details of webhooks for the form with given form_id"""

        url = f"{util.TYPEFORM_BASE_URL}/forms/{payload['form_id']}/webhooks"

        if 'tag' in payload:
            url = f"{url}/{payload['tag']}"

        resp = util.rest('GET', url, token=context['headers']['api_key'])

        return json.loads(resp.text), resp.status_code
