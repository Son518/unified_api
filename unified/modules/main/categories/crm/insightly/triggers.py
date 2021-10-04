from flask import request, Response
from crm.insightly import util
from crm.insightly.entities.insightly_task import InsightlyTask
from crm.insightly.entities.insightly_contact import InsightlyContact
from crm.insightly.entities.insightly_deal import InsightlyDeal
from crm.insightly.entities.insightly_event import InsightlyEvent
from crm.insightly.entities.insightly_account import InsightlyAccount
from crm.insightly.api import InsightlyApi
from unified.core.triggers import Triggers
import requests


class InsightlyTriggers(Triggers):
    def new_task(self, context, payload):
        '''Triggers when new task is created'''

        DATA = payload["entity"]
        task_entity = InsightlyTask(
            task_id = DATA["TASK_ID"],
            name = DATA["TITLE"],
            description = DATA["DETAILS"],
            due_date = DATA["DUE_DATE"],
            owner_id = DATA["OWNER_USER_ID"],
            category_id = DATA["CATEGORY_ID"],
    		completed_date = DATA["COMPLETED_DATE_UTC"],
    		completed = DATA["COMPLETED"],
    		status_id = DATA["STATUS"],
    		priority = DATA["PRIORITY"],
    		percent_complete = DATA["PERCENT_COMPLETE"],
    		start_date = DATA["START_DATE"],
    		milestone_id = DATA["MILESTONE_ID"],
    		task_visibility = DATA["PUBLICLY_VISIBLE"],
    		responsible_user_id = DATA["RESPONSIBLE_USER_ID"],
    		task_owner_id = DATA["OWNER_USER_ID"],
    		date_created = DATA["DATE_CREATED_UTC"],
    		date_updated = DATA["DATE_UPDATED_UTC"],
    		email = DATA["EMAIL_ID"],
    		project_id = DATA["PROJECT_ID"],
    		reminder_date_utc = DATA["REMINDER_DATE_UTC"],
    		reminder_sent = DATA["REMINDER_SENT"],
    		owner_visible = DATA["OWNER_VISIBLE"],
    		stage_id = DATA["STAGE_ID"],
    		assigned_by_user_id = DATA["ASSIGNED_BY_USER_ID"],
    		parent_task_id = DATA["PARENT_TASK_ID"],
    		reccurence = DATA["RECURRENCE"],
    		opportunity_id = DATA["OPPORTUNITY_ID"],
    		assigned_team_id = DATA["ASSIGNED_TEAM_ID"],
    		assigned_date = DATA["ASSIGNED_DATE_UTC"],
    		created_user_id = DATA["CREATED_USER_ID"],
    		customfields = DATA["CUSTOMFIELDS"],
    		links = DATA["LINKS"],
        )

        return task_entity.__dict__

    def new_contact(self, context, payload):
        '''Triggers when new contact is created'''

        DATA = payload["entity"]
        contact_entity = InsightlyContact(
            contact_id = DATA["CONTACT_ID"],
            prefix = DATA["SALUTATION"],
            first_name = DATA["FIRST_NAME"],
            last_name = DATA["LAST_NAME"],
            description = DATA["BACKGROUND"],
            email = DATA["EMAIL_ADDRESS"],
            business_phone = DATA["PHONE"],
            owner_id = DATA["OWNER_USER_ID"],
            assistant_name = DATA["ASSISTANT_NAME"],
            assistant_phone = DATA["PHONE_ASSISTANT"],
            mailing_street = DATA["ADDRESS_MAIL_STREET"],
            mailing_city = DATA["ADDRESS_MAIL_CITY"],
            mailing_state = DATA["ADDRESS_MAIL_STATE"],
            mailing_postal_code = DATA["ADDRESS_MAIL_POSTCODE"],
            mailing_country = DATA["ADDRESS_MAIL_COUNTRY"],
            other_street = DATA["ADDRESS_OTHER_STREET"],
            other_city = DATA["ADDRESS_OTHER_CITY"],
            other_state = DATA["ADDRESS_OTHER_STATE"],
            other_postal_code = DATA["ADDRESS_OTHER_POSTCODE"],
            other_country = DATA["ADDRESS_OTHER_COUNTRY"],
            phone_mobile = DATA["PHONE_MOBILE"],
            phone_other = DATA["PHONE_OTHER"],
            phone_home = DATA["PHONE_HOME"],
            fax = DATA["PHONE_FAX"],
            date_of_birth = DATA["DATE_OF_BIRTH"],
            title = DATA["TITLE"],
            email_opted_out = DATA["EMAIL_OPTED_OUT"],
            facebook = DATA["SOCIAL_FACEBOOK"],
            linkedin = DATA["SOCIAL_LINKEDIN"],
            twitter = DATA["SOCIAL_TWITTER"],
            image_url = DATA["IMAGE_URL"],
            visible_to = DATA["VISIBLE_TO"],
            date_created = DATA["DATE_CREATED_UTC"],
            date_updated = DATA["DATE_UPDATED_UTC"],
            last_activity = DATA["LAST_ACTIVITY_DATE_UTC"],
            next_activity = DATA["NEXT_ACTIVITY_DATE_UTC"],
            created_user_id = DATA["CREATED_USER_ID"],
            organization_id = DATA["ORGANISATION_ID"],
            customfields = DATA["CUSTOMFIELDS"],
            tags = DATA["TAGS"],
            links = DATA["LINKS"]
        )
        return contact_entity.__dict__

    def new_deal(self, context, payload):
        '''Triggers when new deal is created'''

        DATA = payload["entity"]
        deal_entity = InsightlyDeal(
            opportunity_id = DATA["OPPORTUNITY_ID"],
            opportunity_name = DATA["OPPORTUNITY_NAME"],
            description = DATA["OPPORTUNITY_DETAILS"],
            current_state = DATA["OPPORTUNITY_STATE"],
            category = DATA["CATEGORY_ID"],
            image = DATA["IMAGE_URL"],
            bid_currency = DATA["BID_CURRENCY"],
            bid_amount = DATA["BID_AMOUNT"],
            bid_type = DATA["BID_TYPE"],
            bid_duration = DATA["BID_DURATION"],
            actual_close_date = DATA["ACTUAL_CLOSE_DATE"],
            user_responsible_id = DATA["RESPONSIBLE_USER_ID"],
            probability_of_winning = DATA["PROBABILITY"],
            forecast_close_date = DATA["FORECAST_CLOSE_DATE"],
            opportunity_owner_id = DATA["OWNER_USER_ID"],
            visible_to = DATA["VISIBLE_TO"],
            organization_id = DATA["ORGANISATION_ID"],
            date_created = DATA["DATE_CREATED_UTC"],
            date_updated = DATA["DATE_UPDATED_UTC"],
            opportunity_value = DATA["OPPORTUNITY_VALUE"],
            visible_team_id = DATA["VISIBLE_TEAM_ID"],
            last_activity = DATA["LAST_ACTIVITY_DATE_UTC"],
            next_activity = DATA["NEXT_ACTIVITY_DATE_UTC"],
            pipeline = DATA["PIPELINE_ID"],
            stage = DATA["STAGE_ID"],
            created_user_id = DATA["CREATED_USER_ID"],
            customfields = DATA["CUSTOMFIELDS"],
            links = DATA["LINKS"],
            tags = DATA["TAGS"]
        )
        return deal_entity.__dict__

    def new_account(self, context, payload):
        '''Triggers when new account is created'''

        DATA = payload["entity"]
        account_entity = InsightlyAccount(
            organization_id = DATA["ORGANISATION_ID"],
            organization_name = DATA["ORGANISATION_NAME"],
            description = DATA["BACKGROUND"],
            owner_id = DATA["OWNER_USER_ID"],
            billing_city = DATA["ADDRESS_BILLING_CITY"],
            billing_country = DATA["ADDRESS_BILLING_COUNTRY"],
            billing_postal_code = DATA["ADDRESS_BILLING_POSTCODE"],
            billing_state = DATA["ADDRESS_BILLING_STATE"],
            billing_street = DATA["ADDRESS_BILLING_STREET"],
            shipping_city = DATA["ADDRESS_SHIP_CITY"],
            shipping_country = DATA["ADDRESS_SHIP_COUNTRY"],
            shipping_postal_code = DATA["ADDRESS_SHIP_POSTCODE"],
            shipping_state = DATA["ADDRESS_SHIP_STATE"],
            shipping_street = DATA["ADDRESS_SHIP_STREET"],
            facebook = DATA["SOCIAL_FACEBOOK"],
            linkedin = DATA["SOCIAL_LINKEDIN"],
            twitter = DATA["SOCIAL_TWITTER"],
            fax = DATA["PHONE_FAX"],
            phone = DATA["PHONE"],
            image = DATA["IMAGE_URL"],
            visible_to = DATA["VISIBLE_TO"],
            visible_team_id = DATA["VISIBLE_TEAM_ID"],
            date_created = DATA["DATE_CREATED_UTC"],
            date_updated = DATA["DATE_UPDATED_UTC"],
            last_activity = DATA["LAST_ACTIVITY_DATE_UTC"],
            next_activity = DATA["NEXT_ACTIVITY_DATE_UTC"],
            created_user_id = DATA["CREATED_USER_ID"],
            website = DATA["WEBSITE"],
            customfields = DATA["CUSTOMFIELDS"],
            links = DATA["LINKS"],
            dates = DATA["DATES"],
            email_domains = DATA["EMAILDOMAINS"],
            tags = DATA["TAGS"]
        )
        return account_entity.__dict__

    def new_event(self, context, payload):
        '''Triggers when new event is created'''

        pass

    def new_note(self, context, payload):
        '''Triggers when new note is created'''

        pass

    def contact_updated(self, context, payload):
        '''Triggers when contact is updated'''

        pass

    def deal_updated(self, context, payload):
        '''Triggers when deal is updated'''

        pass

    def account_updated(self, context, payload):
        '''Triggers when account is updated'''

        pass

    def event_updated(self, context, payload):
        '''Triggers when event is updated'''

        pass

    def note_updated(self, context, payload):
        '''Triggers when note is updated'''

        pass

    def task_updated(self, context, payload):
        '''Triggers when task is updated'''

        pass
