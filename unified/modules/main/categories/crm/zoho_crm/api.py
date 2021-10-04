from crm.zoho_crm import util
from crm.entities.account import Account
from crm.entities.contact import Contact
from crm.zoho_crm.entities.zohocrm_lead import ZohocrmLead
from crm.zoho_crm.entities.zohocrm_deal import ZohocrmDeal
import json


class ZohocrmApi:
     
    def accounts(self, context, params):
        '''Get list of all accounts'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])
    
        url = f"https://www.zohoapis.{data_center}/crm/v2/Accounts"
        response = util.rest("GET", url, access_token)
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

    def account(self, context, params):
        '''get account details'''

        access_token = util.get_access_token(context['headers'])
        
        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Accounts/{params['account_id']}"
        response = util.rest("GET", url, access_token)
        account = json.loads(response.text)['data'][0]
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
        return account_obj.__dict__

    def contacts(self, context, params):
        '''get list of all contacts'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Contacts"
        response = util.rest("GET", url, access_token)
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

    def contact(self, context, params):
        '''get contact details'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Contacts/{params['contact_id']}"
        response = util.rest("GET", url, access_token)
        contact = json.loads(response.text)['data'][0]
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

        return contact_obj.__dict__

    def leads(self, context, params):
        '''get list of lead details'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])
        
        url = f"https://www.zohoapis.{data_center}/crm/v2/Leads"
        response = util.rest("GET", url, access_token)
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

    def lead(self, context, params):
        '''get lead details'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Leads/{params['lead_id']}"
        response = util.rest("GET", url, access_token)
        lead = json.loads(response.text)['data'][0]
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
        return lead_obj.__dict__

    def deals(self, context, params):
        '''get list of deal'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])
        
        url = f"https://www.zohoapis.{data_center}/crm/v2/Deals"
        response = util.rest("GET", url, access_token)
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

    def deal(self, context, params):
        '''get deal details'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Deals/{params['deal_id']}"
        response = util.rest("GET", url, access_token)
        deal = json.loads(response.text)['data'][0]
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
        return deal_obj.__dict__

    def contact_by_email(self, context, params):
        '''get contact by email'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"
        query = {
            "select_query": f"select Account_Name,Last_Name,First_Name,Email,Mailing_State,Mailing_Country,Mailing_Zip,Mailing_City,Mailing_Street,Phone,Description,Owner from Contacts where Email = '{params['email']}'"
        }
        response = util.rest("POST", url, access_token, query)

        if response.status_code in [204, 400]:
            raise Exception('No Contacts found for Provided Email')

        contact_list = json.loads(response.text)['data']
        contacts = []
        for contact in contact_list:
            contact_obj = Contact(
                contact_id =contact.get('id'),
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

    def contact_by_name(self, context, params):
        '''get contact by name'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])
        

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"
        query = {
            "select_query": f"select Account_Name,Last_Name,First_Name,Email,Mailing_State,Mailing_Country,Mailing_Zip,Mailing_City,Mailing_Street,Phone,Description,Owner from Contacts where Full_Name = '{params['name']}'"
        }
        response = util.rest("POST", url, access_token, query)

        if response.status_code in [204, 400]:
            raise Exception('No Contacts found for Provided Email')

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

    def account_by_name(self, context, params):
        '''get account by name'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])
        
        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"
        query = {
            "select_query": f"select Account_Name,Website,Owner,Description,Billing_State,Billing_Country,Billing_Code,Billing_City,Billing_Street,Phone from Accounts where Account_Name = '{params['name']}'"
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
        
    def contacts_by_phone(self, context, params):
        '''get contact by phone'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"
        query = {
            "select_query": f"select Account_Name,Last_Name,First_Name,Email,Mailing_State,Mailing_Country,Mailing_Zip,Mailing_City,\
                                Mailing_Street,Phone,Description,Owner from Contacts where Phone = '{params['phone_number']}'"
        }
        response = util.rest("POST", url, access_token, query)

        if response.status_code in [204, 400]:
            raise Exception('No Contacts found for Provided Phone number')

        contact_list = json.loads(response.text)['data']
        contacts = []
        for contact in contact_list:
            contact_obj = Contact(
                contact_id=contact.get('id'),
                email=contact.get('Email'),
                business_phone=contact.get('Phone'),
                first_name=contact.get('First_Name'),
                last_name=contact.get('Last_Name'),
                owner_id=contact.get('Owner').get('id'),
                description=contact.get('Description'),
                mailing_city=contact.get("Mailing_City"),
                mailing_country=contact.get('Mailing_Country'),
                mailing_state=contact.get('Mailing_State'),
                mailing_zip=contact.get('Mailing_Zip'),
                mailing_street=contact.get('Mailing_Street'),
                account_id=contact.get('Account_Name').get(
                    'id') if contact.get('Account_Name') else None
            )
            contacts.append(contact_obj.__dict__)

        return json.dumps(contacts)

    def deal_by_name(self, context, params):
        '''get deal by name'''
        
        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])
        
        url = f"https://www.zohoapis.{data_center}/crm/v2/coql"
        query = {
            "select_query": f"select Account_Name,Deal_Name,Closing_Date,Description,Stage,Probability,Contact_Name from Deals where Deal_Name = '{params['name']}'"
        }
        response = util.rest("POST", url, access_token, query)
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

    def profile(self, context, params):
        '''Details of authenticated user'''
        
        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')
        
        data_center = util.know_data_center(context['headers']['data_center'])
        
        url = f"https://accounts.zoho.{data_center}/oauth/user/info"
        
        response_obj = util.rest("GET", url, access_token)
        response = response_obj.json()
        profile = {
            'id':response['ZUID'],
            'email':response['Email'],
            'name':response['Display_Name']
        }
        return profile      