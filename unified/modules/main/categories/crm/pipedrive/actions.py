from pipedrive.client import Client
from unified.core.actions import Actions
from crm.pipedrive.entities.pipedrive_lead import PipedriveCRMLead
from crm.pipedrive.entities.pipedrive_deal import PipedriveCRMDeal
from crm.pipedrive.entities.pipedrive_note import PipedriveCRMNote
from crm.pipedrive.entities.pipedrive_account import PipedriveCRMAccount
from crm.pipedrive.entities.pipedrive_activity import PipredriveCRMActivity
from crm.pipedrive.entities.pipedrive_person import PipedriveCRMPerson
from crm.pipedrive import util
import json
from flask import jsonify


class PipedriveActions(Actions):

    def create_deal(self, context, payload):
        """ Create Deal"""

        client = util.pipedrive_authentication(context["headers"])
        deal = PipedriveCRMDeal(**payload)
        deal_obj = {
            "title": deal.title,
            "person_id": deal.person_id,
            "status": deal.status,
            "probability": deal.probability,
            "value": deal.value,
            "currency": deal.currency,
            "visible_to": deal.visible_to
        }
        deal_obj = self.remove_empty(deal_obj)
        response = client.deals.create_deal(deal_obj)
        response["id"] = response["data"]["id"]
        return response

    def create_account(self, context, payload):
        """ Create account"""

        client = util.pipedrive_authentication(context["headers"])
        account = PipedriveCRMAccount(**payload)
        account_obj = {
            "name" : account.name,
            "owner_id" : account.owner_id,
            "address" : account.address,
            "visible_to": account.visible_to
        }
        account_obj = self.remove_empty(account_obj)
        response = client.organizations.create_organization(account_obj)
        response["id"] = response["data"]["id"]
        return response

    def create_organization(self, context, payload):
        """ Create Organization"""

        return self.create_account(context, payload)

    def create_lead(self, context, payload):
        """ Create lead"""

        lead = PipedriveCRMLead(**payload)

        # Convert person_id, owner_id and organization_id values into integer
        if lead.person_id is not None:
            lead.person_id = int(lead.person_id)
        if lead.organization_id is not None:
            lead.organization_id = int(lead.person_id)
        if lead.owner_id is not None:
            lead.owner_id = int(lead.person_id)
        
        lead_obj = {
            "title" : lead.title,
            "person_id" : lead.person_id,
            "organization_id": lead.organization_id,
            "owner_id" : lead.owner_id,
            "note" : lead.note
        }
        lead_obj = self.remove_empty(lead_obj)
        response = util.rest(f'https://{context["headers"]["domain"]}.pipedrive.com/v1/leads', context["headers"]["api_token"], "POST", lead_obj, "application/json")
        response = json.loads(response)
        if response["success"] is False:
            return {"Error":response["error"]}
        response["id"] = response["data"]["id"]
        return response

    def create_note(self, context, payload):
        """ Create note"""

        client = util.pipedrive_authentication(context["headers"])
        note = PipedriveCRMNote(**payload)
        note_obj = {
            "content": note.content,
            "person_id": note.person_id,
            "org_id": note.organization_id,
            "deal_id": note.deal_id,
            "lead_id": note.lead_id,
            "pinned_to_lead_flag": note.pin_note_on_specified_lead,
            "pinned_to_deal_flag": note.pin_note_on_specified_deal,
            "pinned_to_organization_flag": note.pin_note_on_specified_organization,
            "pinned_to_person_flag": note.pin_note_on_specified_person
        }
        note_obj = self.remove_empty(note_obj)
        response = client.notes.create_note(note_obj)
        response["id"] = response["data"]["id"]
        return response

    def update_deal(self, context, payload):
        """ Update deal"""

        client = util.pipedrive_authentication(context["headers"])
        deal = PipedriveCRMDeal(**payload)
        deal_obj = {
            "title": deal.title,
            "person_id": deal.person_id,
            "status": deal.status,
            "probability": deal.probability,
            "value": deal.value,
            "currency": deal.currency,
            "visible_to": deal.visible_to,
            "stage_id": deal.stage_id,
            "org_id": deal.organization_id
        }
        deal_obj = self.remove_empty(deal_obj)
        response = client.deals.update_deal(deal.deal_id, deal_obj)
        response["id"] = deal.deal_id
        return response

    def update_account(self, context, payload):
        """ Update account"""

        client = util.pipedrive_authentication(context["headers"])
        account = PipedriveCRMAccount(**payload)
        account_obj = {
            "name" : account.name,
            "owner_id" : account.owner_id,
            "address" : account.address,
            "visible_to": account.visible_to
        }
        account_obj = self.remove_empty(account_obj)
        response = client.organizations.update_organization(account.organization_id, account_obj)
        response["id"] = account.organization_id
        return response

    def update_organization(self, context, payload):
        """ Update Organization"""

        return self.update_account(context, payload)

    def create_activity(self, context, payload):
        """ Create activity"""

        client = util.pipedrive_authentication(context["headers"])
        activity = PipredriveCRMActivity(**payload)
        activity_obj = {
            "subject" : activity.subject,
            "type" : activity.type,
            "user_id" : activity.assign_to,
            "note": activity.note,
            "due_date" : activity.due_date,
            "duration" : activity.duration,
            "deal_id" : activity.deal_id,
            "person_id" : activity.person_id,
            "done" : activity.is_done
        }
        account_obj = self.remove_empty(activity_obj)
        response = client.activities.create_activity(account_obj)
        response["id"] = response["data"]["id"]
        return response

    def update_activity(self, context, payload):
        """ Update activity"""

        client = util.pipedrive_authentication(context["headers"])
        activity = PipredriveCRMActivity(**payload)
        activity_obj = {
            "subject" : activity.subject,
            "type" : activity.type,
            "user_id" : activity.assign_to,
            "note": activity.note,
            "due_date" : activity.due_date,
            "duration" : activity.duration,
            "deal_id" : activity.deal_id,
            "person_id" : activity.person_id,
            "done" : activity.is_done
        }
        account_obj = self.remove_empty(activity_obj)
        response = client.activities.update_activity(activity.activity_id, account_obj)
        response["id"] = activity.activity_id
        return response

    def create_person(self, context, payload):
        """ Update activity"""

        client = util.pipedrive_authentication(context["headers"])
        person = PipedriveCRMPerson(**payload)
        person_obj = {
            "name" : person.name,
            "org_id" : person.organization_id,
            "owner_id": person.owner_id,
            "email" : person.email,
            "phone" : person.phone,
            "visible_to" : person.visible_to
        }
        person_obj = self.remove_empty(person_obj)
        response = client.persons.create_person(person_obj)
        response["id"] = response["data"]["id"]
        return response

    def create_contact(self, context, payload):
        """ Create a contact"""

        return self.create_person(self, context, payload)

    def update_person(self, context, payload):
        """ Update activity"""

        client = util.pipedrive_authentication(context["headers"])
        person = PipedriveCRMPerson(**payload)
        person_obj = {
            "name" : person.name,
            "org_id" : person.organization_id,
            "owner_id": person.owner_id,
            "email" : person.email,
            "phone" : person.phone,
            "visible_to" : person.visible_to
        }
        person_obj = self.remove_empty(person_obj)
        response = client.persons.update_person(person.person_id, person_obj)
        response["id"] = response["data"]["id"]
        return response

    def update_contact(self, context, payload):
        """ Update a contact"""

        return self.update_person(self, context, payload)
        
    def remove_empty(self, dct):
        return {k: v for (k, v) in dct.items() if v is not None}   
