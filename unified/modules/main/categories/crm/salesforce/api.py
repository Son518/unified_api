from crm.salesforce import util
from crm.salesforce.entities.salesforce_contact import SalesforceContact
from crm.salesforce.entities.salesforce_account import SalesforceAccount
from crm.salesforce.entities.salesforce_opportunity import SalesforceOpportunity
from crm.salesforce.entities.salesforce_lead import SalesforceLead
from crm.salesforce.entities.salesforce_event import SalesforceEvent
from crm.salesforce.entities.salesforce_task import SalesforceTask
from crm.salesforce.entities.salesforce_note import SalesforceNote
import json


class SalesforceApi:

    @staticmethod
    def get_contact_data(contact):
        """ utility function for parsing contact obj from payload and return as dict """

        contact_data = SalesforceContact(
            contact_id=contact.get("Id"),
            salutation=contact.get("Salutation"),
            owner_id=contact.get("OwnerId"),
            last_name=contact.get("LastName"),
            first_name=contact.get("FirstName"),
            account_id=contact.get("AccountId"),
            title=contact.get("Title"),
            department=contact.get("Department"),
            birth_date=contact.get("Birthdate"),
            reports_to=contact.get("ReportsToId"),
            lead_source=contact.get("LeadSource"),
            phone=contact.get("Phone"),
            homephone=contact.get("HomePhone"),
            mobile=contact.get("MobilePhone"),
            other_mobile=contact.get("OtherPhone"),
            fax=contact.get("Fax"),
            email=contact.get("Email"),
            assistant=contact.get("AssistantName"),
            asst_mobile=contact.get("AssistantPhone"),
            mailing_street=contact.get("MailingStreet"),
            mailing_city=contact.get("MailingCity"),
            mailing_state=contact.get("MailingState"),
            mailing_zip=contact.get("MailingPostalCode"),
            mailing_country=contact.get("MailingCountry"),
            other_street=contact.get("OtherStreet"),
            other_city=contact.get("OtherCity"),
            other_state=contact.get("OtherState"),
            other_zip=contact.get("OtherPostalCode"),
            other_country=contact.get("OtherCountry"),
            languages=contact.get("Languages__c"),
            level=contact.get("Level__c"),
            description=contact.get("Description")
        )

        return contact_data.__dict__

    @staticmethod
    def get_account_data(account):
        """ utility function for parsing account obj from payload and return as dict """

        account_data = SalesforceAccount(
            account_id=account.get("Id"),
            account_name=account.get("Name"),
            parent_id=account.get("ParentId"),
            owner_id=account.get("OwnerId"),
            account_number=account.get("AccountNumber"),
            account_site=account.get("Site"),
            type=account.get("Type"),
            industry=account.get("Industry"),
            annual_revenue=account.get("AnnualRevenue"),
            rating=account.get("Rating"),
            phone=account.get("Phone"),
            website=account.get("Website"),
            ticker_symbol=account.get("TickerSymbol"),
            ownership=account.get("Ownership"),
            employees=account.get("NumberOfEmployees"),
            sic_code=account.get("Sic"),
            billing_street=account.get("BillingStreet"),
            billing_city=account.get("BillingCity"),
            billing_zip=account.get("BillingPostalCode"),
            billing_state=account.get("BillingState"),
            billing_country=account.get("BillingCountry"),
            shipping_street=account.get("ShippingStreet"),
            shipping_city=account.get("ShippingCity"),
            shipping_zip=account.get("ShippingPostalCode"),
            shipping_state=account.get("ShippingState"),
            shipping_country=account.get("ShippingCountry"),
            customer_priority=account.get("CustomerPriority__c"),
            end_date=account.get("SLAExpirationDate__c"),
            number_of_locations=account.get("NumberofLocations__c"),
            active=account.get("Active__c"),
            sla=account.get("SLA__c"),
            sla_serial_number=account.get("SLASerialNumber__c"),
            upsell_opportunity=account.get("UpsellOpportunity__c"),
            description=account.get("Description")
        )

        return account_data.__dict__

    @staticmethod
    def get_deal_data(opportunity):
        """ utility function for parsing opportunity obj from payload and return as dict """

        deal_data = SalesforceOpportunity(
            opportunity_id=opportunity.get("Id"),
            account_id=opportunity.get("AccountId"),
            owner_id=opportunity.get("OwnerId"),
            probability=opportunity.get("Probability"),
            private=opportunity.get("IsPrivate"),
            amount=opportunity.get("Amount"),
            opportunity_name=opportunity.get("Name"),
            end_date=opportunity.get("CloseDate"),
            type=opportunity.get("Type"),
            lead_source=opportunity.get("LeadSource"),
            next_step=opportunity.get("NextStep"),
            stage=opportunity.get("StageName"),
            order_number=opportunity.get("OrderNumber__c"),
            current_generator=opportunity.get("CurrentGenerators__c"),
            tracking_number=opportunity.get("TrackingNumber__c"),
            main_competitor=opportunity.get("MainCompetitors__c"),
            delivery_status=opportunity.get("DeliveryInstallationStatus__c"),
            description=opportunity.get("Description")
        )

        return deal_data.__dict__

    @staticmethod
    def get_lead_data(lead):
        """ utility function for parsing lead obj from payload and return as dict """

        lead_data = SalesforceLead(
            lead_id=lead.get("Id"),
            salutation=lead.get("Salutation"),
            last_name=lead.get("LastName"),
            first_name=lead.get("FirstName"),
            owner_id=lead.get("OwnerId"),
            company=lead.get("Company"),
            title=lead.get("Title"),
            lead_source=lead.get("LeadSource"),
            industry=lead.get("Industry"),
            annual_revenue=lead.get("AnnualRevenue"),
            phone=lead.get("Phone"),
            mobile=lead.get("MobilePhone"),
            fax=lead.get("Fax"),
            email=lead.get("Email"),
            website=lead.get("Website"),
            lead_status=lead.get("Status"),
            rating=lead.get("Rating"),
            no_employees=lead.get("NumberOfEmployees"),
            product_interest=lead.get("ProductInterest__c"),
            sic_code=lead.get("SICCode__c"),
            current_generator=lead.get("CurrentGenerators__c"),
            no_locations=lead.get("NumberofLocations__c"),
            street=lead.get("Street"),
            city=lead.get("City"),
            postal_code=lead.get("PostalCode"),
            country=lead.get("Country"),
            state=lead.get("State"),
            primary=lead.get("Primary__c"),
            description=lead.get("Description")
        )

        return lead_data.__dict__

    @staticmethod
    def get_event_data(event):
        """ utility function for parsing event obj from payload and return as dict """

        event_data = SalesforceEvent(
            event_id=event.get("Id"),
            subject=event.get("Subject"),
            start_date=event.get("StartDateTime"),
            end_date=event.get("EndDateTime"),
            all_day_event=event.get("IsAllDayEvent"),
            name_id=event.get("WhoId"),
            related_to=event.get("WhatId"),
            assigned_to=event.get("OwnerId"),
            location=event.get("Location")
        )

        return event_data.__dict__

    @staticmethod
    def get_task_data(task):
        """ utility function for parsing task obj from payload and return as dict """

        task_data = SalesforceTask(
            task_id=task.get("Id"),
            subject=task.get("Subject"),
            end_date=task.get("ActivityDate"),
            name_id=task.get("WhoId"),
            related_to=task.get("WhatId"),
            assigned_to=task.get("OwnerId"),
            status=task.get("Status")
        )

        return task_data.__dict__

    @staticmethod
    def get_note_data(note):
        """ utility function for parsing note obj from payload and return as dict """

        note_data = SalesforceNote(
            note_id=note.get("Id"),
            body=note.get("Body"),
            parent=note.get("ParentId"),
            title=note.get("Title"),
            owner_id=note.get("OwnerId"),
            private=note.get("IsPrivate")
        )

        return note_data.__dict__

    def contact(self, context, params):
        """ Search a contact by ID """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"sobjects/Contact/{params['contact_id']}"
        response = util.rest("GET", url, access_token)
        contact = json.loads(
            response.text
        )

        if response.status_code != 200 or contact.get("objectDescribe"):
            return contact

        return self.get_contact_data(contact)

    def contacts(self, context, params):
        """ Get list of all contacts """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"query/?q=SELECT+FIELDS(ALL)+FROM+Contact+LIMIT+200"
        response = util.rest("GET", url, access_token)
        contacts_list = json.loads(response.text)['records']
        contacts = []

        for contact in contacts_list:
            contacts.append(self.get_contact_data(contact))

        return json.dumps(contacts)

    def contact_by_name(self, context, params):
        """ Search a contact by full name (First name + Contact name) """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Contact+WHERE+" \
                                      f"Name='{params['contact_name']}'+LIMIT+200"
        response = util.rest("GET", url, access_token)
        contacts_list = json.loads(response.text)['records']

        if len(contacts_list) == 0:
            return json.loads(response.text)

        contacts = []

        for contact in contacts_list:
            contacts.append(self.get_contact_data(contact))

        return json.dumps(contacts)

    def contact_by_email(self, context, params):
        """ Search a contact by Email """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Contact+WHERE+" \
                                      f"Email='{params['email']}'+LIMIT+200"
        response = util.rest("GET", url, access_token)
        contacts_list = json.loads(response.text)['records']

        if len(contacts_list) == 0:
            return json.loads(response.text)

        contacts = []

        for contact in contacts_list:
            contacts.append(self.get_contact_data(contact))

        return json.dumps(contacts)
    
    def contacts_by_phone_number(self, context, params):
        """ Search a contact by phone """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Contact+WHERE+" \
                                      f"Phone='{params['phone_number']}'+LIMIT+200"
        response = util.rest("GET", url, access_token)
        contacts_list = json.loads(response.text)['records']

        if len(contacts_list) == 0:
            return json.loads(response.text)

        contacts = []

        for contact in contacts_list:
            contacts.append(self.get_contact_data(contact))

        return json.dumps(contacts)

    def new_contacts_by_date_range(self, context, params):
        """ Get contacts created between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Contact+WHERE+" \
                                      f"CreatedDate>={start_date}+AND+CreatedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        contacts_list = json.loads(response.text)['records']

        if len(contacts_list) == 0:
            return json.loads(response.text)

        contacts = []

        for contact in contacts_list:
            contacts.append(self.get_contact_data(contact))

        return json.dumps(contacts)

    def updated_contacts_by_date_range(self, context, params):
        """ Get contacts Updated between provided Start date time & End date time"""

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Contact+WHERE+" \
                                      f"LastModifiedDate>={start_date}+AND+LastModifiedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        contacts_list = json.loads(response.text)['records']

        if len(contacts_list) == 0:
            return json.loads(response.text)

        contacts = []

        for contact in contacts_list:
            contacts.append(self.get_contact_data(contact))

        return json.dumps(contacts)

    def account(self, context, params):
        """ Search an account by ID """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"sobjects/Account/{params['account_id']}"
        response = util.rest("GET", url, access_token)
        account = json.loads(
            response.text
        )

        if response.status_code != 200 or account.get("objectDescribe"):
            return account

        return self.get_account_data(account)

    def accounts(self, context, params):
        """ Get list of all accounts """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"query/?q=SELECT+FIELDS(ALL)+FROM+Account+LIMIT+200"
        response = util.rest("GET", url, access_token)
        accounts_list = json.loads(response.text)['records']
        accounts = []

        for account in accounts_list:
            accounts.append(self.get_account_data(account))

        return json.dumps(accounts)

    def account_by_name(self, context, params):
        """ Search an account by Name """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Account+WHERE+" \
                                      f"Name='{params['account_name']}'+LIMIT+200"
        response = util.rest("GET", url, access_token)
        accounts_list = json.loads(response.text)['records']

        if len(accounts_list) == 0:
            return json.loads(response.text)

        accounts = []

        for account in accounts_list:
            accounts.append(self.get_account_data(account))

        return json.dumps(accounts)

    def new_accounts_by_date_range(self, context, params):
        """ Get accounts created between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Account+WHERE+" \
                                      f"CreatedDate>={start_date}+AND+CreatedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        accounts_list = json.loads(response.text)['records']

        if len(accounts_list) == 0:
            return json.loads(response.text)

        accounts = []

        for account in accounts_list:
            accounts.append(self.get_account_data(account))

        return json.dumps(accounts)

    def updated_accounts_by_date_range(self, context, params):
        """ Get accounts updated between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Account+WHERE+" \
                                      f"LastModifiedDate>={start_date}+AND+LastModifiedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        accounts_list = json.loads(response.text)['records']

        if len(accounts_list) == 0:
            return json.loads(response.text)

        accounts = []

        for account in accounts_list:
            accounts.append(self.get_account_data(account))

        return json.dumps(accounts)

    def deal(self, context, params):
        """ Search a deal by ID """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"sobjects/Opportunity/{params['deal_id']}"
        response = util.rest("GET", url, access_token)
        deal = json.loads(
            response.text
        )

        if response.status_code != 200 or deal.get("objectDescribe"):
            return deal

        return self.get_deal_data(deal)

    def deals(self, context, params):
        """ Get list of all deals """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"query/?q=SELECT+FIELDS(ALL)+FROM+Opportunity+LIMIT+200"
        response = util.rest("GET", url, access_token)
        deals_list = json.loads(response.text)['records']
        deals = []

        for deal in deals_list:
            deals.append(self.get_deal_data(deal))

        return json.dumps(deals)

    def deal_by_name(self, context, params):
        """ Search a deal by name """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Opportunity+WHERE+" \
                                      f"Name='{params['deal_name']}'+LIMIT+200"
        response = util.rest("GET", url, access_token)
        deals_list = json.loads(response.text)['records']

        if len(deals_list) == 0:
            return json.loads(response.text)

        deals = []

        for deal in deals_list:
            deals.append(self.get_deal_data(deal))

        return json.dumps(deals)

    def new_deals_by_date_range(self, context, params):
        """ Get deals created  between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Opportunity+WHERE+" \
                                      f"CreatedDate>={start_date}+AND+CreatedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        deals_list = json.loads(response.text)['records']

        if len(deals_list) == 0:
            return json.loads(response.text)

        deals = []

        for deal in deals_list:
            deals.append(self.get_deal_data(deal))

        return json.dumps(deals)

    def updated_deals_by_date_range(self, context, params):
        """ Get deals Updated between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Opportunity+WHERE+" \
                                      f"LastModifiedDate>={start_date}+AND+LastModifiedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        deals_list = json.loads(response.text)['records']

        if len(deals_list) == 0:
            return json.loads(response.text)

        deals = []

        for deal in deals_list:
            deals.append(self.get_deal_data(deal))

        return json.dumps(deals)

    def lead(self, context, params):
        """ Search a lead by ID """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + f"sobjects/Lead/{params['lead_id']}"
        response = util.rest("GET", url, access_token)
        lead = json.loads(
            response.text
        )

        if response.status_code != 200 or lead.get("objectDescribe"):
            return lead

        return self.get_lead_data(lead)

    def leads(self, context, params):
        """ Get list of all leads """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Lead+LIMIT+200"
        response = util.rest("GET", url, access_token)
        leads_list = json.loads(response.text)['records']
        leads = []

        for lead in leads_list:
            leads.append(self.get_lead_data(lead))

        return json.dumps(leads)

    def new_leads_by_date_range(self, context, params):
        """ Get leads created between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Lead+WHERE+" \
                                      f"CreatedDate>={start_date}+AND+CreatedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        leads_list = json.loads(response.text)['records']

        if len(leads_list) == 0:
            return json.loads(response.text)

        leads = []

        for lead in leads_list:
            leads.append(self.get_lead_data(lead))

        return json.dumps(leads)

    def updated_leads_by_date_range(self, context, params):
        """ Get leads Updated between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Lead+WHERE+" \
                                      f"LastModifiedDate>={start_date}+AND+LastModifiedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        leads_list = json.loads(response.text)['records']

        if len(leads_list) == 0:
            return json.loads(response.text)

        leads = []

        for lead in leads_list:
            leads.append(self.get_lead_data(lead))

        return json.dumps(leads)

    def tasks(self, context, params):
        """ Get list of all tasks """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Task+LIMIT+200"
        response = util.rest("GET", url, access_token)
        tasks_list = json.loads(response.text)['records']
        tasks = []

        for task in tasks_list:
            tasks.append(self.get_task_data(task))

        return json.dumps(tasks)

    def events(self, context, params):
        """ Get list of all events """

        access_token = util.get_access_token(context['headers'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Event+LIMIT+200"
        response = util.rest("GET", url, access_token)
        events_list = json.loads(response.text)['records']
        events = []

        for event in events_list:
            events.append(self.get_event_data(event))

        return json.dumps(events)

    def new_tasks_by_date_range(self, context, params):
        """ Get tasks created between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Task+WHERE+" \
                                      f"CreatedDate>={start_date}+AND+CreatedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        tasks_list = json.loads(response.text)['records']

        if len(tasks_list) == 0:
            return json.loads(response.text)

        tasks = []

        for task in tasks_list:
            tasks.append(self.get_task_data(task))

        return json.dumps(tasks)

    def updated_tasks_by_date_range(self, context, params):
        """ Get tasks Updated between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Task+WHERE+" \
                                      f"LastModifiedDate>={start_date}+AND+LastModifiedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        tasks_list = json.loads(response.text)['records']

        if len(tasks_list) == 0:
            return json.loads(response.text)

        tasks = []

        for task in tasks_list:
            tasks.append(self.get_task_data(task))

        return json.dumps(tasks)

    def new_events_by_date_range(self, context, params):
        """ Get events created between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Event+WHERE+" \
                                      f"CreatedDate>={start_date}+AND+CreatedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        events_list = json.loads(response.text)['records']

        if len(events_list) == 0:
            return json.loads(response.text)

        events = []

        for event in events_list:
            events.append(self.get_event_data(event))

        return json.dumps(events)

    def updated_events_by_date_range(self, context, params):
        """ Get events Updated between provided Start date time & End date time """

        access_token = util.get_access_token(context['headers'])
        start_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['start_date'])
        end_date = util.epoch_to_format('%Y-%m-%dT%H:%M:%SZ', params['end_date'])
        url = util.get_url(context) + "query/?q=SELECT+FIELDS(ALL)+FROM+Event+WHERE+" \
                                      f"LastModifiedDate>={start_date}+AND+LastModifiedDate<={end_date}+LIMIT+200"
        response = util.rest("GET", url, access_token)
        events_list = json.loads(response.text)['records']

        if len(events_list) == 0:
            return json.loads(response.text)

        events = []

        for event in events_list:
            events.append(self.get_event_data(event))

        return json.dumps(events)
