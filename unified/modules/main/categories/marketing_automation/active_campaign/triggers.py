from marketing_automation.active_campaign.entities.active_campaign_account import ActiveCampaignAccount 
from marketing_automation.active_campaign.entities.active_campaign_contact import ActiveCampaignContact
from marketing_automation.active_campaign.entities.active_campaign_contact_note import ActiveCampaignContactNote
from marketing_automation.active_campaign.entities.active_campaign_contact_task import ActiveCampaignContactTask
from marketing_automation.active_campaign.entities.active_campaign_deal import ActiveCampaignDeal
from marketing_automation.active_campaign.entities.active_campaign_deal_note import ActiveCampaignDealNote
from marketing_automation.active_campaign.entities.active_campaign_deal_task import ActiveCampaignDealTask
from marketing_automation.active_campaign import util
import json
import urllib


class ActiveCampaignTriggers:
    """Triggers for Active Campaign"""

    def new_contact(self, context, payload):
        """ Trigger when new contact is added"""

        customer_entity = ActiveCampaignContact(
            contact_id=payload['contact[id]'],
            first_name=payload['contact[first_name]'],
            last_name=payload['contact[last_name]'],
            email_address=payload['contact[email]'],
            phone_number=payload['contact[phone]'],
            organization_name=payload['contact[orgname]'],
            tags=payload['contact[tags]'],
            list_id=payload['list'],
            full_name=payload['contact[first_name]']+" "+payload['contact[last_name]']
        )
        return customer_entity.__dict__


    def contact_updated(self, context, payload):
        """ Trigger while updating the contact"""

        customer_entity = ActiveCampaignContact(
            contact_id=payload['contact[id]'],
            first_name=payload['contact[first_name]'],
            last_name=payload['contact[last_name]'],
            email_address=payload['contact[email]'],
            phone_number=payload['contact[phone]'],
            organization_name=payload['contact[orgname]'],
            full_name= payload['contact[first_name]']+" "+payload['contact[last_name]'],
            list_id=payload['list'],
            tags=payload['contact[tags]']
        )
        return customer_entity.__dict__

    def new_contact_note(self, context, payload):
        """ Trigger for new contact note"""

        note_entity = ActiveCampaignContactNote(
            contact_id=payload['contact[id]'],
            list_id=payload['list'],
            note=payload['note']
        )
        return note_entity.__dict__

    def new_deal_added(self, context, payload):
        """ Trigger for new deal added"""
        
        deal_entity = ActiveCampaignDeal(
            deal_id=payload['deal[id]'],
            title=payload['deal[title]'],
            value=payload['deal[value]'],
            owner_id=payload['deal[owner]'],
            currency=payload['deal[currency]'],
            pipeline_title=payload['deal[pipeline_title]'],
            contact_email_address=payload['deal[contact_email]'],
            account_id=payload['customer_acct_id'],
            contact_id=payload['contact[id]'],
            pipeline_id=payload['deal[pipelineid]'],
            stage=payload['deal[stage_title]'],
            forecasted_close_date=payload['deal[fields][0][value]']
        )
        return deal_entity.__dict__


    def deal_updated(self, context, payload):
        """ Trigger for deal update"""

        deal_entity = ActiveCampaignDeal(
            deal_id=payload['deal[id]'],
            title=payload['deal[title]'],
            value=payload['deal[value]'],
            owner_id=payload['deal[owner]'],
            currency=payload['deal[currency]'],
            pipeline_title=payload['deal[pipeline_title]'],
            contact_email_address=payload['deal[contact_email]'],
            account_id=payload['customer_acct_id'],
            contact_id=payload['contact[id]'],
            pipeline_id=payload['deal[pipelineid]'],
            stage=payload['deal[stage_title]']
        )
        return deal_entity.__dict__

    def new_deal_note(self, context, payload):
        """ Trigger for new deal note"""

        note_entity = ActiveCampaignDealNote(
            id=payload['note[id]'],
            deal_id=payload['deal[id]'],
            note=payload['note[text]'],
        )
        return note_entity.__dict__

    def new_deal_task(self, context, payload):
        """ Trigger for new deal task"""
        task_entity = ActiveCampaignDealTask(
            deal_id=payload['deal[id]'],
            title=payload['deal[title]'],
            task_id=payload['task[id]'],
            note=payload['task[note]'],
            due_date=payload['task[duedate]'],
            task_type_id=payload['task[type_id]'],
            assignee_id=payload['deal[owner]']
        )
        return task_entity.__dict__

    def new_account(self, context, payload):
        """ Trigger for new contact"""

        account_entity = ActiveCampaignAccount(
            account_id=payload['account[id]'],
            name=payload['account[name]'],
            website=payload['account[account_url]']
        )
        return account_entity.__dict__

    def account_updated(self, context, payload):
        """ Triggers for account update"""

        account_entity = ActiveCampaignAccount(
            account_id=payload['account[id]'],
            name=payload['account[name]'],
            website=payload['account[account_url]']
        )
        return account_entity.__dict__

    def new_contact_task(self, context, payload):
        """ Triggers for new contact task"""

        task_entity = ActiveCampaignContactTask(
            contact_id=payload['contact[id]'],
            customer_acct_name=payload['contact[customer_acct_name]'],
            task_title=payload['task[title]'],
            due_date=payload['task[duedate_iso]'],
            task_type=payload['type'],
            first_name=payload['contact[first_name]'],
            last_name=payload['contact[last_name]'],
            phone=payload['contact[phone]'],
            orgname=payload['orgname'],
            task_id=payload['task[id]'],
            task_type_title=payload['task[type_title]'],
            task_note=payload['task[note]']
        )
        return task_entity.__dict__