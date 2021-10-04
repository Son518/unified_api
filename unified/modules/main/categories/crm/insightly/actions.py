import json

from unified.core.actions import Actions
from crm.insightly import util
from crm.insightly.entities.insightly_task import InsightlyTask
from crm.insightly.entities.insightly_contact import InsightlyContact
from crm.insightly.entities.insightly_deal import InsightlyDeal
from crm.insightly.entities.insightly_event import InsightlyEvent
from crm.insightly.entities.insightly_account import InsightlyAccount
from crm.entities.task import Task

class InsightlyActions(Actions):

    def create_task(self, context, task_entity):
        '''Creates a new task'''

        task_schema = InsightlyTask(**task_entity)

        method = "POST"
        url = "/Tasks"
        task_data = {
            "TITLE": task_schema.task_name,
            "DUE_DATE": task_schema.date_due,
            "CATEGORY_ID": task_schema.category_id,
            "PRIORITY": task_schema.priority_id,
            "DETAILS": task_schema.description,
            "EMAIL_ID": task_schema.email,
            "COMPLETED": task_schema.completed,
            "STATUS": task_schema.status_id,
            "PERCENT_COMPLETE": task_schema.progress,
            "START_DATE": task_schema.start_date,
            "ASSIGNED_TEAM_ID": task_schema.assigned_team_id,
            "MILESTONE_ID": task_schema.milestone_id,
            "OPPORTUNITY_ID": task_schema.opportunity_id,
        }
        if task_schema.project_id:
            task_data["PROJECT_ID"] = task_schema.project_id
        if task_schema.task_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.task_owner_id
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_contact(self, context, task_entity):
        '''Creates a new contact'''

        task_schema = InsightlyContact(**task_entity)
        method = "POST"
        url = "/Contacts"
        task_data = {
            "SALUTATION": task_schema.prefix,
            "LAST_NAME": task_schema.last_name,
            "FIRST_NAME": task_schema.first_name,
            "ASSISTANT_NAME": task_schema.assistant_name,
            "PHONE_ASSISTANT": task_schema.assistant_phone,
            "EMAIL_ADDRESS": task_schema.email,
            "PHONE": task_schema.phone,
            "ADDRESS_MAIL_STREET": task_schema.mailing_street,
            "ADDRESS_MAIL_CITY": task_schema.mailing_city,
            "ADDRESS_MAIL_STATE": task_schema.mailing_state,
            "ADDRESS_MAIL_POSTCODE": task_schema.mailing_postal_code,
            "ADDRESS_MAIL_COUNTRY": task_schema.mailing_country,
            "ADDRESS_OTHER_CITY": task_schema.other_city,
            "ADDRESS_OTHER_COUNTRY": task_schema.other_country,
            "ADDRESS_OTHER_POSTCODE" : task_schema.other_postal_code,
            "ADDRESS_OTHER_STATE" : task_schema.other_state,
            "ADDRESS_OTHER_STREET" : task_schema.other_street,
            "BACKGROUND": task_schema.description,
            "PHONE_MOBILE": task_schema.phone_mobile,
            "DATE_OF_BIRTH": task_schema.date_of_birth,
            "TITLE": task_schema.title,
            "PHONE_FAX": task_schema.fax,
            "PHONE_HOME": task_schema.phone_home,
            "PHONE_OTHER": task_schema.phone_other,
            "SOCIAL_TWITTER": task_schema.twitter,
            "EMAIL_OPTED_OUT": task_schema.email_opted_out,
            "SOCIAL_FACEBOOK": task_schema.facebook,
            "SOCIAL_LINKEDIN": task_schema.linkedin,
        }
        if task_schema.organization_id:
            task_data["ORGANISATION_ID"] = task_schema.organization_id
        if task_schema.tags:
            task_data["TAGS"] =  [{"TAG_NAME": task_schema.tags}]
        if task_schema.contact_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.contact_owner_id

        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_deal(self, context, task_entity):
        '''Creates a new deal'''

        task_schema = InsightlyDeal(**task_entity)
        method = "POST"
        url = "/Opportunities"
        task_data = {
            "OPPORTUNITY_NAME": task_schema.opportunity_name,
            "OPPORTUNITY_DETAILS": task_schema.description,
            "ACTUAL_CLOSE_DATE": task_schema.actual_close_date,
            "BID_AMOUNT": task_schema.bid_amount,
            "BID_CURRENCY": task_schema.bid_currency,
            "BID_DURATION": task_schema.bid_duration,
            "BID_TYPE": task_schema.bid_type,
            "CATEGORY_ID": task_schema.category,
            "OPPORTUNITY_STATE": task_schema.current_state,
            "FORECAST_CLOSE_DATE": task_schema.forecast_close_date,
            "PROBABILITY": task_schema.probability_of_winning,
            "IMAGE_URL": task_schema.image,
            "RESPONSIBLE_USER_ID": task_schema.user_responsible_id
        }
        if task_schema.opportunity_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.opportunity_owner_id
        if task_schema.organization_id:
            task_data["ORGANISATION_ID"] = task_schema.organization_id
        if task_schema.tags:
            task_data["TAGS"] =  [{"TAG_NAME": task_schema.tags}]
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_account(self, context, task_entity):
        '''Creates a new account'''

        task_schema = InsightlyAccount(**task_entity)
        method = "POST"
        url = "/Organizations"
        task_data = {
            "ORGANISATION_NAME": task_schema.organization_name,
            "BACKGROUND": task_schema.description,
            "ADDRESS_BILLING_CITY": task_schema.billing_city,
            "ADDRESS_BILLING_COUNTRY": task_schema.billing_country,
            "ADDRESS_BILLING_POSTCODE": task_schema.biiling_postal_code,
            "ADDRESS_BILLING_STATE": task_schema.billing_state,
            "ADDRESS_BILLING_STREET": task_schema.billing_street,
            "SOCIAL_FACEBOOK": task_schema.facebook,
            "SOCIAL_LINKEDIN": task_schema.linkedin,
            "SOCIAL_TWITTER": task_schema.twitter,
            "PHONE_FAX": task_schema.fax,
            "PHONE": task_schema.phone,
            "ADDRESS_SHIP_CITY": task_schema.shipping_city,
            "ADDRESS_SHIP_COUNTRY": task_schema.shipping_country,
            "ADDRESS_SHIP_POSTCODE": task_schema.shipping_postal_code,
            "ADDRESS_SHIP_STATE": task_schema.shipping_state,
            "ADDRESS_SHIP_STREET": task_schema.shipping_street,
            "IMAGE_URL": task_schema.image,
        }
        if task_schema.tags:
            task_data["TAGS"] =  [{"TAG_NAME": task_schema.tags}]
        if task_schema.email_domains:
            task_data["EMAILDOMAINS"] = [{"EMAIL_DOMAIN": task_schema.email_domains}]
        if task_schema.opportunity_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.opportunity_owner_id

        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_event(self, context, task_entity):
        '''Creates a new event'''

        task_schema = InsightlyEvent(**task_entity)
        method = "POST"
        url = "/Events"
        task_data = {
            "TITLE": task_schema.title,
            "DETAILS": task_schema.description,
            "START_DATE_UTC": task_schema.start_date,
            "END_DATE_UTC": task_schema.end_date,
            "ALL_DAY": task_schema.all_day_event,
            "LOCATION": task_schema.location,
            "REMINDER_DATE_UTC": task_schema.reminder_date,
            "REMINDER_SENT": task_schema.reminder_sent,
            "DATE_CREATED_UTC": task_schema.date_added,
            "DATE_UPDATED_UTC": task_schema.date_updated,
        }
        if task_schema.owner_id:
            task_data["OWNER_USER_ID"] = task_schema.owner_id
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def update_contact(self, context, task_entity):
        '''Updates a contact'''

        task_schema = InsightlyContact(**task_entity)
        method = "PUT"
        url = "/Contacts"
        task_data = {
            "CONTACT_ID": task_schema.contact_id,
            "SALUTATION": task_schema.prefix,
            "LAST_NAME": task_schema.last_name,
            "FIRST_NAME": task_schema.first_name,
            "ASSISTANT_NAME": task_schema.assistant_name,
            "PHONE_ASSISTANT": task_schema.assistant_phone,
            "EMAIL_ADDRESS": task_schema.email,
            "PHONE": task_schema.phone,
            "ADDRESS_MAIL_STREET": task_schema.mailing_street,
            "ADDRESS_MAIL_CITY": task_schema.mailing_city,
            "ADDRESS_MAIL_STATE": task_schema.mailing_state,
            "ADDRESS_MAIL_POSTCODE": task_schema.mailing_postal_code,
            "ADDRESS_MAIL_COUNTRY": task_schema.mailing_country,
            "ADDRESS_OTHER_CITY": task_schema.other_city,
            "ADDRESS_OTHER_COUNTRY": task_schema.other_country,
            "ADDRESS_OTHER_POSTCODE" : task_schema.other_postal_code,
            "ADDRESS_OTHER_STATE" : task_schema.other_state,
            "ADDRESS_OTHER_STREET" : task_schema.other_street,
            "BACKGROUND": task_schema.description,
            "PHONE_MOBILE": task_schema.phone_mobile,
            "DATE_OF_BIRTH": task_schema.date_of_birth,
            "TITLE": task_schema.title,
            "PHONE_FAX": task_schema.fax,
            "PHONE_HOME": task_schema.phone_home,
            "PHONE_OTHER": task_schema.phone_other,
            "SOCIAL_TWITTER": task_schema.twitter,
            "EMAIL_OPTED_OUT": task_schema.email_opted_out,
            "SOCIAL_FACEBOOK": task_schema.facebook,
            "SOCIAL_LINKEDIN": task_schema.linkedin,
        }
        if task_schema.organization_id:
            task_data["ORGANISATION_ID"] = task_schema.organization_id
        if task_schema.tags:
            task_data["TAGS"] =  [{"TAG_NAME": task_schema.tags}]
        if task_schema.contact_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.contact_owner_id
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def update_deal(self, context, task_entity):
        '''Updates a deal'''

        task_schema = InsightlyDeal(**task_entity)
        method = "PUT"
        url = "/Opportunities"
        task_data = {
            "OPPORTUNITY_ID": task_schema.opportunity_id,
            "OPPORTUNITY_NAME": task_schema.opportunity_name,
            "OPPORTUNITY_DETAILS": task_schema.description,
            "ACTUAL_CLOSE_DATE": task_schema.actual_close_date,
            "BID_AMOUNT": task_schema.bid_amount,
            "BID_CURRENCY": task_schema.bid_currency,
            "BID_DURATION": task_schema.bid_duration,
            "BID_TYPE": task_schema.bid_type,
            "CATEGORY_ID": task_schema.category,
            "OPPORTUNITY_STATE": task_schema.current_state,
            "FORECAST_CLOSE_DATE": task_schema.forecast_close_date,
            "PROBABILITY": task_schema.probability_of_winning,
            "IMAGE_URL": task_schema.image,
            "RESPONSIBLE_USER_ID": task_schema.user_responsible_id
        }
        if task_schema.opportunity_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.opportunity_owner_id
        if task_schema.organization_id:
            task_data["ORGANISATION_ID"] = task_schema.organization_id
        if task_schema.tags:
            task_data["TAGS"] =  [{"TAG_NAME": task_schema.tags}]

        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def update_account(self, context, task_entity):
        '''Updates an account'''

        task_schema = InsightlyAccount(**task_entity)
        method = "PUT"
        url = "/Organizations"
        task_data = {
            "ORGANISATION_ID": task_schema.organization_id,
            "ORGANISATION_NAME": task_schema.organization_name,
            "BACKGROUND": task_schema.description,
            "ADDRESS_BILLING_CITY": task_schema.billing_city,
            "ADDRESS_BILLING_COUNTRY": task_schema.billing_country,
            "ADDRESS_BILLING_POSTCODE": task_schema.biiling_postal_code,
            "ADDRESS_BILLING_STATE": task_schema.billing_state,
            "ADDRESS_BILLING_STREET": task_schema.billing_street,
            "SOCIAL_FACEBOOK": task_schema.facebook,
            "SOCIAL_LINKEDIN": task_schema.linkedin,
            "SOCIAL_TWITTER": task_schema.twitter,
            "PHONE_FAX": task_schema.fax,
            "PHONE": task_schema.phone,
            "ADDRESS_SHIP_CITY": task_schema.shipping_city,
            "ADDRESS_SHIP_COUNTRY": task_schema.shipping_country,
            "ADDRESS_SHIP_POSTCODE": task_schema.shipping_postal_code,
            "ADDRESS_SHIP_STATE": task_schema.shipping_state,
            "ADDRESS_SHIP_STREET": task_schema.shipping_street,
            "IMAGE_URL": task_schema.image,
        }
        if task_schema.tags:
            task_data["TAGS"] = [{"TAG_NAME": task_schema.tags}]
        if task_schema.opportunity_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.opportunity_owner_id
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def update_event(self, context, task_entity):
        '''Updates an event'''

        task_schema = InsightlyEvent(**task_entity)
        method = "PUT"
        url = "/Events"
        task_data = {
            "EVENT_ID": task_schema.event_id,
            "TITLE": task_schema.title,
            "DETAILS": task_schema.description,
            "START_DATE_UTC": task_schema.start_date,
            "END_DATE_UTC": task_schema.end_date,
            "ALL_DAY": task_schema.all_day_event,
            "LOCATION": task_schema.location,
            "REMINDER_DATE_UTC": task_schema.reminder_date,
            "REMINDER_SENT": task_schema.reminder_sent,
            "DATE_CREATED_UTC": task_schema.date_added,
            "DATE_UPDATED_UTC": task_schema.date_updated,
        }
        if task_schema.owner_id:
            task_data["OWNER_USER_ID"] = task_schema.owner_id
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def update_task(self, context, task_entity):
        '''Updates a task'''

        task_schema = InsightlyTask(**task_entity)
        method = "PUT"
        url = "/Tasks"
        task_data = {
            "TASK_ID": task_schema.task_id,
            "TITLE": task_schema.task_name,
            "DUE_DATE": task_schema.date_due,
            "CATEGORY_ID": task_schema.category_id,
            "PRIORITY": task_schema.priority_id,
            "DETAILS": task_schema.description,
            "EMAIL_ID": task_schema.email,
            "COMPLETED": task_schema.completed,
            "STATUS": task_schema.status_id,
            "PERCENT_COMPLETE": task_schema.progress,
            "START_DATE": task_schema.start_date,
            "ASSIGNED_TEAM_ID": task_schema.assigned_team_id,
            "MILESTONE_ID": task_schema.milestone_id,
            "OPPORTUNITY_ID": task_schema.opportunity_id,
        }
        if task_schema.project_id:
            task_data["PROJECT_ID"] = task_schema.project_id
        if task_schema.task_owner_id:
            task_data["OWNER_USER_ID"] = task_schema.task_owner_id
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def update_note(self, context, task_entity):
        '''Updates a note'''

        task_schema = InsightlyContact(**task_entity)
        method = "PUT"
        url = "/Notes"
        task_data = {
            "NOTE_ID": task_schema.note_id,
            "TITLE": task_schema.note_title,
            "BODY": task_schema.description,
            "DATE_CREATED_UTC": task_schema.date_created,
            "DATE_UPDATED_UTC": task_schema.date_updated,
        }
        result = util.get_insightly_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)
