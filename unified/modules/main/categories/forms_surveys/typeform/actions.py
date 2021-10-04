from typeform import Typeform, Client
import json

from unified.core.actions import Actions
from forms_surveys.entities.form import Form
from forms_surveys.typeform.api import TypeformApi

from . import util

class TypeformActions(Actions):
    # def forms(self, context, payload):
    #     if method == 'POST':
    #         create_form
    #     elif method == 'GET':
    #         get_forms/forms_list
    #     elif method == 'PUT'
    #         update_form
    #     elif METHOD == 'DELETE??'
    #         delete_form


    def create_form(self, context, payload):
        """Create a new form with title in payload"""
        typeform = Typeform(context['headers']['api_key'])

        form_entity = Form(**payload)
        form_data = {
            "title": form_entity.title,
        }

        resp = typeform.forms.create(form_data)

        return resp


    def duplicate_form(self, context, payload):        
        """Duplicate a form completely with given form id"""

        form_data = TypeformApi().form(context, payload)

        form_data.pop('_links', None)
        form_data.pop('id', None)
        form_data['thankyou_screens'][0].pop('id', None)

        form_data = util.remove_field(form_data, 'id')

        ## This supports ONLY one field 'title', which is based on payloads
        ## which in trun is based on Zapier
        ## resp = typeform.forms.create(form_data)

        url = f"{util.TYPEFORM_BASE_URL}/forms"
        resp = util.rest('POST', url, form_data, context['headers']['api_key'])

        return json.loads(resp.text), resp.status_code


    def delete_form(self, context, payload):
        """Delete a from with given id"""

        typeform = Typeform(context['headers']['api_key'])

        resp = typeform.forms.delete(payload['id'])

        return {'result': resp}


    def create_webhook(self, context, payload):
        """Create a webhook for the form with given form_id and tag for given url"""
       
        webhook_payload = {
            'url': payload['url'],
            'enabled': payload['enabled'],
        }

        url = f"{util.TYPEFORM_BASE_URL}/forms/{payload['form_id']}/webhooks/{payload['tag']}"

        resp = util.rest('PUT', url, webhook_payload, context['headers']['api_key'])

        return json.loads(resp.text), resp.status_code


    def delete_webhook(self, context, payload):
        """Delete a webhook with given form_id and tag"""
        
        url = f"{util.TYPEFORM_BASE_URL}/forms/{payload['form_id']}/webhooks/{payload['tag']}"

        resp = util.rest('DELETE', url, token=context['headers']['api_key'])

        return {'result': 'deleted' if resp.status_code == 204 else 'error'}, resp.status_code
