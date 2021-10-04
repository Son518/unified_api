from crm.zoho_crm import util
from unified.core.actions import Actions
from crm.entities.account import Account
from crm.zoho_crm.entities.zohocrm_contact import ZohocrmContact
from crm.zoho_crm.entities.zohocrm_account import ZohocrmAccount
from crm.zoho_crm.entities.zohocrm_deal import ZohocrmDeal
from crm.zoho_crm.entities.zohocrm_lead import ZohocrmLead
from crm.zoho_crm.entities.zohocrm_note import ZohocrmNote
from crm.zoho_crm.entities.zohocrm_tag import ZohocrmTag
import json


class ZohocrmActions(Actions):

    def create_contact(self, context, payload):
        '''creates a new contact'''

        access_token = util.get_access_token(context['headers'])
        contact = ZohocrmContact(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])
        url = f"https://www.zohoapis.{data_center}/crm/v2/Contacts"
        contact_body = {
            "data": [
                {
                    "Last_Name": contact.last_name,
                    "First_Name": contact.first_name,
                    "Email": contact.email,
                    "Mailing_State": contact.mailing_state,
                    "Mailing_Country": contact.mailing_country,
                    "Mailing_Zip": contact.mailing_zip,
                    "Mailing_Street": contact.mailing_street,
                    "Phone": contact.business_phone,
                    "Description": contact.description,
                    "Department": contact.department,
                    "Lead_Source": contact.lead_source_id,
                    "Mobile": contact.mobile,
                    "Date_of_Birth": contact.date_of_birth,
                    "Title": contact.title,
                    "Salutation": contact.salutation,
                    "Fax": contact.fax,
                    "Home_Phone": contact.home_phone,
                    "Other_Phone": contact.other_phone,
                    "Reporting_To": contact.report_to_id,
                    "Skype_ID": contact.skype_id,
                    "Twitter": contact.twitter,
                    "Asst_Phone": contact.assistant_phone,
                    "Assistant": contact.assistant_name,
                    "Email_Opt_Out": contact.email_opt_out
                }
            ]
        }
        if contact.owner_id:
            contact_body['Owner'] = { "id" : contact.owner_id }

        if contact.account_id:
            contact_body['Account_Name'] = { "id" : contact.account_id }

        response = util.rest("POST", url, access_token, contact_body)
        res_obj = json.loads(response.text)

        if response.status_code == 201:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def create_deal(self, context, payload):
        '''creates new deal'''

        access_token = util.get_access_token(context['headers'])
        deal = ZohocrmDeal(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Deals"
        deal_body = {
            "data": [
                {
                    "Lead_Source": deal.lead_source_id,
                    "Type": deal.type,
                    "Description": deal.description,
                    "Deal_Name": deal.name,
                    "Closing_Date": deal.close_date,
                    "Stage": deal.stage_id,
                    "Amount": deal.value,
                    "Probability": deal.probability,
                    "Account_Name": {
                        "id": deal.account_id
                    }
                }
            ]
        }
        if deal.owner_id:
            deal_body["Owner"]: {"id": deal.owner_id}
        if deal.contact_id:
            deal_body["Contact_Name"]: {"id": deal.contact_id}
        response = util.rest("POST", url, access_token, deal_body)
        res_obj = json.loads(response.text)

        if response.status_code == 201:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def create_account(self, context, payload):
        '''creates new account'''

        access_token = util.get_access_token(context['headers'])
        account = ZohocrmAccount(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Accounts"
        account_body = {
            "data": [
                {
                    "Account_Name": account.name,
                    "Account_Number": account.phone,
                    "Account_Site": account.website,
                    "Description": account.description,
                    "Billing_City": account.billing_city,
                    "Billing_Code": account.billing_zip,
                    "Billing_Country": account.billing_country,
                    "Billing_State": account.billing_state,
                    "Billing_Street": account.billing_street,
                    "Other_State": account.mailing_state,
                    "Other_Country": account.mailing_country,
                    "Other_Zip": account.mailing_zip,
                    "Other_Street": account.mailing_street,
                    "Other_City": account.mailing_city,
                    "Fax": account.fax,
                    "Rating": account.rating_id,
                    "Industry": account.industry_id,
                    "Account_Site": account.account_site,
                    "Account_Number": account.account_number
                }
            ]
        }
        if account.owner_id:
            account_body["Owner"]: {"id": account.owner_id}

        if account.parent_account_id:
            account_body["Parent_Account"]: {"id": account.Parent_Account}
        
        response = util.rest("POST", url, access_token, account_body)
        res_obj = json.loads(response.text)

        if response.status_code == 201:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def create_lead(self, context, payload):
        '''creates new lead'''

        access_token = util.get_access_token(context['headers'])
        lead = ZohocrmLead(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Leads"
        lead_body = {
            "data": [
                {
                    "Company": lead.company_name,
                    "Last_Name": lead.last_name,
                    "First_Name": lead.first_name,
                    "Email": lead.email,
                    "State": lead.state,
                    "Country": lead.country_id,
                    "Zip": lead.zip,
                    "Street": lead.street,
                    "Phone": lead.phone,
                    "Description": lead.description,
                    "Lead_Source": lead.lead_source_id,
                    "Industry": lead.industry_id,
                    "Annual_Revenue": lead.annual_revenue,
                    "Fax": lead.fax,
                    "Title": lead.title,
                    "Salutation": lead.salutation,
                    "Lead_Status": lead.lead_status_id,
                    "Rating": lead.rating_id,
                    "No_of_Employees": lead.no_of_Employees,
                    "$currency_symbol": lead.currency_symbol
                }
            ]
        }
        if lead.owner_id:
            lead_body['Owner'] = {"id" : lead.owner_id}

        if lead.account_id:
            lead_body['Account_Name'] = {"id": lead.account_id}

        response = util.rest("POST", url, access_token, lead_body)
        res_obj = json.loads(response.text)

        if response.status_code == 201:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def add_note_to_contact(self, context, payload):
        '''creates new note to contact '''

        payload['parent_id'] = payload['contact_id']
        del payload['contact_id']
        return self.create_note(context, payload)

    def create_note(self, context, payload):
        '''create New note for a module'''

        access_token = util.get_access_token(context['headers'])

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Notes"
        note = ZohocrmNote(**payload)
        note_body = {
            "data": [
                {
                    "Note_Title": note.title,
                    "Note_Content": note.content,
                    "Parent_Id": note.parent_id,
                    "se_module": note.parent_module,
                    "Owner": {
                        "id": note.owner_id
                    }
                }
            ]
        }
        response = util.rest("POST", url, access_token, note_body)
        res_obj = json.loads(response.text)

        if response.status_code == 200 or response.status_code == 201:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def add_tag_to_contact(self, context, payload):
        '''adds tag to contact '''

        payload['module_name'] = "Contacts"
        payload['module_id'] = payload['contact_id']
        del payload['contact_id']
        return self.create_tag(context, payload)

    def create_tag(self, context, payload):
        '''create tag to module '''

        access_token = util.get_access_token(context['headers'])
        tag = ZohocrmTag(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/{tag.module_name}/actions/add_tags?ids={tag.module_id}&tag_names={tag.name}"
        response = util.rest("POST", url, access_token)
        res_obj = json.loads(response.text)

        if response.status_code == 200:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def update_contact(self, context, payload):
        '''updates existing contact '''

        access_token = util.get_access_token(context['headers'])
        contact = ZohocrmContact(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Contacts/{contact.contact_id}"
        contact_body = {
            "data": [
                {
                    "Last_Name": contact.last_name,
                    "First_Name": contact.first_name,
                    "Email": contact.email,
                    "Mailing_State": contact.mailing_state,
                    "Mailing_Country": contact.mailing_country,
                    "Mailing_Zip": contact.mailing_zip,
                    "Mailing_Street": contact.mailing_street,
                    "Phone": contact.business_phone,
                    "Description": contact.description,
                    "Department": contact.department,
                    "Lead_Source": contact.lead_source_id,
                    "Mobile": contact.mobile,
                    "Date_of_Birth": contact.date_of_birth,
                    "Title": contact.title,
                    "Salutation": contact.salutation,
                    "Fax": contact.fax,
                    "Home_Phone": contact.home_phone,
                    "Other_Phone": contact.other_phone,
                    "Reporting_To": contact.report_to_id,
                    "Skype_ID": contact.skype_id,
                    "Twitter": contact.twitter,
                    "Asst_Phone": contact.assistant_phone,
                    "Assistant": contact.assistant_name,
                    "Email_Opt_Out": contact.email_opt_out
                }
            ]
        }
        if contact.owner_id:
            contact_body["Owner"]: {"id": contact.owner_id}

        if contact.contact_id:
            contact_body["Account_Name"]: {"id": contact.account_id}

        response = util.rest("PUT", url, access_token, contact_body)
        res_obj = json.loads(response.text)

        if response.status_code == 200:
            res_obj['id'] = res_obj['data'][0]['details']['id']
        
        return res_obj, response.status_code

    def update_deal(self, context, payload):
        '''update existing deal '''

        access_token = util.get_access_token(context['headers'])
        deal = ZohocrmDeal(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Deals/{deal.deal_id}"
        deal_body = {
            "data": [
                {
                    "Lead_Source": deal.lead_source_id,
                    "Type": deal.type,
                    "Description": deal.description,
                    "Deal_Name": deal.name,
                    "Closing_Date": deal.close_date,
                    "Stage": deal.stage_id,
                    "Amount": deal.value,
                    "Probability": deal.probability,
                    "Account_Name": {
                        "id": deal.account_id
                    }
                }
            ]
        }
        if deal.owner_id:
            deal_body["Owner"]: {"id": deal.owner_id}

        if deal.contact_id:
            deal_body["Contact_Name"]: {"id": deal.contact_id}

        response = util.rest("put", url, access_token, deal_body)
        res_obj = json.loads(response.text)

        if response.status_code == 200:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def update_account(self, context, payload):
        '''creates new account'''

        access_token = util.get_access_token(context['headers'])
        account = ZohocrmAccount(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Accounts/{account.account_id}"
        account_body = {
            "data": [
                {
                    "Account_Name": account.name,
                    "Account_Number": account.phone,
                    "Account_Site": account.website,
                    "Description": account.description,
                    "Billing_City": account.billing_city,
                    "Billing_Code": account.billing_zip,
                    "Billing_Country": account.billing_country,
                    "Billing_State": account.billing_state,
                    "Billing_Street": account.billing_street,
                    "Other_State": account.mailing_state,
                    "Other_Country": account.mailing_country,
                    "Other_Zip": account.mailing_zip,
                    "Other_Street": account.mailing_street,
                    "Other_City": account.mailing_city,
                    "Fax": account.fax,
                    "Rating": account.rating_id,
                    "Industry": account.industry_id,
                    "Account_Site": account.account_site,
                    "Account_Number": account.account_number
                }
            ]
        }
        if account.owner_id:
            account_body["Owner"]: {"id": account.owner_id}
            
        if account.parent_account_id:
            account_body["Parent_Account"]: {"id": account.Parent_Account}

        response = util.rest("PUT", url, access_token, account_body)
        res_obj = json.loads(response.text)

        if response.status_code == 200:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code

    def update_lead(self, context, payload):
        '''updates existing lead'''

        access_token = util.get_access_token(context['headers'])
        lead = ZohocrmLead(**payload)

        if not context.get('headers').get('data_center'):
            raise Exception('Provide data center')

        data_center = util.know_data_center(context['headers']['data_center'])

        url = f"https://www.zohoapis.{data_center}/crm/v2/Leads/{lead.lead_id}"
        lead_body = {
            "data": [
                {
                    "Company": lead.company_name,
                    "Last_Name": lead.last_name,
                    "First_Name": lead.first_name,
                    "Email": lead.email,
                    "State": lead.state,
                    "Country": lead.country_id,
                    "Zip": lead.zip,
                    "Street": lead.street,
                    "Phone": lead.phone,
                    "Description": lead.description,
                    "Lead_Source": lead.lead_source_id,
                    "Industry": lead.industry_id,
                    "Annual_Revenue": lead.annual_revenue,
                    "Fax": lead.fax,
                    "Title": lead.title,
                    "Salutation": lead.salutation,
                    "Lead_Status": lead.lead_status_id,
                    "Rating": lead.rating_id,
                    "No_of_Employees": lead.no_of_Employees,
                    "$currency_symbol": lead.currency_symbol
                }
            ]
        }
        if lead.owner_id:
            lead_body['Owner'] = {"id" : lead.owner_id}

        if lead.account_id:
            lead_body['Account_Name'] = {"id": lead.account_id}

        response = util.rest("PUT", url, access_token, lead_body)
        res_obj = json.loads(response.text)

        if response.status_code == 200:
            res_obj['id'] = res_obj['data'][0]['details']['id']

        return res_obj, response.status_code
