from unified.core.triggers import Triggers
from marketing_automation.hubspot.api import HubspotApi
from marketing_automation.hubspot.entities.hubspot_ticket import HubspotTicket
from marketing_automation.hubspot.entities.hubspot_contact import HubspotContact


class HubspotTriggers(Triggers):
    def new_ticket(self, context, payload):
        '''Triggers when new ticket.'''

        payload_properties = payload.get('properties')
        ticket = HubspotTicket(
            ticket_id=payload.get('objectId'),
            name=payload_properties.get('subject').get(
                'value') if payload_properties.get('subject') else None,
            pipeline=payload_properties.get('hs_pipeline').get(
                'value') if payload_properties.get('hs_pipeline') else None,
            ticket_description=payload_properties.get('content').get(
                'value') if payload_properties.get('content') else None,
            source=payload_properties.get('hs_pipeline_stage').get(
                'value') if payload_properties.get('hs_pipeline_stage') else None,
            owner_id=payload_properties.get('hubspot_owner_id').get(
                'value') if payload_properties.get('hubspot_owner_id') else None,
            priority=payload_properties.get('hs_ticket_priority').get(
                'value') if payload_properties.get('hs_ticket_priority') else None
        ).__dict__
        return ticket
        
    def new_company(self, context, payload):
        '''Triggers when new company.'''

        return HubspotApi().company_mappings(payload)

    def new_contact(self, context, payload):
        '''Triggers when new contact.'''

        payload_properties = payload.get("properties")
        contact = HubspotContact(
            contact_id=payload.get("vid"),
            email_address=payload_properties.get('email').get(
                'value') if payload_properties.get('email') else None,
            first_name=payload_properties.get('firstname').get(
                'value') if payload_properties.get('firstname') else None,
            last_name=payload_properties.get('lastname').get(
                'value') if payload_properties.get('lastname') else None,
            phone_number=payload_properties.get('phone').get(
                'value') if payload_properties.get('phone') else None,
            job_title=payload_properties.get('jobtitle').get(
                'value') if payload_properties.get('jobtitle') else None,
            lifecycle_stage=payload_properties.get('lifecyclestage').get(
                'value') if payload_properties.get('lifecyclestage') else None,
            lead_status=payload_properties.get('hs_lead_status').get(
                'value') if payload_properties.get('hs_lead_status') else None,
        ).__dict__
        return contact

    def new_deal(self, context, payload):
        '''Triggers when new deal.'''

        return HubspotApi().deal_mappings(payload)
