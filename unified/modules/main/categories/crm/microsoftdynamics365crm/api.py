from crm.microsoftdynamics365crm import util
from crm.microsoftdynamics365crm.entities.dynamics_crm_contact import Microsoftdynamics365crmContact
from crm.microsoftdynamics365crm.entities.dynamics_crm_account import Microsoftdynamics365crmAccount
from crm.microsoftdynamics365crm.entities.dynamics_crm_lead import Microsoftdynamics365crmLead
import json


class Microsoftdynamics365crmApi:

    def contact(self, context, params):
        """ Returns contact's data by provided id """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/contacts({params['contactid']})"

        contact = json.loads(
            util.rest("GET", url, access_token).text
        )

        contact_data = Microsoftdynamics365crmContact(
            contact_id=contact['contactid'],
            first_name=contact['firstname'] if contact.get('firstname') else None,
            last_name=contact['lastname'] if contact.get('lastname') else None,
            job_title=contact['jobtitle'] if contact.get('jobtitle') else None,
            email=contact['emailaddress1'] if contact.get('emailaddress1') else None,
            business_phone=contact['telephone1'] if contact.get('telephone1') else None,
            mobile_phone=contact['telephone2'] if contact.get('telephone2') else None,
            fax=contact['fax'] if contact.get('fax') else None,
            street_1=contact['address1_line1'] if contact.get('address1_line1') else None,
            street_2=contact['address1_line2'] if contact.get('address1_line2') else None,
            street_3=contact['address1_line3'] if contact.get('address1_line3') else None,
            city=contact['address1_city'] if contact.get('address1_city') else None,
            state=contact['address1_stateorprovince'] if contact.get('address1_stateorprovince') else None,
            zip=contact['address1_postalcode'] if contact.get('address1_postalcode') else None,
            country=contact['address1_country'] if contact.get('address1_country') else None
        )

        return contact_data.__dict__

    def contacts(self, context, params):
        """ Returns all contacts data """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/contacts"

        response = util.rest("GET", url, access_token)

        contacts_list = json.loads(response.text)['value']
        contacts = []

        for contact in contacts_list:
            contact_data = Microsoftdynamics365crmContact(
                contact_id=contact['contactid'],
                first_name=contact['firstname'] if contact.get('firstname') else None,
                last_name=contact['lastname'] if contact.get('lastname') else None,
                job_title=contact['jobtitle'] if contact.get('jobtitle') else None,
                email=contact['emailaddress1'] if contact.get('emailaddress1') else None,
                business_phone=contact['telephone1'] if contact.get('telephone1') else None,
                mobile_phone=contact['telephone2'] if contact.get('telephone2') else None,
                fax=contact['fax'] if contact.get('fax') else None,
                street_1=contact['address1_line1'] if contact.get('address1_line1') else None,
                street_2=contact['address1_line2'] if contact.get('address1_line2') else None,
                street_3=contact['address1_line3'] if contact.get('address1_line3') else None,
                city=contact['address1_city'] if contact.get('address1_city') else None,
                state=contact['address1_stateorprovince'] if contact.get('address1_stateorprovince') else None,
                zip=contact['address1_postalcode'] if contact.get('address1_postalcode') else None,
                country=contact['address1_country'] if contact.get('address1_country') else None
            )
            contacts.append(contact_data.__dict__)

        return json.dumps(contacts)

    def contact_by_email(self, context, params):
        """ Returns contact's data by provided email """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/contacts?" \
            f"$filter=emailaddress1 eq '{params['emailaddress1']}'"

        response = util.rest("GET", url, access_token)

        if response.status_code in [204, 400]:
            raise Exception(f"No contacts found by provided email - {params['emailaddress1']}")

        contacts_list = json.loads(response.text)['value']
        contacts = []

        for contact in contacts_list:
            contact_data = Microsoftdynamics365crmContact(
                contact_id=contact['contactid'],
                first_name=contact['firstname'] if contact.get('firstname') else None,
                last_name=contact['lastname'] if contact.get('lastname') else None,
                job_title=contact['jobtitle'] if contact.get('jobtitle') else None,
                email=contact['emailaddress1'] if contact.get('emailaddress1') else None,
                business_phone=contact['telephone1'] if contact.get('telephone1') else None,
                mobile_phone=contact['telephone2'] if contact.get('telephone2') else None,
                fax=contact['fax'] if contact.get('fax') else None,
                street_1=contact['address1_line1'] if contact.get('address1_line1') else None,
                street_2=contact['address1_line2'] if contact.get('address1_line2') else None,
                street_3=contact['address1_line3'] if contact.get('address1_line3') else None,
                city=contact['address1_city'] if contact.get('address1_city') else None,
                state=contact['address1_stateorprovince'] if contact.get('address1_stateorprovince') else None,
                zip=contact['address1_postalcode'] if contact.get('address1_postalcode') else None,
                country=contact['address1_country'] if contact.get('address1_country') else None
            )
            contacts.append(contact_data.__dict__)

        return json.dumps(contacts)
    
    def contacts_by_phone_number(self, context, params):
        """ Returns contact's data by provided Phone number """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/contacts?" \
            f"$filter=telephone1 eq '{params['phone_number']}'"

        response = util.rest("GET", url, access_token)

        if response.status_code in [204, 400]:
            raise Exception(f"No contacts found by provided phone number - {params['phone_number']}")

        contacts_list = json.loads(response.text)['value']
        contacts = []

        for contact in contacts_list:
            contact_data = Microsoftdynamics365crmContact(
                contact_id=contact['contactid'],
                first_name=contact['firstname'] if contact.get('firstname') else None,
                last_name=contact['lastname'] if contact.get('lastname') else None,
                job_title=contact['jobtitle'] if contact.get('jobtitle') else None,
                email=contact['emailaddress1'] if contact.get('emailaddress1') else None,
                business_phone=contact['telephone1'] if contact.get('telephone1') else None,
                mobile_phone=contact['telephone2'] if contact.get('telephone2') else None,
                fax=contact['fax'] if contact.get('fax') else None,
                street_1=contact['address1_line1'] if contact.get('address1_line1') else None,
                street_2=contact['address1_line2'] if contact.get('address1_line2') else None,
                street_3=contact['address1_line3'] if contact.get('address1_line3') else None,
                city=contact['address1_city'] if contact.get('address1_city') else None,
                state=contact['address1_stateorprovince'] if contact.get('address1_stateorprovince') else None,
                zip=contact['address1_postalcode'] if contact.get('address1_postalcode') else None,
                country=contact['address1_country'] if contact.get('address1_country') else None
            )
            contacts.append(contact_data.__dict__)

        return json.dumps(contacts)

    def contact_by_full_name(self, context, params):
        """ Returns contact's data by provided full name """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/contacts?$filter=firstname eq '{params['firstname']}' " \
            f"and lastname eq '{params['lastname']}'"

        response = util.rest("GET", url, access_token)

        if response.status_code in [204, 400]:
            raise Exception(f"No contacts found by provided full name - {params['firstname']} {params['lastname']}")

        contacts_list = json.loads(response.text)['value']
        contacts = []

        for contact in contacts_list:
            contact_data = Microsoftdynamics365crmContact(
                contact_id=contact['contactid'],
                first_name=contact['firstname'] if contact.get('firstname') else None,
                last_name=contact['lastname'] if contact.get('lastname') else None,
                job_title=contact['jobtitle'] if contact.get('jobtitle') else None,
                email=contact['emailaddress1'] if contact.get('emailaddress1') else None,
                business_phone=contact['telephone1'] if contact.get('telephone1') else None,
                mobile_phone=contact['telephone2'] if contact.get('telephone2') else None,
                fax=contact['fax'] if contact.get('fax') else None,
                street_1=contact['address1_line1'] if contact.get('address1_line1') else None,
                street_2=contact['address1_line2'] if contact.get('address1_line2') else None,
                street_3=contact['address1_line3'] if contact.get('address1_line3') else None,
                city=contact['address1_city'] if contact.get('address1_city') else None,
                state=contact['address1_stateorprovince'] if contact.get('address1_stateorprovince') else None,
                zip=contact['address1_postalcode'] if contact.get('address1_postalcode') else None,
                country=contact['address1_country'] if contact.get('address1_country') else None
            )
            contacts.append(contact_data.__dict__)

        return json.dumps(contacts)

    def account(self, context, params):
        """ Returns account's data by provided id """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/accounts({params['accountid']})"

        account = json.loads(
            util.rest("GET", url, access_token).text
        )

        account_data = Microsoftdynamics365crmAccount(
            account_id=account['accountid'],
            name=account['name'] if account.get('name') else None,
            phone=account['telephone1'] if account.get('telephone1') else None,
            fax=account['fax'] if account.get('fax') else None,
            website=account['websiteurl'] if account.get('websiteurl') else None,
            relationship_type=account['customertypecode'] if account.get('customertypecode') else None,
            product_price_list=account['_defaultpricelevelid_value'] if account.get('_defaultpricelevelid_value') else None,
            street_1=account['address1_line1'] if account.get('address1_line1') else None,
            street_2=account['address1_line2'] if account.get('address1_line2') else None,
            street_3=account['address1_line3'] if account.get('address1_line3') else None,
            city=account['address1_city'] if account.get('address1_city') else None,
            state=account['address1_stateorprovince'] if account.get('address1_stateorprovince') else None,
            zip=account['address1_postalcode'] if account.get('address1_postalcode') else None,
            country=account['address1_country'] if account.get('address1_country') else None,
            ownership=account['ownershipcode'] if account.get('ownershipcode') else None,
            description=account['description'] if account.get('description') else None
        )

        return account_data.__dict__

    def accounts(self, context, params):
        """ Returns all accounts data """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/accounts"

        response = util.rest("GET", url, access_token)

        accounts_list = json.loads(response.text)['value']
        accounts = []

        for account in accounts_list:
            account_data = Microsoftdynamics365crmAccount(
                account_id=account['accountid'],
                name=account['name'] if account.get('name') else None,
                phone=account['telephone1'] if account.get('telephone1') else None,
                fax=account['fax'] if account.get('fax') else None,
                website=account['websiteurl'] if account.get('websiteurl') else None,
                relationship_type=account['customertypecode'] if account.get('customertypecode') else None,
                product_price_list=account['_defaultpricelevelid_value'] if account.get('_defaultpricelevelid_value') else None,
                street_1=account['address1_line1'] if account.get('address1_line1') else None,
                street_2=account['address1_line2'] if account.get('address1_line2') else None,
                street_3=account['address1_line3'] if account.get('address1_line3') else None,
                city=account['address1_city'] if account.get('address1_city') else None,
                state=account['address1_stateorprovince'] if account.get('address1_stateorprovince') else None,
                zip=account['address1_postalcode'] if account.get('address1_postalcode') else None,
                country=account['address1_country'] if account.get('address1_country') else None,
                ownership=account['ownershipcode'] if account.get('ownershipcode') else None,
                description=account['description'] if account.get('description') else None
            )
            accounts.append(account_data.__dict__)

        return json.dumps(accounts)

    def account_by_name(self, context, params):
        """ Returns account's data by provided name """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/accounts?$filter=name eq '{params['name']}'"

        response = util.rest("GET", url, access_token)

        if response.status_code in [204, 400]:
            raise Exception(f"No accounts found by provided name {params['name']}")

        accounts_list = json.loads(response.text)['value']
        accounts = []

        for account in accounts_list:
            account_data = Microsoftdynamics365crmAccount(
                account_id=account['accountid'],
                name=account['name'] if account.get('name') else None,
                phone=account['telephone1'] if account.get('telephone1') else None,
                fax=account['fax'] if account.get('fax') else None,
                website=account['websiteurl'] if account.get('websiteurl') else None,
                relationship_type=account['customertypecode'] if account.get('customertypecode') else None,
                product_price_list=account['_defaultpricelevelid_value'] if account.get('_defaultpricelevelid_value') else None,
                street_1=account['address1_line1'] if account.get('address1_line1') else None,
                street_2=account['address1_line2'] if account.get('address1_line2') else None,
                street_3=account['address1_line3'] if account.get('address1_line3') else None,
                city=account['address1_city'] if account.get('address1_city') else None,
                state=account['address1_stateorprovince'] if account.get('address1_stateorprovince') else None,
                zip=account['address1_postalcode'] if account.get('address1_postalcode') else None,
                country=account['address1_country'] if account.get('address1_country') else None,
                ownership=account['ownershipcode'] if account.get('ownershipcode') else None,
                description=account['description'] if account.get('description') else None
            )
            accounts.append(account_data.__dict__)

        return json.dumps(accounts)

    def lead(self, context, params):
        """ Returns lead's data by provided id """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/leads({params['leadid']})"

        lead = json.loads(
            util.rest("GET", url, access_token).text
        )

        lead_data = Microsoftdynamics365crmLead(
            lead_id=lead['leadid'],
            last_name=lead['lastname'] if lead.get('lastname') else None,
            topic=lead['subject'] if lead.get('subject') else None,
            first_name=lead['firstname'] if lead.get('firstname') else None,
            type=lead['msdyn_ordertype'] if lead.get('msdyn_ordertype') else None,
            title=lead['jobtitle'] if lead.get('jobtitle') else None,
            business_phone=lead['telephone1'] if lead.get('telephone1') else None,
            mobile_phone=lead['telephone2'] if lead.get('telephone2') else None,
            email=lead['emailaddress1'] if lead.get('emailaddress1') else None,
            company=lead['companyname'] if lead.get('companyname') else None,
            website=lead['websiteurl'] if lead.get('websiteurl') else None,
            street_1=lead['address1_line1'] if lead.get('address1_line1') else None,
            street_2=lead['address1_line2'] if lead.get('address1_line2') else None,
            street_3=lead['address1_line3'] if lead.get('address1_line3') else None,
            city=lead['address1_city'] if lead.get('address1_city') else None,
            state=lead['address1_stateorprovince'] if lead.get('address1_stateorprovince') else None,
            zip=lead['address1_postalcode'] if lead.get('address1_postalcode') else None,
            country=lead['address1_country'] if lead.get('address1_country') else None,
            industry=lead['industrycode'] if lead.get('industrycode') else None,
            description=lead['description'] if lead.get('description') else None,
            annual_revenue=lead['revenue'] if lead.get('revenue') else None,
            employees=lead['numberofemployees'] if lead.get('numberofemployees') else None,
            sic_code=lead['sic'] if lead.get('sic') else None,
            currency=lead['_transactioncurrencyid_value'] if lead.get('_transactioncurrencyid_value') else None
        )

        return lead_data.__dict__

    def leads(self, context, params):
        """ Returns all leads data """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        url = f"{headers['organization_uri']}/api/data/v9.0/leads"

        response = util.rest("GET", url, access_token)

        leads_list = json.loads(response.text)['value']
        leads = []

        for lead in leads_list:
            lead_data = Microsoftdynamics365crmLead(
                lead_id=lead['leadid'],
                last_name=lead['lastname'] if lead.get('lastname') else None,
                topic=lead['subject'] if lead.get('subject') else None,
                first_name=lead['firstname'] if lead.get('firstname') else None,
                type=lead['msdyn_ordertype'] if lead.get('msdyn_ordertype') else None,
                title=lead['jobtitle'] if lead.get('jobtitle') else None,
                business_phone=lead['telephone1'] if lead.get('telephone1') else None,
                mobile_phone=lead['telephone2'] if lead.get('telephone2') else None,
                email=lead['emailaddress1'] if lead.get('emailaddress1') else None,
                company=lead['companyname'] if lead.get('companyname') else None,
                website=lead['websiteurl'] if lead.get('websiteurl') else None,
                street_1=lead['address1_line1'] if lead.get('address1_line1') else None,
                street_2=lead['address1_line2'] if lead.get('address1_line2') else None,
                street_3=lead['address1_line3'] if lead.get('address1_line3') else None,
                city=lead['address1_city'] if lead.get('address1_city') else None,
                state=lead['address1_stateorprovince'] if lead.get('address1_stateorprovince') else None,
                zip=lead['address1_postalcode'] if lead.get('address1_postalcode') else None,
                country=lead['address1_country'] if lead.get('address1_country') else None,
                industry=lead['industrycode'] if lead.get('industrycode') else None,
                description=lead['description'] if lead.get('description') else None,
                annual_revenue=lead['revenue'] if lead.get('revenue') else None,
                employees=lead['numberofemployees'] if lead.get('numberofemployees') else None,
                sic_code=lead['sic'] if lead.get('sic') else None,
                currency=lead['_transactioncurrencyid_value'] if lead.get('_transactioncurrencyid_value') else None
            )
            leads.append(lead_data.__dict__)

        return json.dumps(leads)
