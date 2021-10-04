from unified.core.triggers import Triggers
from pipedrive.client import Client
from crm.pipedrive.entities.pipedrive_lead import PipedriveCRMLead
from crm.pipedrive.entities.pipedrive_deal import PipedriveCRMDeal
from crm.pipedrive.entities.pipedrive_note import PipedriveCRMNote
from crm.pipedrive.entities.pipedrive_account import PipedriveCRMAccount
from crm.pipedrive.entities.pipedrive_activity import PipredriveCRMActivity
from crm.pipedrive.entities.pipedrive_person import PipedriveCRMPerson
import json


class PipedriveTriggers(Triggers):

    def new_contact(self, context, payload):
        """ Create new contact"""

        contact = PipedriveCRMPerson(
            contact_id= payload["current"]["id"],
            email= payload["current"]["email"][0]["value"],
            name=  payload["current"]["name"],
            owner_id=  payload["current"]["owner_id"],
            organization_id= payload["current"]["org_id"],
            phone= payload["current"]["phone"][0]["value"],
        )
        return contact.__dict__

    def new_person(self, context, payload):
        """ Create new person"""

        return self.new_contact(context, payload)

    def new_deal(self, context, payload):
        """ Triggers when a new deal is added"""

        deal = PipedriveCRMDeal(
            title= payload["current"]["title"],
            expected_close_date= payload["current"]["expected_close_date"],
            person_id= payload["current"]["person_id"],
            status= payload["current"]["status"],
            currency= payload["current"]["currency"],
            visible_to= payload["current"]["visible_to"],
            organization_id= payload["current"]["org_id"],
            deal_id= payload["current"]["id"],
            stage_id= payload["current"]["stage_id"],
            value= payload["current"]["value"],
            probability= payload["current"]["probability"]
        )
        return deal.__dict__

    def new_note(self, context, payload):
        """ Create a new lead"""

        note = PipedriveCRMNote(            
            note_id= payload["current"]["id"],
            content= payload["current"]["content"],
            deal_id= payload["current"]["deal_id"],
            pin_note_on_specified_deal= payload["current"]["pinned_to_deal_flag"],
            organization_id= payload["current"]["org_id"],
            pin_note_on_specified_organization= payload["current"]["pinned_to_organization_flag"],
            person_id= payload["current"]["person_id"],
            pin_note_on_specified_person= payload["current"]["pinned_to_person_flag"],
            lead_id= payload["current"]["lead_id"],
            pin_note_on_specified_lead= payload["current"]["pinned_to_lead_flag"]
        )
        return note.__dict__

    def updated_contact(self, context, payload):
        """ Update a contact"""

        contact = PipedriveCRMPerson(
            contact_id= payload["current"]["id"],
            email= payload["current"]["email"][0]["value"],
            organization_id= payload["current"]["org_id"],
            name= payload["current"]["name"],
            visible_to= payload["current"]["visible_to"],
            phone= payload["current"]["phone"][0]["value"],
            person_id= payload["current"]["id"],
            last_name= payload["current"]["last_name"],
            first_name= payload["current"]["first_name"]
        )
        return contact.__dict__

    def updated_deal(self, context, payload):
        """ Update a deal"""

        deal = PipedriveCRMDeal(
            title= payload["current"]["title"],
            expected_close_date= payload["current"]["expected_close_date"],
            person_id= payload["current"]["person_id"],
            status= payload["current"]["status"],
            currency= payload["current"]["currency"],
            visible_to= payload["current"]["visible_to"],
            organization_id= payload["current"]["org_id"],
            deal_id= payload["current"]["id"],
            stage_id= payload["current"]["stage_id"],
            value= payload["current"]["value"],
            probability= payload["current"]["probability"]
        )
        return deal.__dict__
        
    def update_note(self, context, payload):
        """ Update Note"""
        
        note = PipedriveCRMNote(            
            note_id= payload["current"]["id"],
            content= payload["current"]["content"],
            deal_id= payload["current"]["deal_id"],
            pin_note_on_specified_deal= payload["current"]["pinned_to_deal_flag"],
            organization_id= payload["current"]["org_id"],
            pin_note_on_specified_organization= payload["current"]["pinned_to_organization_flag"],
            person_id= payload["current"]["person_id"],
            pin_note_on_specified_person= payload["current"]["pinned_to_person_flag"],
            lead_id= payload["current"]["lead_id"],
            pin_note_on_specified_lead= payload["current"]["pinned_to_lead_flag"]
        )
        return note.__dict__

    def new_activity(self, context, payload):
        """ Create a activity"""

        activity = PipredriveCRMActivity(
            activity_id= payload["current"]["id"],
            subject= payload["current"]["subject"],
            organization_id= payload["current"]["org_id"],
            assign_to= payload["current"]["assigned_to_user_id"],
            person_id= payload["current"]["person_id"],
            deal_id= payload["current"]["deal_id"],
            is_done= payload["current"]["done"],
            type= payload["current"]["type"],
            due_date= payload["current"]["due_date"],
            duration= payload["current"]["duration"],
            note= payload["current"]["note"]
        )
        return activity.__dict__        