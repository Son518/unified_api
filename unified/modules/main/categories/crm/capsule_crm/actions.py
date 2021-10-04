from unified.core.actions import Actions
from crm.entities.deal import Deal
from crm.entities.task import Task
from crm.capsule_crm.entities.capsulecrm_account import CapsulecrmAccount
from crm.capsule_crm.entities.capsulecrm_contact import CapsulecrmContact
from crm.capsule_crm.entities.capsulecrm_case import CapsulecrmCase
from crm.capsule_crm.entities.capsulecrm_deal import CapsulecrmDeal
from crm.capsule_crm.entities.capsulecrm_task import CapsulecrmTask
from crm.capsule_crm.entities.capsulecrm_tag import CapsulecrmTag
from crm.capsule_crm.entities.capsulecrm_note import CapsulecrmNote
from crm.capsule_crm import util
import json


class CapsulecrmActions(Actions):

    def create_contact(self, context, payload):
        '''Creates a new Person.'''

        access_token = util.get_access_token(context['headers'])
        contact = CapsulecrmContact(**payload)
        url = "parties"
        request_body = {"party": {
            "type": "person",
            "firstName": contact.first_name,
            "lastName": contact.last_name,
            "title": contact.title,
            "jobTitle": contact.job_title,
            "addresses": [{
                    "city": contact.mailing_city,
                    "country": contact.mailing_country,
                    "street": contact.mailing_street,
                    "state": contact.mailing_state,
                    "zip": contact.mailing_zip
            }]}}

        if contact.business_phone:
            request_body["phoneNumbers"] = [
                {"type": "work", "number": contact.business_phone}]

        if contact.email:
            request_body["emailAddresses"] = [
                {"type": "work", "address": contact.email}]

        if contact.website:
            request_body["websites"] = [
                {"type": "Home", "address": contact.website, "service": "URL"}]

        if contact.tags:
            request_body["tags"] = [{"name": contact.tags}]

        address_obj = {k: v for k,
                       v in request_body['party']['addresses'][0].items() if v}

        if address_obj != {}:
            request_body['party']['addresses'][0] = address_obj
        else:
            request_body['party'].pop('addresses')

        respose_obj = util.rest("post", url, access_token, request_body)
        response = json.loads(respose_obj.text)

        if respose_obj.ok:
            response['id'] = response['party']['id']

        return json.dumps(response), respose_obj.status_code

    def create_deal(self, context, payload):
        '''Creates a deal'''

        return self.create_opportunity(context, payload)

    def create_opportunity(self, context, payload):
        '''Creates a new opportunity.'''

        access_token = util.get_access_token(context['headers'])
        deal = CapsulecrmDeal(**payload)
        url = "opportunities"
        request_body = {
            "opportunity": {
                "description": deal.description,
                "party": {
                    "id": int(deal.contact_id)
                },
                "milestone": int(deal.milestone_id),
                "value": {
                    "amount": int(deal.value) if deal.value else 0,
                    "currency": deal.currency_id if deal.currency_id else "INR"
                },
                "expectedCloseOn": deal.close_date,
                "name": deal.name
            }
        }

        if deal.payment_terms:
            request_body['durationBasis'] = deal.payment_terms

        if deal.probability:
            request_body["probability"] = deal.probability

        if deal.tags:
            request_body['tags'] = [{"name": deal.tags}]

        respose_obj = util.rest("post", url, access_token, request_body)
        response = json.loads(respose_obj.text)

        if respose_obj.ok:
            response['id'] = response['opportunity']['id']

        return json.dumps(response), respose_obj.status_code

    def create_organization(self, context, payload):
        '''Creates a new organization.'''

        access_token = util.get_access_token(context['headers'])
        organization = CapsulecrmAccount(**payload)
        url = "parties"
        request_body = {"party": {
            "type": "organisation",
            "name": organization.name,
            "addresses": [{
                    "city": organization.mailing_city,
                    "country": organization.mailing_country,
                    "street": organization.mailing_street,
                    "state": organization.mailing_state,
                    "zip": organization.mailing_zip
            }]
        }}

        if organization.phone:
            request_body["phoneNumbers"] = [
                {"type": "work", "number": organization.phone}]

        if organization.website:
            request_body["websites"] = [
                {"type": "Work", "address": organization.website, "service": "URL"}]

        if organization.email:
            request_body["emailAddresses"] = [
                {"type": "work", "address": organization.email}]

        if organization.tags:
            request_body["tags"] = [{"name": organization.tags}]

        address_obj = {k: v for k,
                       v in request_body['party']['addresses'][0].items() if v}

        if address_obj != {}:
            request_body['party']['addresses'][0] = address_obj
        else:
            request_body['party'].pop('addresses')

        respose_obj = util.rest("post", url, access_token, request_body)
        response = json.loads(respose_obj.text)

        if respose_obj.ok:
            response['id'] = response['party']['id']

        return json.dumps(response), respose_obj.status_code

    def create_task(self, context, payload):
        '''Creates a new task.'''

        access_token = util.get_access_token(context['headers'])
        task = CapsulecrmTask(**payload)
        activity = "tasks"
        request_body = {
            "task": {
                "description": task.description,
                "party": {
                    "id": int(task.owner_id)
                },
                "dueOn": task.due_date
            }
        }
        if task.category_id:
            request_body["category"]: {"name": task.category_id}

        respose_obj = util.rest("post", activity, access_token, request_body)
        response = json.loads(respose_obj.text)

        if respose_obj.ok:
            response['id'] = response['task']['id']

        return json.dumps(response), respose_obj.status_code

    def create_case(self, context, payload):
        '''Creates a new Case.'''

        access_token = util.get_access_token(context['headers'])
        case = CapsulecrmCase(**payload)
        activity = "kases"

        request_body = {"kase": {
            "description": case.description,
            "name": case.name
        }}

        if case.owner_id:
            request_body['kase']['owner'] = case.owner_id
        
        if case.contact_id:
            request_body['kase']["party"] = {"id": int(case.contact_id)}
        
        if case.tags:
            request_body['tags'] = [{"name": case.tags}]

        respose_obj = util.rest("post", activity, access_token, request_body)
        response = json.loads(respose_obj.text)

        if respose_obj.ok:
            response['id'] = response['kase']['id']

        return json.dumps(response), respose_obj.status_code

    def add_tag_to_contact(self, context, payload):
        '''Adds  tag to contact.'''

        access_token = util.get_access_token(context['headers'])
        tag = CapsulecrmTag(**payload)
        activity = f"parties/{tag.contact_id}"
        request_body = {"party": {"tags": [{"name": tag.tag}]}}

        respose_obj = util.rest("PUT", activity, access_token, request_body)
        response = json.loads(respose_obj.text)

        if respose_obj.ok:
            response['id'] = response['party']['id']

        return json.dumps(response), respose_obj.status_code

    def add_note_to_entry(self, context, payload):
        '''Adds note to entity.'''

        access_token = util.get_access_token(context['headers'])
        note = CapsulecrmNote(**payload)
        activity = 'entries'
        request_body = {
            "entry": {
                "type": "note",
                "content": note.note
            }}
        
        if note.entity_type == 'contact':
            request_body['entry']['party'] = { "id": int(note.entity_id) }
        
        if note.entity_type == 'case':
            request_body['entry']['kase'] = { "id": int(note.entity_id) }

        respose_obj = util.rest("POST", activity, access_token, request_body)
        response = json.loads(respose_obj.text)

        if respose_obj.ok:
            response['id'] = response['entry']['id']

        return json.dumps(response), respose_obj.status_code
