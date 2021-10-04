from marketing_automation.active_campaign.entities.active_campaign_contact_automation import ActiveCampaignContactAutomation
from marketing_automation.active_campaign.entities.active_campaign_contact_note import ActiveCampaignContactNote
from marketing_automation.active_campaign.entities.active_campaign_deal import ActiveCampaignDeal
from marketing_automation.active_campaign.entities.active_campaign_deal_note import ActiveCampaignDealNote
from marketing_automation.active_campaign.entities.active_campaign_deal_task import ActiveCampaignDealTask
from unified.core.actions import Actions
from marketing_automation.active_campaign import util
from marketing_automation.active_campaign.entities.active_campaign_account import ActiveCampaignAccount
from marketing_automation.active_campaign.entities.active_campaign_tracked_event import ActiveCampaignTrackedEvent
import json
import requests


class ActiveCampaignActions(Actions):
    """ActiveCampaign Actions wrapper class.

        Extends from common Actions class.
    """

    def get_account_fields_data(self, account_entity, context):
        """ Get the account custom  fields data"""

        custom_fields_data = util.rest('GET', 'accountCustomFieldMeta', context, None).text
        custom_fields_data = json.loads(custom_fields_data)
        
        fields = []
        custom_fields_data = custom_fields_data["accountCustomFieldMeta"]

        if account_entity.address_1 is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Address 1":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.address_1
                    }
                    fields.append(field_data)

        if account_entity.address_2 is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Address 2":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.address_2
                    }
                    fields.append(field_data)

        if account_entity.city is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "City":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.city
                    }
                    fields.append(field_data)

        if account_entity.state is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "State/Province":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.state
                    }
                    fields.append(field_data)

        if account_entity.postal_code is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Postal Code":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.postal_code
                    }
                    fields.append(field_data)

        if account_entity.country is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Country":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.country
                    }
                    fields.append(field_data)   

        if account_entity.phone_number is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Phone Number":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.phone_number
                    }
                    fields.append(field_data)

        if account_entity.description is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Description":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.description
                    }
                    fields.append(field_data)

        if account_entity.number_of_employees is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Number of Employees":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.number_of_employees
                    }
                    fields.append(field_data)

        if account_entity.annual_revenue is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Annual Revenue":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.annual_revenue
                    }
                    fields.append(field_data)     

        if account_entity.industry is not None:
            for obj in custom_fields_data:
                if obj["fieldLabel"] == "Industry/Vertical":
                    field_data = {
                        "customFieldId": obj["id"],
                        "fieldValue": account_entity.industry
                    }
                    fields.append(field_data)
        return fields

    def create_account(self, context, payload):
        """ Create a new account."""

        account_entity = ActiveCampaignAccount(**payload)

        # Get custom feilds data 
        fields = self.get_account_fields_data(account_entity, context)

        if len(fields)!=0:
            account_data = {
                "account": {
                    "name": account_entity.name,
                    "accountUrl": account_entity.website,
                    "fields": fields
                }
            }
        else:
            account_data = {
                "account": {
                    "name": account_entity.name,
                    "accountUrl": account_entity.website,
                }
            }
        
        resp = util.rest('POST', 'accounts', context, account_data)
        return json.loads(resp.text)

    def update_account(self, context, payload):
        """ Create a new account."""
        
        account_entity = ActiveCampaignAccount(**payload)

        # Get custom fields data
        fields = self.get_account_fields_data(account_entity, context)

        if len(fields)!=0:
            account_data = {
                "account": {
                    "name": account_entity.name,
                    "accountUrl": account_entity.website,
                    "fields": fields
                }
            }
        else:
            account_data = {
                "account": {
                    "name": account_entity.name,
                    "accountUrl": account_entity.website,
                }
            }
            
        resp = util.rest('PUT', f'accounts/{account_entity.account_id}', context, account_data).text
        return json.loads(resp)

    def add_contact_note(self, context, payload):
        """Add a note to contact"""

        note_entity = ActiveCampaignContactNote(**payload)
        note_data = {
            "note": {
                "note": note_entity.note,
                "relid": note_entity.contact_id,
                "reltype": "Subscriber",
            }
        }

        client = util.get_client(context) 
        return client.notes.create_a_note(note_data)
    
    def add_contact_to_automation(self, context, payload):
        """Add a contact to an automation."""

        contact_entity = ActiveCampaignContactAutomation(**payload)
        contact_data = {
            "contactAutomation": {
                "contact": int(contact_entity.contact_id),
                "automation": int(contact_entity.automation_id)
            }
        }

        client = util.get_client(context) 
        return client.contacts.add_a_contact_to_an_automation(contact_data)

    def get_deal_stages_id(self, deal_entity,  context):
        """ Get deal Stages data"""

        stage_data = util.rest('GET', 'dealStages', context, None).text
        stage_data = json.loads(stage_data)
        stage_data = stage_data["dealStages"]

        for obj in stage_data:
            if deal_entity.stage == obj["title"]:
                id = obj["id"]
                return id
        return None

    def create_deal(self, context, payload):
        """Create a new deal."""

        deal_entity = ActiveCampaignDeal(**payload)

        # Get stage id
        stage_id = self.get_deal_stages_id(deal_entity, context)

        deal_data = {
            "deal": {
                "contact": deal_entity.contact_id,
                "account": deal_entity.account_id,
                "currency": deal_entity.currency,
                "group": deal_entity.pipeline_id,
                "owner": deal_entity.owner_id,
                "stage": stage_id,
                "title": deal_entity.title,
                "value": deal_entity.value,
            }
        }

        client = util.get_client(context)
        response = client.deals.create_a_deal(deal_data)
        id = response["deal"]["id"]

        custom_fields_data = {
            "dealCustomFieldDatum":{
                "customFieldId": 1,
                "dealId": id,
                "fieldValue": deal_entity.forecasted_close_date
            }
        }
        
        update_forecast_date = util.rest('POST', 'dealCustomFieldData', context, custom_fields_data).text
        return response

    def update_deal(self, context, payload):
        """Update an existing deal"""

        deal_entity = ActiveCampaignDeal(**payload)     

        # Get Stage Id
        stage_id = self.get_deal_stages_id(deal_entity, context)

        deal_data = {
            "deal": {
                "contact": deal_entity.contact_id,
                "account": deal_entity.account_id,
                "currency": deal_entity.currency,
                "group": deal_entity.pipeline_id,
                "owner": deal_entity.owner_id,
                "stage": stage_id,
                "title": deal_entity.title,
                "value": deal_entity.value,
            }
        }

        client = util.get_client(context)
        response = client.deals.update_a_deal(deal_entity.deal_id, deal_data)

        custom_fields_data = {
            "dealCustomFieldDatum":{
                "customFieldId": 1,
                "dealId": deal_entity.deal_id,
                "fieldValue": deal_entity.forecasted_close_date
            }
        }
        
        update_forecast_date = util.rest('POST', 'dealCustomFieldData', context, custom_fields_data).text
        return response


    def add_note_to_deal(self, context, payload):
        """Create a deal note"""

        note_entity = ActiveCampaignDealNote(**payload)
        note_data = {
            "note": {
                "note": note_entity.note
            }
        }

        client = util.get_client(context)
        return client.deals.create_a_deal_note(note_entity.deal_id, note_data)


    def create_deal_task(self, context, payload):
        """Create a deal task"""

        task_entity = ActiveCampaignDealTask(**payload)
        resp = util.rest('GET', 'dealTasktypes', context, None).text
        resp = json.loads(resp)

        for dealtype in resp["dealTasktypes"]:
            if dealtype["title"] == task_entity.task_type:
                task_type_id = dealtype["id"]

        task_data = {
            "dealTask": {
                "title": task_entity.title,
                "relid": task_entity.deal_id,
                "note": task_entity.note,
                "duedate": task_entity.due_date,
                "dealTasktype": task_type_id,
                "assignee": task_entity.assignee_id,
            }
        }

        resp = util.rest('POST', 'dealTasks', context, task_data).text
        return json.loads(resp)


    def create_tracked_event(self, context, payload):
        
        headers= {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        event_info = ActiveCampaignTrackedEvent(**payload)
        data={
            "actid": event_info.account_id,
            "key": event_info.event_key,
            "event":event_info.event_name,
            "eventdata": int(event_info.event_value),
            "visit":{"email":event_info.contact_email_address}
        }
        resp = requests.request('POST', 'https://trackcmp.net/event', headers=headers, data=data).text
        return json.loads(resp)