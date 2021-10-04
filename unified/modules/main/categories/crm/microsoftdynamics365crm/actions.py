from crm.microsoftdynamics365crm import util
from crm.microsoftdynamics365crm.entities.dynamics_crm_contact import Microsoftdynamics365crmContact
from crm.microsoftdynamics365crm.entities.dynamics_crm_account import Microsoftdynamics365crmAccount
from crm.microsoftdynamics365crm.entities.dynamics_crm_lead import Microsoftdynamics365crmLead
from unified.core.actions import Actions


class Microsoftdynamics365crmActions(Actions):

    def create_contact(self, context, payload):
        """ Create new contact """

        headers = context['headers']

        # access_token
        access_token = util.get_access_token(headers)

        contact = Microsoftdynamics365crmContact(**payload)

        url = f"{headers['organization_uri']}/api/data/v9.0/contacts"

        contact_data = {
            "firstname": contact.first_name,
            "lastname": contact.last_name,
            "jobtitle": contact.job_title,
            "emailaddress1": contact.email,
            "telephone1": contact.business_phone,
            "telephone2": contact.mobile_phone,
            "fax": contact.fax,
            "address1_line1": contact.street_1,
            "address1_line2": contact.street_2,
            "address1_line3": contact.street_3,
            "address1_city": contact.city,
            "address1_stateorprovince": contact.state,
            "address1_postalcode": contact.zip,
            "address1_country": contact.country
        }

        response = util.rest("POST", url, access_token, contact_data)

        return response.text, response.status_code

    def create_account(self, context, payload):
        """ Create new account """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        account = Microsoftdynamics365crmAccount(**payload)

        url = f"{headers['organization_uri']}/api/data/v9.0/accounts"

        account_data = {
            "name": account.name,
            "telephone1": account.phone,
            "fax": account.fax,
            "websiteurl": account.website,
            "customertypecode": account.relationship_type,
            "defaultpricelevelid@odata.bind": account.product_price_list,
            "address1_line1": account.street_1,
            "address1_line2": account.street_2,
            "address1_line3": account.street_3,
            "address1_city": account.city,
            "address1_stateorprovince": account.state,
            "address1_postalcode": account.zip,
            "address1_country": account.country,
            "ownershipcode": account.ownership,
            "description": account.description
        }

        response = util.rest("POST", url, access_token, account_data)

        return response.text, response.status_code

    def create_lead(self, context, payload):
        """ Create new lead """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        lead = Microsoftdynamics365crmLead(**payload)

        url = f"{headers['organization_uri']}/api/data/v9.0/leads"

        lead_data = {
            "lastname": lead.last_name,
            "subject": lead.topic,
            "firstname": lead.first_name,
            "msdyn_ordertype": lead.type,
            "jobtitle": lead.title,
            "telephone1": lead.business_phone,
            "telephone2": lead.mobile_phone,
            "emailaddress1": lead.email,
            "companyname": lead.company,
            "websiteurl": lead.website,
            "address1_line1": lead.street_1,
            "address1_line2": lead.street_2,
            "address1_line3": lead.street_3,
            "address1_city": lead.city,
            "address1_stateorprovince": lead.state,
            "address1_postalcode": lead.zip,
            "address1_country": lead.country,
            "description": lead.description,
            "industrycode": lead.industry,
            "revenue": lead.revenue(),
            "numberofemployees": lead.employees,
            "sic": lead.sic_code,
            "transactioncurrencyid@odata.bind": lead.currency
        }

        response = util.rest("POST", url, access_token, lead_data)

        return response.text, response.status_code

    def update_contact(self, context, payload):
        """ Update existing contact """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        contact = Microsoftdynamics365crmContact(**payload)

        url = f"{headers['organization_uri']}/api/data/v9.0/contacts({contact.contact_id})"

        contact_data = {
            "firstname": contact.first_name,
            "lastname": contact.last_name,
            "jobtitle": contact.job_title,
            "emailaddress1": contact.email,
            "telephone1": contact.business_phone,
            "telephone2": contact.mobile_phone,
            "fax": contact.fax,
            "address1_line1": contact.street_1,
            "address1_line2": contact.street_2,
            "address1_line3": contact.street_3,
            "address1_city": contact.city,
            "address1_stateorprovince": contact.state,
            "address1_postalcode": contact.zip,
            "address1_country": contact.country
        }

        response = util.rest("PATCH", url, access_token, contact_data)

        return response.text, response.status_code

    def update_account(self, context, payload):
        """ Update existing account """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        account = Microsoftdynamics365crmAccount(**payload)

        url = f"{headers['organization_uri']}/api/data/v9.0/accounts({account.account_id})"

        account_data = {
            "name": account.name,
            "telephone1": account.phone,
            "fax": account.fax,
            "websiteurl": account.website,
            "customertypecode": account.relationship_type,
            "address1_line1": account.street_1,
            "address1_line2": account.street_2,
            "address1_line3": account.street_3,
            "address1_city": account.city,
            "address1_stateorprovince": account.state,
            "address1_postalcode": account.zip,
            "address1_country": account.country,
            "ownershipcode": account.ownership,
            "description": account.description
        }

        response = util.rest("PATCH", url, access_token, account_data)

        return response.text, response.status_code

    def update_lead(self, context, payload):
        """ Update existing lead """

        headers = context['headers']

        access_token = util.get_access_token(headers)

        lead = Microsoftdynamics365crmLead(**payload)

        print(lead.annual_revenue)

        url = f"{headers['organization_uri']}/api/data/v9.0/leads({lead.lead_id})"

        lead_data = {
            "lastname": lead.last_name,
            "subject": lead.topic,
            "firstname": lead.first_name,
            "msdyn_ordertype": lead.type,
            "jobtitle": lead.title,
            "telephone1": lead.business_phone,
            "telephone2": lead.mobile_phone,
            "emailaddress1": lead.email,
            "companyname": lead.company,
            "websiteurl": lead.website,
            "address1_line1": lead.street_1,
            "address1_line2": lead.street_2,
            "address1_line3": lead.street_3,
            "address1_city": lead.city,
            "address1_stateorprovince": lead.state,
            "address1_postalcode": lead.zip,
            "address1_country": lead.country,
            "description": lead.description,
            "industrycode": lead.industry,
            "revenue": lead.revenue(),
            "numberofemployees": lead.employees,
            "sic": lead.sic_code,
            "transactioncurrencyid@odata.bind": lead.currency
        }

        response = util.rest("PATCH", url, access_token, lead_data)

        return response.text, response.status_code
