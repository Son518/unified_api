import json

from crm.entities.tag import Tag
from crm.insightly.entities.insightly_task import InsightlyTask
from crm.insightly.entities.insightly_contact import InsightlyContact
from crm.insightly.entities.insightly_deal import InsightlyDeal
from crm.insightly.entities.insightly_event import InsightlyEvent
from crm.insightly.entities.insightly_account import InsightlyAccount
from crm.insightly.entities.insightly_lead import InsightlyLead
from crm.insightly import util

class InsightlyApi():
    def task(self, context, params):
        '''Gets a task by id'''

        headers = context['headers']
        method = 'GET'
        url = '/Tasks/{id}'.format(id=params['id'])

        result = json.loads(util.get_insightly_request(method, url, context['headers']).text)

        insightly_task = InsightlyTask(
            task_id = result["TASK_ID"],
            task_name = result["TITLE"],
            date_due = result["DUE_DATE"],
            category_id = result["CATEGORY_ID"],
            priority_id = result["PRIORITY"],
            description = result["DETAILS"],
            email = result["EMAIL_ID"],
            completed = result["COMPLETED"],
            status_id = result["STATUS"],
            progress = result["PERCENT_COMPLETE"],
            start_date = result["START_DATE"],
            assigned_team_id = result["ASSIGNED_TEAM_ID"],
            milestone_id = result["MILESTONE_ID"],
            opportunity_id = result["OPPORTUNITY_ID"],
            project_id = result["PROJECT_ID"],
            task_owner_id = result["OWNER_USER_ID"]
        )

        return insightly_task.__dict__

    def contact(self, context, params):
        '''Gets a contact by id'''

        headers = context['headers']
        method = 'GET'
        url = '/Contacts/{id}'.format(id=params['id'])

        result = json.loads(util.get_insightly_request(method, url, context['headers']).text)
        insightly_contact = InsightlyContact(
            contact_id = result["CONTACT_ID"],
            prefix = result["SALUTATION"],
            last_name = result["LAST_NAME"],
            first_name = result["FIRST_NAME"],
            assistant_name = result["ASSISTANT_NAME"],
            assistant_phone = result["PHONE_ASSISTANT"],
            email = result["EMAIL_ADDRESS"],
            phone = result["PHONE"],
            mailing_street = result["ADDRESS_MAIL_STREET"],
            mailing_city = result["ADDRESS_MAIL_CITY"],
            mailing_state = result["ADDRESS_MAIL_STATE"],
            mailing_postal_code = result["ADDRESS_MAIL_POSTCODE"],
            mailing_country = result["ADDRESS_MAIL_COUNTRY"],
            other_city = result["ADDRESS_OTHER_CITY"],
            other_country = result["ADDRESS_OTHER_COUNTRY"],
            other_postal_code = result["ADDRESS_OTHER_POSTCODE"],
            other_state = result["ADDRESS_OTHER_STATE"],
            other_street = result["ADDRESS_OTHER_STREET"],
            description = result["BACKGROUND"],
            phone_mobile = result["PHONE_MOBILE"],
            date_of_birth = result["DATE_OF_BIRTH"],
            title = result["TITLE"],
            fax = result["PHONE_FAX"],
            phone_home = result["PHONE_HOME"],
            phone_other = result["PHONE_OTHER"],
            twitter = result["SOCIAL_TWITTER"],
            email_opted_out = result["EMAIL_OPTED_OUT"],
            facebook = result["SOCIAL_FACEBOOK"],
            linkedin = result["SOCIAL_LINKEDIN"],
            owner_id = result['OWNER_USER_ID'],
            organization_id = result["ORGANISATION_ID"],
            tags = result["TAGS"]
        )

        return insightly_contact.__dict__

    def contact_by_name(self, context, params):
        '''Gets a contact by name'''

        headers = context['headers']
        method = 'GET'
        url = '/Contacts'

        contact_list = json.loads(util.get_insightly_request(method, url, headers).text)
        contacts = []

        for contact in contact_list:
            if params["name"] == contact["LAST_NAME"]:
                insightly_contact = InsightlyContact(
                    contact_id = contact["CONTACT_ID"],
                    prefix = contact["SALUTATION"],
                    last_name = contact["LAST_NAME"],
                    first_name = contact["FIRST_NAME"],
                    assistant_name = contact["ASSISTANT_NAME"],
                    assistant_phone = contact["PHONE_ASSISTANT"],
                    email = contact["EMAIL_ADDRESS"],
                    phone = contact["PHONE"],
                    mailing_street = contact["ADDRESS_MAIL_STREET"],
                    mailing_city = contact["ADDRESS_MAIL_CITY"],
                    mailing_state = contact["ADDRESS_MAIL_STATE"],
                    mailing_postal_code = contact["ADDRESS_MAIL_POSTCODE"],
                    mailing_country = contact["ADDRESS_MAIL_COUNTRY"],
                    other_city = contact["ADDRESS_OTHER_CITY"],
                    other_country = contact["ADDRESS_OTHER_COUNTRY"],
                    other_postal_code = contact["ADDRESS_OTHER_POSTCODE"],
                    other_state = contact["ADDRESS_OTHER_STATE"],
                    other_street = contact["ADDRESS_OTHER_STREET"],
                    description = contact["BACKGROUND"],
                    phone_mobile = contact["PHONE_MOBILE"],
                    date_of_birth = contact["DATE_OF_BIRTH"],
                    title = contact["TITLE"],
                    fax = contact["PHONE_FAX"],
                    phone_home = contact["PHONE_HOME"],
                    phone_other = contact["PHONE_OTHER"],
                    twitter = contact["SOCIAL_TWITTER"],
                    email_opted_out = contact["EMAIL_OPTED_OUT"],
                    facebook = contact["SOCIAL_FACEBOOK"],
                    linkedin = contact["SOCIAL_LINKEDIN"],
                    owner_id = contact['OWNER_USER_ID'],
                    organization_id = contact["ORGANISATION_ID"],
                    tags = contact["TAGS"]
                )
                contacts.append(insightly_contact.__dict__)
        return json.dumps(contacts)

    def contact_by_email(self, context, params):
        '''Gets a contact by email'''

        headers = context['headers']
        method = 'GET'
        url = '/Contacts'

        contact_list = json.loads(util.get_insightly_request(method, url, headers).text)
        contacts = []

        for contact in contact_list:
            if params["email"] == contact["EMAIL_ADDRESS"]:
                insightly_contact = InsightlyContact(
                    contact_id = contact["CONTACT_ID"],
                    prefix = contact["SALUTATION"],
                    last_name = contact["LAST_NAME"],
                    first_name = contact["FIRST_NAME"],
                    assistant_name = contact["ASSISTANT_NAME"],
                    assistant_phone = contact["PHONE_ASSISTANT"],
                    email = contact["EMAIL_ADDRESS"],
                    phone = contact["PHONE"],
                    mailing_street = contact["ADDRESS_MAIL_STREET"],
                    mailing_city = contact["ADDRESS_MAIL_CITY"],
                    mailing_state = contact["ADDRESS_MAIL_STATE"],
                    mailing_postal_code = contact["ADDRESS_MAIL_POSTCODE"],
                    mailing_country = contact["ADDRESS_MAIL_COUNTRY"],
                    other_city = contact["ADDRESS_OTHER_CITY"],
                    other_country = contact["ADDRESS_OTHER_COUNTRY"],
                    other_postal_code = contact["ADDRESS_OTHER_POSTCODE"],
                    other_state = contact["ADDRESS_OTHER_STATE"],
                    other_street = contact["ADDRESS_OTHER_STREET"],
                    description = contact["BACKGROUND"],
                    phone_mobile = contact["PHONE_MOBILE"],
                    date_of_birth = contact["DATE_OF_BIRTH"],
                    title = contact["TITLE"],
                    fax = contact["PHONE_FAX"],
                    phone_home = contact["PHONE_HOME"],
                    phone_other = contact["PHONE_OTHER"],
                    twitter = contact["SOCIAL_TWITTER"],
                    email_opted_out = contact["EMAIL_OPTED_OUT"],
                    facebook = contact["SOCIAL_FACEBOOK"],
                    linkedin = contact["SOCIAL_LINKEDIN"],
                    owner_id = contact['OWNER_USER_ID'],
                    organization_id = contact["ORGANISATION_ID"],
                    tags = contact["TAGS"]
                )
                contacts.append(insightly_contact.__dict__)
        return json.dumps(contacts)

    def account(self, context, params):
        '''Gets an account by id'''

        headers = context['headers']
        method = 'GET'
        url = '/Organisations/{id}'.format(id=params['id'])
        result = json.loads(util.get_insightly_request(method, url, context['headers']).text)


        insightly_organisation = InsightlyAccount(
            organization_id = result["ORGANISATION_ID"],
            organization_name = result["ORGANISATION_NAME"],
            description = result["BACKGROUND"],
            billing_city = result["ADDRESS_BILLING_CITY"],
            billing_country = result["ADDRESS_BILLING_COUNTRY"],
            biiling_postal_code = result["ADDRESS_BILLING_POSTCODE"],
            billing_state = result["ADDRESS_BILLING_STATE"],
            billing_street = result["ADDRESS_BILLING_STREET"],
            facebook = result["SOCIAL_FACEBOOK"],
            linkedin = result["SOCIAL_LINKEDIN"],
            twitter = result["SOCIAL_TWITTER"],
            fax = result["PHONE_FAX"],
            phone = result["PHONE"],
            shipping_city = result["ADDRESS_SHIP_CITY"],
            shipping_country = result["ADDRESS_SHIP_COUNTRY"],
            shipping_postal_code = result["ADDRESS_SHIP_POSTCODE"],
            shipping_state = result["ADDRESS_SHIP_STATE"],
            shipping_street = result["ADDRESS_SHIP_STREET"],
            image = result["IMAGE_URL"],
            tags = result["TAGS"],
            email_domains = result["EMAILDOMAINS"],
            opportunity_owner_id = result["OWNER_USER_ID"]
        )

        return insightly_organisation.__dict__

    def account_by_name(self, context, params):
        '''Gets an account by name'''

        headers = context['headers']
        method = 'GET'
        url = '/Organisations'

        organisations_list = json.loads(util.get_insightly_request(method, url, headers).text)
        organisations = []

        for organisation in organisations_list:
            if params["name"] == organisation["ORGANISATION_NAME"]:
                insightly_organisation = InsightlyAccount(
                    organization_id = organisation["ORGANISATION_ID"],
                    organization_name = organisation["ORGANISATION_NAME"],
                    description = organisation["BACKGROUND"],
                    billing_city = organisation["ADDRESS_BILLING_CITY"],
                    billing_country = organisation["ADDRESS_BILLING_COUNTRY"],
                    biiling_postal_code = organisation["ADDRESS_BILLING_POSTCODE"],
                    billing_state = organisation["ADDRESS_BILLING_STATE"],
                    billing_street = organisation["ADDRESS_BILLING_STREET"],
                    facebook = organisation["SOCIAL_FACEBOOK"],
                    linkedin = organisation["SOCIAL_LINKEDIN"],
                    twitter = organisation["SOCIAL_TWITTER"],
                    fax = organisation["PHONE_FAX"],
                    phone = organisation["PHONE"],
                    shipping_city = organisation["ADDRESS_SHIP_CITY"],
                    shipping_country = organisation["ADDRESS_SHIP_COUNTRY"],
                    shipping_postal_code = organisation["ADDRESS_SHIP_POSTCODE"],
                    shipping_state = organisation["ADDRESS_SHIP_STATE"],
                    shipping_street = organisation["ADDRESS_SHIP_STREET"],
                    image = organisation["IMAGE_URL"],
                    tags = organisation["TAGS"],
                    email_domains = organisation["EMAILDOMAINS"],
                    opportunity_owner_id = organisation["OWNER_USER_ID"]
                )
                organisations.append(insightly_organisation.__dict__)
        return json.dumps(organisations)

    def deal(self, context, params):
        '''Gets a deal by id'''

        headers = context['headers']
        method = 'GET'
        url = '/Opportunities/{id}'.format(id=params['id'])
        result = json.loads(util.get_insightly_request(method, url, context['headers']).text)

        insightly_opportunity = InsightlyDeal(
            opportunity_id = result["OPPORTUNITY_ID"],
            opportunity_name = result["OPPORTUNITY_NAME"],
            description = result["OPPORTUNITY_DETAILS"],
            actual_close_date = result["ACTUAL_CLOSE_DATE"],
            bid_amount = result["BID_AMOUNT"],
            bid_currency = result["BID_CURRENCY"],
            bid_duration = result["BID_DURATION"],
            bid_type = result["BID_TYPE"],
            category = result["CATEGORY_ID"],
            current_state = result["OPPORTUNITY_STATE"],
            forecast_close_date = result["FORECAST_CLOSE_DATE"],
            probability_of_winning = result["PROBABILITY"],
            image = result["IMAGE_URL"],
            user_responsible_id = result["RESPONSIBLE_USER_ID"],
            opportunity_owner_id = result["OWNER_USER_ID"],
            organization_id = result["ORGANISATION_ID"],
            tags = result["TAGS"]
        )
        return insightly_opportunity.__dict__

    def deal_by_name(self, context, params):
        '''Gets a deal by name'''

        headers = context['headers']
        method = 'GET'
        url = '/Opportunities'

        opportunities_list = json.loads(util.get_insightly_request(method, url, headers).text)
        opportunities = []

        for opportunity in opportunities_list:
            if params["name"] == opportunity["OPPORTUNITY_NAME"]:
                insightly_opportunity = InsightlyDeal(
                    opportunity_id = opportunity["OPPORTUNITY_ID"],
                    opportunity_name = opportunity["OPPORTUNITY_NAME"],
                    description = opportunity["OPPORTUNITY_DETAILS"],
                    actual_close_date = opportunity["ACTUAL_CLOSE_DATE"],
                    bid_amount = opportunity["BID_AMOUNT"],
                    bid_currency = opportunity["BID_CURRENCY"],
                    bid_duration = opportunity["BID_DURATION"],
                    bid_type = opportunity["BID_TYPE"],
                    category = opportunity["CATEGORY_ID"],
                    current_state = opportunity["OPPORTUNITY_STATE"],
                    forecast_close_date = opportunity["FORECAST_CLOSE_DATE"],
                    probability_of_winning = opportunity["PROBABILITY"],
                    image = opportunity["IMAGE_URL"],
                    user_responsible_id = opportunity["RESPONSIBLE_USER_ID"],
                    opportunity_owner_id = opportunity["OWNER_USER_ID"],
                    organization_id = opportunity["ORGANISATION_ID"],
                    tags = opportunity["TAGS"]
                )
                opportunities.append(insightly_opportunity.__dict__)
        return json.dumps(opportunities)

    def accounts(self, context, params):
        '''Gets a list of accounts'''

        headers = context['headers']
        method = 'GET'
        url = '/Organisations'

        organisations_list = json.loads(util.get_insightly_request(method, url, headers).text)
        organisations = []

        for organisation in organisations_list:
            insightly_organisation = InsightlyAccount(
                organization_id = organisation["ORGANISATION_ID"],
                organization_name = organisation["ORGANISATION_NAME"],
                description = organisation["BACKGROUND"],
                billing_city = organisation["ADDRESS_BILLING_CITY"],
                billing_country = organisation["ADDRESS_BILLING_COUNTRY"],
                biiling_postal_code = organisation["ADDRESS_BILLING_POSTCODE"],
                billing_state = organisation["ADDRESS_BILLING_STATE"],
                billing_street = organisation["ADDRESS_BILLING_STREET"],
                facebook = organisation["SOCIAL_FACEBOOK"],
                linkedin = organisation["SOCIAL_LINKEDIN"],
                twitter = organisation["SOCIAL_TWITTER"],
                fax = organisation["PHONE_FAX"],
                phone = organisation["PHONE"],
                shipping_city = organisation["ADDRESS_SHIP_CITY"],
                shipping_country = organisation["ADDRESS_SHIP_COUNTRY"],
                shipping_postal_code = organisation["ADDRESS_SHIP_POSTCODE"],
                shipping_state = organisation["ADDRESS_SHIP_STATE"],
                shipping_street = organisation["ADDRESS_SHIP_STREET"],
                image = organisation["IMAGE_URL"],
                tags = organisation["TAGS"],
                email_domains = organisation["EMAILDOMAINS"],
                opportunity_owner_id = organisation["OWNER_USER_ID"]
            )
            organisations.append(insightly_organisation.__dict__)
        return json.dumps(organisations)

    def deals(self, context, params):
        '''Gets a list of deals'''

        headers = context['headers']
        method = 'GET'
        url = '/Opportunities'

        opportunities_list = json.loads(util.get_insightly_request(method, url, headers).text)
        opportunities = []

        for opportunity in opportunities_list:
            insightly_opportunity = InsightlyDeal(
                opportunity_id = opportunity["OPPORTUNITY_ID"],
                opportunity_name = opportunity["OPPORTUNITY_NAME"],
                description = opportunity["OPPORTUNITY_DETAILS"],
                actual_close_date = opportunity["ACTUAL_CLOSE_DATE"],
                bid_amount = opportunity["BID_AMOUNT"],
                bid_currency = opportunity["BID_CURRENCY"],
                bid_duration = opportunity["BID_DURATION"],
                bid_type = opportunity["BID_TYPE"],
                category = opportunity["CATEGORY_ID"],
                current_state = opportunity["OPPORTUNITY_STATE"],
                forecast_close_date = opportunity["FORECAST_CLOSE_DATE"],
                probability_of_winning = opportunity["PROBABILITY"],
                image = opportunity["IMAGE_URL"],
                user_responsible_id = opportunity["RESPONSIBLE_USER_ID"],
                opportunity_owner_id = opportunity["OWNER_USER_ID"],
                organization_id = opportunity["ORGANISATION_ID"],
                tags = opportunity["TAGS"]
            )
            opportunities.append(insightly_opportunity.__dict__)
        return json.dumps(opportunities)

    def leads(self, context, params):
        '''Gets a list of leads'''

        headers = context['headers']
        method = 'GET'
        url = '/Leads'

        leads_list = json.loads(util.get_insightly_request(method, url, headers).text)
        leads = []

        for lead in leads_list:
            insightly_lead = InsightlyLead(
                lead_id = lead["LEAD_ID"],
                first_name = lead["FIRST_NAME"],
                last_name = lead["LAST_NAME"],
                owner_id = lead["OWNER_USER_ID"]
            )
            leads.append(insightly_lead.__dict__)
        return json.dumps(leads)

    def events(self, context, params):
        '''Gets a list of events'''

        headers = context['headers']
        method = 'GET'
        url = '/Events'

        events_list = json.loads(util.get_insightly_request(method, url, headers).text)
        events = []

        for event in events_list:
            insightly_event = InsightlyEvent(
                event_id = event["EVENT_ID"],
                title = event["TITLE"],
                description = event["DETAILS"],
                start_date = event["START_DATE_UTC"],
                end_date = event["END_DATE_UTC"],
                all_day_event = event["ALL_DAY"],
                location = event["LOCATION"],
                reminder_date = event["REMINDER_DATE_UTC"],
                reminder_sent = event["REMINDER_SENT"],
                date_added = event["DATE_CREATED_UTC"],
                date_updated = event["DATE_UPDATED_UTC"],
                owner_id = event["OWNER_USER_ID"]
            )
            events.append(insightly_event.__dict__)
        return json.dumps(events)

    def tasks(self, context, params):
        '''Gets a list of tasks'''

        headers = context['headers']
        method = 'GET'
        url = '/Tasks'

        task_list = json.loads(util.get_insightly_request(method, url, headers).text)
        tasks = []

        for task in task_list:
            insightly_task = InsightlyTask(
                task_id = task["TASK_ID"],
                task_name = task["TITLE"],
                date_due = task["DUE_DATE"],
                category_id = task["CATEGORY_ID"],
                priority_id = task["PRIORITY"],
                description = task["DETAILS"],
                email = task["EMAIL_ID"],
                completed = task["COMPLETED"],
                status_id = task["STATUS"],
                progress = task["PERCENT_COMPLETE"],
                start_date = task["START_DATE"],
                assigned_team_id = task["ASSIGNED_TEAM_ID"],
                milestone_id = task["MILESTONE_ID"],
                opportunity_id = task["OPPORTUNITY_ID"],
                project_id = task["PROJECT_ID"],
                task_owner_id = task["OWNER_USER_ID"]
            )
            tasks.append(insightly_task.__dict__)
        return json.dumps(tasks)

    def contacts(self, context, params):
        '''Gets a list of contacts'''

        headers = context['headers']
        method = 'GET'
        url = '/Contacts'

        contact_list = json.loads(util.get_insightly_request(method, url, headers).text)
        contacts = []

        for contact in contact_list:
            insightly_contact = InsightlyContact(
                contact_id = contact["CONTACT_ID"],
                prefix = contact["SALUTATION"],
                last_name = contact["LAST_NAME"],
                first_name = contact["FIRST_NAME"],
                assistant_name = contact["ASSISTANT_NAME"],
                assistant_phone = contact["PHONE_ASSISTANT"],
                email = contact["EMAIL_ADDRESS"],
                phone = contact["PHONE"],
                mailing_street = contact["ADDRESS_MAIL_STREET"],
                mailing_city = contact["ADDRESS_MAIL_CITY"],
                mailing_state = contact["ADDRESS_MAIL_STATE"],
                mailing_postal_code = contact["ADDRESS_MAIL_POSTCODE"],
                mailing_country = contact["ADDRESS_MAIL_COUNTRY"],
                other_city = contact["ADDRESS_OTHER_CITY"],
                other_country = contact["ADDRESS_OTHER_COUNTRY"],
                other_postal_code = contact["ADDRESS_OTHER_POSTCODE"],
                other_state = contact["ADDRESS_OTHER_STATE"],
                other_street = contact["ADDRESS_OTHER_STREET"],
                description = contact["BACKGROUND"],
                phone_mobile = contact["PHONE_MOBILE"],
                date_of_birth = contact["DATE_OF_BIRTH"],
                title = contact["TITLE"],
                fax = contact["PHONE_FAX"],
                phone_home = contact["PHONE_HOME"],
                phone_other = contact["PHONE_OTHER"],
                twitter = contact["SOCIAL_TWITTER"],
                email_opted_out = contact["EMAIL_OPTED_OUT"],
                facebook = contact["SOCIAL_FACEBOOK"],
                linkedin = contact["SOCIAL_LINKEDIN"],
                owner_id = contact['OWNER_USER_ID'],
                organization_id = contact["ORGANISATION_ID"],
                tags = contact["TAGS"]
            )
            contacts.append(insightly_contact.__dict__)
        return json.dumps(contacts)

    def new_accounts_by_date_range(self, context, params):
        '''Gets a list of accounts based on creation date'''

        headers = context['headers']
        method = 'GET'
        url = '/Organisations'

        organisations_list = json.loads(util.get_insightly_request(method, url, headers).text)
        organisations = []

        for organisation in organisations_list:
            if int(params["start_date"]) > util.date_format_to_epoch(organisation['DATE_CREATED_UTC']) and util.date_format_to_epoch(organisation['DATE_CREATED_UTC']) < int(params["end_date"]):
                insightly_organisation = InsightlyAccount(
                    organization_id = organisation["ORGANISATION_ID"],
                    organization_name = organisation["ORGANISATION_NAME"],
                    description = organisation["BACKGROUND"],
                    billing_city = organisation["ADDRESS_BILLING_CITY"],
                    billing_country = organisation["ADDRESS_BILLING_COUNTRY"],
                    biiling_postal_code = organisation["ADDRESS_BILLING_POSTCODE"],
                    billing_state = organisation["ADDRESS_BILLING_STATE"],
                    billing_street = organisation["ADDRESS_BILLING_STREET"],
                    facebook = organisation["SOCIAL_FACEBOOK"],
                    linkedin = organisation["SOCIAL_LINKEDIN"],
                    twitter = organisation["SOCIAL_TWITTER"],
                    fax = organisation["PHONE_FAX"],
                    phone = organisation["PHONE"],
                    shipping_city = organisation["ADDRESS_SHIP_CITY"],
                    shipping_country = organisation["ADDRESS_SHIP_COUNTRY"],
                    shipping_postal_code = organisation["ADDRESS_SHIP_POSTCODE"],
                    shipping_state = organisation["ADDRESS_SHIP_STATE"],
                    shipping_street = organisation["ADDRESS_SHIP_STREET"],
                    image = organisation["IMAGE_URL"],
                    tags = organisation["TAGS"],
                    email_domains = organisation["EMAILDOMAINS"],
                    opportunity_owner_id = organisation["OWNER_USER_ID"]
                )
                organisations.append(insightly_organisation.__dict__)
        return json.dumps(organisations)

    def new_contacts_by_date_range(self, context, params):
        '''Gets a list of contacts based on creation date'''

        headers = context['headers']
        method = 'GET'
        url = '/Contacts'

        contact_list = json.loads(util.get_insightly_request(method, url, headers).text)
        contacts = []

        for contact in contact_list:
            if int(params["start_date"]) > util.date_format_to_epoch(contact['DATE_CREATED_UTC']) and util.date_format_to_epoch(contact['DATE_CREATED_UTC']) < int(params["end_date"]):
                insightly_contact = InsightlyContact(
                    contact_id = contact["CONTACT_ID"],
                    prefix = contact["SALUTATION"],
                    last_name = contact["LAST_NAME"],
                    first_name = contact["FIRST_NAME"],
                    assistant_name = contact["ASSISTANT_NAME"],
                    assistant_phone = contact["PHONE_ASSISTANT"],
                    email = contact["EMAIL_ADDRESS"],
                    phone = contact["PHONE"],
                    mailing_street = contact["ADDRESS_MAIL_STREET"],
                    mailing_city = contact["ADDRESS_MAIL_CITY"],
                    mailing_state = contact["ADDRESS_MAIL_STATE"],
                    mailing_postal_code = contact["ADDRESS_MAIL_POSTCODE"],
                    mailing_country = contact["ADDRESS_MAIL_COUNTRY"],
                    other_city = contact["ADDRESS_OTHER_CITY"],
                    other_country = contact["ADDRESS_OTHER_COUNTRY"],
                    other_postal_code = contact["ADDRESS_OTHER_POSTCODE"],
                    other_state = contact["ADDRESS_OTHER_STATE"],
                    other_street = contact["ADDRESS_OTHER_STREET"],
                    description = contact["BACKGROUND"],
                    phone_mobile = contact["PHONE_MOBILE"],
                    date_of_birth = contact["DATE_OF_BIRTH"],
                    title = contact["TITLE"],
                    fax = contact["PHONE_FAX"],
                    phone_home = contact["PHONE_HOME"],
                    phone_other = contact["PHONE_OTHER"],
                    twitter = contact["SOCIAL_TWITTER"],
                    email_opted_out = contact["EMAIL_OPTED_OUT"],
                    facebook = contact["SOCIAL_FACEBOOK"],
                    linkedin = contact["SOCIAL_LINKEDIN"],
                    owner_id = contact['OWNER_USER_ID'],
                    organization_id = contact["ORGANISATION_ID"],
                    tags = contact["TAGS"]
                )
                contacts.append(insightly_contact.__dict__)
        return json.dumps(contacts)

    def new_deals_by_date_range(self, context, params):
        '''Gets a list of deals based on creation date'''

        headers = context['headers']
        method = 'GET'
        url = '/Opportunities'

        opportunities_list = json.loads(util.get_insightly_request(method, url, headers).text)
        opportunities = []

        for opportunity in opportunities_list:
            if int(params["start_date"]) > util.date_format_to_epoch(opportunity['DATE_CREATED_UTC']) and util.date_format_to_epoch(opportunity['DATE_CREATED_UTC']) < int(params["end_date"]):
                insightly_opportunity = InsightlyDeal(
                    opportunity_id = opportunity["OPPORTUNITY_ID"],
                    opportunity_name = opportunity["OPPORTUNITY_NAME"],
                    description = opportunity["OPPORTUNITY_DETAILS"],
                    actual_close_date = opportunity["ACTUAL_CLOSE_DATE"],
                    bid_amount = opportunity["BID_AMOUNT"],
                    bid_currency = opportunity["BID_CURRENCY"],
                    bid_duration = opportunity["BID_DURATION"],
                    bid_type = opportunity["BID_TYPE"],
                    category = opportunity["CATEGORY_ID"],
                    current_state = opportunity["OPPORTUNITY_STATE"],
                    forecast_close_date = opportunity["FORECAST_CLOSE_DATE"],
                    probability_of_winning = opportunity["PROBABILITY"],
                    image = opportunity["IMAGE_URL"],
                    user_responsible_id = opportunity["RESPONSIBLE_USER_ID"],
                    opportunity_owner_id = opportunity["OWNER_USER_ID"],
                    organization_id = opportunity["ORGANISATION_ID"],
                    tags = opportunity["TAGS"]
                )
                opportunities.append(insightly_opportunity.__dict__)
        return json.dumps(opportunities)

    def new_tasks_by_date_range(self, context, params):
        '''Gets a list of tasks based on creation date'''

        headers = context['headers']
        method = 'GET'
        url = '/Tasks'

        task_list = json.loads(util.get_insightly_request(method, url, headers).text)
        tasks = []

        for task in task_list:
            if int(params["start_date"]) > util.date_format_to_epoch(task['DATE_CREATED_UTC']) and util.date_format_to_epoch(task['DATE_CREATED_UTC']) < int(params["end_date"]):
                insightly_task = InsightlyTask(
                    task_id = task["TASK_ID"],
                    task_name = task["TITLE"],
                    date_due = task["DUE_DATE"],
                    category_id = task["CATEGORY_ID"],
                    priority_id = task["PRIORITY"],
                    description = task["DETAILS"],
                    email = task["EMAIL_ID"],
                    completed = task["COMPLETED"],
                    status_id = task["STATUS"],
                    progress = task["PERCENT_COMPLETE"],
                    start_date = task["START_DATE"],
                    assigned_team_id = task["ASSIGNED_TEAM_ID"],
                    milestone_id = task["MILESTONE_ID"],
                    opportunity_id = task["OPPORTUNITY_ID"],
                    project_id = task["PROJECT_ID"],
                    task_owner_id = task["OWNER_USER_ID"]
                )
                tasks.append(insightly_task.__dict__)
        return json.dumps(tasks)
    def new_events_by_date_range(self, context, params):
        '''Gets a list of events based on creation date'''

        headers = context['headers']
        method = 'GET'
        url = '/Events'

        events_list = json.loads(util.get_insightly_request(method, url, headers).text)
        events = []

        for event in events_list:
            if int(params["start_date"]) > util.date_format_to_epoch(event['DATE_CREATED_UTC']) and util.date_format_to_epoch(event['DATE_CREATED_UTC']) < int(params["end_date"]):
                insightly_event = InsightlyEvent(
                    event_id = event["EVENT_ID"],
                    title = event["TITLE"],
                    description = event["DETAILS"],
                    start_date = event["START_DATE_UTC"],
                    end_date = event["END_DATE_UTC"],
                    all_day_event = event["ALL_DAY"],
                    location = event["LOCATION"],
                    reminder_date = event["REMINDER_DATE_UTC"],
                    reminder_sent = event["REMINDER_SENT"],
                    date_added = event["DATE_CREATED_UTC"],
                    date_updated = event["DATE_UPDATED_UTC"],
                    owner_id = event["OWNER_USER_ID"]
                )
                events.append(insightly_event.__dict__)
        return json.dumps(events)

    def updated_accounts_by_date_range(self, context, params):
        '''Gets a list of accounts based on update date'''

        headers = context['headers']
        method = 'GET'
        url = '/Organisations'

        organisations_list = json.loads(util.get_insightly_request(method, url, headers).text)
        organisations = []

        for organisation in organisations_list:
            if int(params["start_date"]) > util.date_format_to_epoch(organisation['DATE_UPDATED_UTC']) and util.date_format_to_epoch(organisation['DATE_UPDATED_UTC']) < int(params["end_date"]):
                insightly_organisation = InsightlyAccount(
                    organization_id = organisation["ORGANISATION_ID"],
                    organization_name = organisation["ORGANISATION_NAME"],
                    description = organisation["BACKGROUND"],
                    billing_city = organisation["ADDRESS_BILLING_CITY"],
                    billing_country = organisation["ADDRESS_BILLING_COUNTRY"],
                    biiling_postal_code = organisation["ADDRESS_BILLING_POSTCODE"],
                    billing_state = organisation["ADDRESS_BILLING_STATE"],
                    billing_street = organisation["ADDRESS_BILLING_STREET"],
                    facebook = organisation["SOCIAL_FACEBOOK"],
                    linkedin = organisation["SOCIAL_LINKEDIN"],
                    twitter = organisation["SOCIAL_TWITTER"],
                    fax = organisation["PHONE_FAX"],
                    phone = organisation["PHONE"],
                    shipping_city = organisation["ADDRESS_SHIP_CITY"],
                    shipping_country = organisation["ADDRESS_SHIP_COUNTRY"],
                    shipping_postal_code = organisation["ADDRESS_SHIP_POSTCODE"],
                    shipping_state = organisation["ADDRESS_SHIP_STATE"],
                    shipping_street = organisation["ADDRESS_SHIP_STREET"],
                    image = organisation["IMAGE_URL"],
                    tags = organisation["TAGS"],
                    email_domains = organisation["EMAILDOMAINS"],
                    opportunity_owner_id = organisation["OWNER_USER_ID"]
                )
                organisations.append(insightly_organisation.__dict__)
        return json.dumps(organisations)

    def updated_contacts_by_date_range(self, context, params):
        '''Gets a list of contacts based on update date'''

        headers = context['headers']
        method = 'GET'
        url = '/Contacts'

        contact_list = json.loads(util.get_insightly_request(method, url, headers).text)
        contacts = []

        for contact in contact_list:
            if int(params["start_date"]) > util.date_format_to_epoch(contact['DATE_UPDATED_UTC']) and util.date_format_to_epoch(contact['DATE_UPDATED_UTC']) < int(params["end_date"]):
                insightly_contact = InsightlyContact(
                    contact_id = contact["CONTACT_ID"],
                    prefix = contact["SALUTATION"],
                    last_name = contact["LAST_NAME"],
                    first_name = contact["FIRST_NAME"],
                    assistant_name = contact["ASSISTANT_NAME"],
                    assistant_phone = contact["PHONE_ASSISTANT"],
                    email = contact["EMAIL_ADDRESS"],
                    phone = contact["PHONE"],
                    mailing_street = contact["ADDRESS_MAIL_STREET"],
                    mailing_city = contact["ADDRESS_MAIL_CITY"],
                    mailing_state = contact["ADDRESS_MAIL_STATE"],
                    mailing_postal_code = contact["ADDRESS_MAIL_POSTCODE"],
                    mailing_country = contact["ADDRESS_MAIL_COUNTRY"],
                    other_city = contact["ADDRESS_OTHER_CITY"],
                    other_country = contact["ADDRESS_OTHER_COUNTRY"],
                    other_postal_code = contact["ADDRESS_OTHER_POSTCODE"],
                    other_state = contact["ADDRESS_OTHER_STATE"],
                    other_street = contact["ADDRESS_OTHER_STREET"],
                    description = contact["BACKGROUND"],
                    phone_mobile = contact["PHONE_MOBILE"],
                    date_of_birth = contact["DATE_OF_BIRTH"],
                    title = contact["TITLE"],
                    fax = contact["PHONE_FAX"],
                    phone_home = contact["PHONE_HOME"],
                    phone_other = contact["PHONE_OTHER"],
                    twitter = contact["SOCIAL_TWITTER"],
                    email_opted_out = contact["EMAIL_OPTED_OUT"],
                    facebook = contact["SOCIAL_FACEBOOK"],
                    linkedin = contact["SOCIAL_LINKEDIN"],
                    owner_id = contact['OWNER_USER_ID'],
                    organization_id = contact["ORGANISATION_ID"],
                    tags = contact["TAGS"]
                )
                contacts.append(insightly_contact.__dict__)
        return json.dumps(contacts)

    def updated_deals_by_date_range(self, context, params):
        '''Gets a list of deals based on update date'''

        headers = context['headers']
        method = 'GET'
        url = '/Opportunities'

        opportunities_list = json.loads(util.get_insightly_request(method, url, headers).text)
        opportunities = []

        for opportunity in opportunities_list:
            if int(params["start_date"]) > util.date_format_to_epoch(opportunity['DATE_UPDATED_UTC']) and util.date_format_to_epoch(opportunity['DATE_UPDATED_UTC']) < int(params["end_date"]):
                insightly_opportunity = InsightlyDeal(
                    opportunity_id = opportunity["OPPORTUNITY_ID"],
                    opportunity_name = opportunity["OPPORTUNITY_NAME"],
                    description = opportunity["OPPORTUNITY_DETAILS"],
                    actual_close_date = opportunity["ACTUAL_CLOSE_DATE"],
                    bid_amount = opportunity["BID_AMOUNT"],
                    bid_currency = opportunity["BID_CURRENCY"],
                    bid_duration = opportunity["BID_DURATION"],
                    bid_type = opportunity["BID_TYPE"],
                    category = opportunity["CATEGORY_ID"],
                    current_state = opportunity["OPPORTUNITY_STATE"],
                    forecast_close_date = opportunity["FORECAST_CLOSE_DATE"],
                    probability_of_winning = opportunity["PROBABILITY"],
                    image = opportunity["IMAGE_URL"],
                    user_responsible_id = opportunity["RESPONSIBLE_USER_ID"],
                    opportunity_owner_id = opportunity["OWNER_USER_ID"],
                    organization_id = opportunity["ORGANISATION_ID"],
                    tags = opportunity["TAGS"]
                )
                opportunities.append(insightly_opportunity.__dict__)
        return json.dumps(opportunities)

    def updated_tasks_by_date_range(self, context, params):
        '''Gets a list of tasks based on update date'''

        headers = context['headers']
        method = 'GET'
        url = '/Tasks'

        task_list = json.loads(util.get_insightly_request(method, url, headers).text)
        tasks = []

        for task in task_list:
            if int(params["start_date"]) > util.date_format_to_epoch(task['DATE_UPDATED_UTC']) and util.date_format_to_epoch(task['DATE_UPDATED_UTC']) < int(params["end_date"]):
                insightly_task = InsightlyTask(
                    task_id = task["TASK_ID"],
                    task_name = task["TITLE"],
                    date_due = task["DUE_DATE"],
                    category_id = task["CATEGORY_ID"],
                    priority_id = task["PRIORITY"],
                    description = task["DETAILS"],
                    email = task["EMAIL_ID"],
                    completed = task["COMPLETED"],
                    status_id = task["STATUS"],
                    progress = task["PERCENT_COMPLETE"],
                    start_date = task["START_DATE"],
                    assigned_team_id = task["ASSIGNED_TEAM_ID"],
                    milestone_id = task["MILESTONE_ID"],
                    opportunity_id = task["OPPORTUNITY_ID"],
                    project_id = task["PROJECT_ID"],
                    task_owner_id = task["OWNER_USER_ID"]
                )
                tasks.append(insightly_task.__dict__)
        return json.dumps(tasks)

    def updated_events_by_date_range(self, context, params):
        '''Gets a list of events based on update date'''

        headers = context['headers']
        method = 'GET'
        url = '/Events'

        events_list = json.loads(util.get_insightly_request(method, url, headers).text)
        events = []

        for event in events_list:
            if int(params["start_date"]) > util.date_format_to_epoch(event['DATE_UPDATED_UTC']) and util.date_format_to_epoch(event['DATE_UPDATED_UTC']) < int(params["end_date"]):
                insightly_event = InsightlyEvent(
                    event_id = event["EVENT_ID"],
                    title = event["TITLE"],
                    description = event["DETAILS"],
                    start_date = event["START_DATE_UTC"],
                    end_date = event["END_DATE_UTC"],
                    all_day_event = event["ALL_DAY"],
                    location = event["LOCATION"],
                    reminder_date = event["REMINDER_DATE_UTC"],
                    reminder_sent = event["REMINDER_SENT"],
                    date_added = event["DATE_CREATED_UTC"],
                    date_updated = event["DATE_UPDATED_UTC"],
                    owner_id = event["OWNER_USER_ID"]
                )
                events.append(insightly_event.__dict__)
        return json.dumps(events)
