from crm.entities.contact import Contact
from crm.zoho_crm.entities.zohocrm_deal import ZohocrmDeal
from crm.zoho_crm.entities.zohocrm_lead import ZohocrmLead
from crm.entities.account import Account

from crm.zoho_crm import util
import json


class ZohocrmSearch:

    def new_contacts_by_date_range(self, context, params):
        '''Get contacts created  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+05:30"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+05:30"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"
        query = {
            "select_query": f"select Account_Name,Last_Name,First_Name,Email,Mailing_State,Mailing_Country,Mailing_Zip,Mailing_Street,Mailing_City,Phone,Description,Owner from Contacts where Created_Time between '{start_date}' and   '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)

        if response.status_code in [204, 400]:
            raise Exception('No Contacts found')

        contact_list = json.loads(response.text)['data']
        contacts = []
        for contact in contact_list:
            contact_obj = Contact(
                contact_id = contact.get('id'),
                email = contact.get('Email'),
                business_phone = contact.get('Phone'),
                first_name = contact.get('First_Name'),
                last_name = contact.get('Last_Name'),
                owner_id = contact.get('Owner').get('id'),
                description = contact.get('Description'),
                mailing_city = contact.get("Mailing_City"),
                mailing_country = contact.get('Mailing_Country'),
                mailing_state = contact.get('Mailing_State'),
                mailing_zip = contact.get('Mailing_Zip'),
                mailing_street = contact.get('Mailing_Street'),
                account_id = contact.get('Account_Name').get(
                    'id') if contact.get('Account_Name') else None
            )
            contacts.append(contact_obj.__dict__)

        return json.dumps(contacts)
    
    def updated_contacts_by_date_range(self, context, params):
        '''Get contacts updated  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+05:30"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+05:30"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"

        query = {
            "select_query": f"select Account_Name,Last_Name,First_Name,Email,Mailing_State,Mailing_Country,Mailing_Zip,Mailing_Street,Mailing_City,Phone,Description,Owner from Contacts where Modified_Time between '{start_date}' and   '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)

        if response.status_code in [204, 400]:
            raise Exception('No Contacts found')

        contact_list = json.loads(response.text)['data']
        contacts = []
        for contact in contact_list:
            contact_obj = Contact(
                contact_id = contact.get('id'),
                email = contact.get('Email'),
                business_phone = contact.get('Phone'),
                first_name = contact.get('First_Name'),
                last_name = contact.get('Last_Name'),
                owner_id = contact.get('Owner').get('id'),
                description = contact.get('Description'),
                mailing_city = contact.get("Mailing_City"),
                mailing_country = contact.get('Mailing_Country'),
                mailing_state = contact.get('Mailing_State'),
                mailing_zip = contact.get('Mailing_Zip'),
                mailing_street = contact.get('Mailing_Street'),
                account_id = contact.get('Account_Name').get(
                    'id') if contact.get('Account_Name') else None
            )
            contacts.append(contact_obj.__dict__)

        return json.dumps(contacts)

    def new_deals_by_date_range(self, context, params):
        '''Get Deals created  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+05:30"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+05:30"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"

        query = {
            "select_query": f"select Account_Name,Deal_Name,Closing_Date,Description,Stage,Probability,Contact_Name from Deals where Created_Time between '{start_date}' and '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)
        if response.status_code in [204, 400]:
            raise Exception('No Deals found')
        deal_list = json.loads(response.text)['data']
        deals = []
        for deal in deal_list:
            deal_obj = ZohocrmDeal(
                deal_id = deal.get('id'),
                account_id = deal.get('Account_Name').get(
                    'id') if deal.get('Account_Name') else None,
                name = deal.get('Deal_Name'),
                close_date = deal.get('Closing_Date'),
                description = deal.get('Description'),
                stage_id = deal.get('Stage'),
                probability = deal.get('Probability'),
                contact_id = deal.get('Contact_Name').get(
                    'id') if deal.get('Contact_Name') else None
            )
            deals.append(deal_obj.__dict__)

        return json.dumps(deals)

    def updated_deals_by_date_range(self, context, params):
        '''Get deals updated  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+05:30"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+05:30"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"

        query = {
            "select_query": f"select Account_Name,Deal_Name,Closing_Date,Description,Stage,Probability,Contact_Name from Deals where Modified_Time between '{start_date}' and '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)
        if response.status_code in [204, 400]:
            raise Exception('No Deals found')
        deal_list = json.loads(response.text)['data']
        deals = []
        for deal in deal_list:
            deal_obj = ZohocrmDeal(
                deal_id = deal.get('id'),
                account_id = deal.get('Account_Name').get(
                    'id') if deal.get('Account_Name') else None,
                name = deal.get('Deal_Name'),
                close_date = deal.get('Closing_Date'),
                description = deal.get('Description'),
                stage_id = deal.get('Stage'),
                probability = deal.get('Probability'),
                contact_id = deal.get('Contact_Name').get(
                    'id') if deal.get('Contact_Name') else None
            )
            deals.append(deal_obj.__dict__)

        return json.dumps(deals)

    def new_accounts_by_date_range(self, context, params):
        '''Get accounts created  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+05:30"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+05:30"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"

        query = {
            "select_query": f"select Account_Name,Website,Owner,Description,Billing_State,Billing_Country,Billing_Code,Billing_City,Billing_Street,Phone from Accounts where Created_Time between '{start_date}' and   '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)
        accounts_list = json.loads(response.text)['data']
        accounts = []
        for account in accounts_list:
            account_obj = Account(
                account_id = account.get('id'),
                name = account.get('Account_Name'),
                website = account.get('Website'),
                phone = account.get('Phone'),
                owner_id = account.get('Owner').get('id'),
                description = account.get('Description'),
                mailing_city = account.get("Billing_City"),
                mailing_country = account.get('Billing_Country'),
                mailing_state = account.get('Billing_State'),
                mailing_zip = account.get('Billing_Code'),
                mailing_street = account.get('Billing_Street')
            )
            accounts.append(account_obj.__dict__)

        return json.dumps(accounts)

    def updated_accounts_by_date_range(self, context, params):
        '''Get accounts updated  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+05:30"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+05:30"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"

        query = {
            "select_query": f"select Account_Name,Website,Owner,Description,Billing_State,Billing_Country,Billing_Code,Billing_City,Billing_Street,Phone from Accounts where Modified_Time between '{start_date}' and   '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)
        accounts_list = json.loads(response.text)['data']
        accounts = []
        for account in accounts_list:
            account_obj = Account(
                account_id = account.get('id'),
                name = account.get('Account_Name'),
                website = account.get('Website'),
                phone = account.get('Phone'),
                owner_id = account.get('Owner').get('id'),
                description = account.get('Description'),
                mailing_city = account.get("Billing_City"),
                mailing_country = account.get('Billing_Country'),
                mailing_state = account.get('Billing_State'),
                mailing_zip = account.get('Billing_Code'),
                mailing_street = account.get('Billing_Street')
            )
            accounts.append(account_obj.__dict__)

        return json.dumps(accounts)

    def new_leads_by_date_range(self, context, params):
        '''Get leads created  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+00:00"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+00:00"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"

        query = {
            "select_query": f"select Email,Phone,First_Name,Last_Name,Owner,Description,City,Country,State,Zip_Code,Fax,Industry,Annual_Revenue,Salutation from Leads where Created_Time between '{start_date}' and   '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)
        if response.status_code in [204]:
            raise Exception('No lead found')
        lead_list = json.loads(response.text)['data']
        leads = []

        for lead in lead_list:
            lead_obj = ZohocrmLead(
                lead_id = lead.get('id'),
                email = lead.get('Email'),
                phone = lead.get('Phone'),
                first_name = lead.get('First_Name'),
                last_name = lead.get('Last_Name'),
                owner_id = lead.get('Owner').get('id'),
                description = lead.get('Description'),
                city = lead.get("City"),
                country_id = lead.get('Country'),
                state = lead.get('State'),
                zip = lead.get('Zip_Code'),
                street = lead.get('Street'),
                fax = lead.get('Fax'),
                industry_id = lead.get("Industry"),
                annual_revenue = lead.get('Annual_Revenue'),
                account_id = lead.get('Account_Name').get(
                    'id') if lead.get('Account_Name') else None,
                title = lead.get('Title'),
                salutation = lead.get("Salutation")

            )
            leads.append(lead_obj.__dict__)

        return json.dumps(leads)

    def updated_leads_by_date_range(self, context, params):
        '''Get leads updated  between provided Start date time & End date time'''

        access_token = util.get_access_token(context['headers'])
        format = '%Y-%m-%dT%H:%M:%S'
        start_date = f"{util.epoch_to_format(format, params['start_date_time'])}+00:00"
        end_date = f"{util.epoch_to_format(format, params['end_date_time'])}+00:00"

        if not context.get('headers').get('data_center'):
            raise Exception('Please provid data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"

        query = {
            "select_query": f"select Email,Phone,First_Name,Last_Name,Owner,Description,City,Country,State,Zip_Code,Fax,Industry,Annual_Revenue,Salutation from Leads where Modified_Time between '{start_date}' and   '{end_date}'"
        }
        response = util.rest("POST", url, access_token, query)

        if response.status_code in [204]:
            raise Exception('No lead found')

        lead_list = json.loads(response.text)['data']
        leads = []
        for lead in lead_list:
            lead_obj = ZohocrmLead(
                lead_id = lead.get('id'),
                email = lead.get('Email'),
                phone = lead.get('Phone'),
                first_name = lead.get('First_Name'),
                last_name = lead.get('Last_Name'),
                owner_id = lead.get('Owner').get('id'),
                description = lead.get('Description'),
                city = lead.get("City"),
                country_id = lead.get('Country'),
                state = lead.get('State'),
                zip = lead.get('Zip_Code'),
                street = lead.get('Street'),
                fax = lead.get('Fax'),
                industry_id = lead.get("Industry"),
                annual_revenue = lead.get('Annual_Revenue'),
                account_id = lead.get('Account_Name').get(
                    'id') if lead.get('Account_Name') else None,
                title = lead.get('Title'),
                salutation = lead.get("Salutation")

            )
            leads.append(lead_obj.__dict__)

        return json.dumps(leads)
