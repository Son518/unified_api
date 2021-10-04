from . import util
import json
import requests
from marketing_automation.active_campaign.entities.active_campaign_account import ActiveCampaignAccount
from marketing_automation.active_campaign.entities.active_campaign_contact import ActiveCampaignContact
from marketing_automation.active_campaign.entities.active_campaign_deal import ActiveCampaignDeal


class ActiveCampaignApi:

    def get_custom_fields_metadata(self, context):
        """ Get the custom field metadata"""

        resp = util.rest('GET', 'accountCustomFieldMeta', context, None)
        resp = json.loads(resp.text)
        accountCustomFieldData = resp["accountCustomFieldMeta"]
        custom_field_obj = {}

        for custom_field in accountCustomFieldData:
            custom_field_obj[custom_field["id"]] = custom_field["fieldLabel"]

        return custom_field_obj

    def account(self, context, params):
        """ Find account by account name"""

        name = params.get("account_name")
        resp = util.rest('GET', f'accounts?name={name}', context, None)
        
        if len(json.loads(resp.text)["accounts"]) != 0:

            # Get account data
            resp = json.loads(resp.text)["accounts"][0]

            api_token = context['headers']['api_key']
            headers = {
                "Api-Token": f"{api_token}",
                "Content-Type": "application/json"
            }
            
            # Get custom fields metadata
            custom_field_obj = self.get_custom_fields_metadata(context)

            # Get custom field data
            accountCustomFieldData = resp["links"]["accountCustomFieldData"]
            accountCustomFieldData =  accountCustomFieldData.replace("\\", "")
            custom_field_data = requests.request("GET", accountCustomFieldData, headers= headers).text
            custom_field_data = json.loads(custom_field_data)
            custom_field_data = custom_field_data["customerAccountCustomFieldData"]

            data = {}
            data["account_id"] = resp["id"]
            data["name"] = resp["name"]
            data["website"] = resp["accountUrl"]

            for custom_field in custom_field_data:
                field_name = custom_field_obj[custom_field["custom_field_id"]]

                if field_name == 'Address 1':
                    data["address_1"] = custom_field["custom_field_text_value"]  

                if field_name == 'Address 2':
                    data["address_2"] = custom_field["custom_field_text_value"]

                if field_name == 'Annual Revenue':
                    data["annual_revenue"] = custom_field["custom_field_text_value"] 

                if field_name == 'City':
                    data["city"] = custom_field["custom_field_text_value"]   

                if field_name == 'Country':
                    data["country"] = custom_field["custom_field_text_value"] 

                if field_name == 'Description':
                    data["description"] = custom_field["custom_field_text_value"] 
                
                if field_name == 'Industry/Vertical':
                    data["industry"] = custom_field["custom_field_text_value"]

                if field_name == 'Number of Employees':
                    data["number_of_employees"] = custom_field["custom_field_text_value"]

                if field_name == 'Phone Number':
                    data["phone_number"] = custom_field["custom_field_text_value"]

                if field_name == 'Postal Code':
                    data["postal_code"] = custom_field["custom_field_text_value"]

                if field_name == 'State/Province':
                    data["state"] = custom_field["custom_field_text_value"]     
            return data
        return json.loads(resp.text)

    def contact(self, context, params):
        """ Find contact by email id"""

        emailId = params.get("email_id")
        resp = util.rest('GET', f'contacts?email={emailId}', context, None)

        if len(json.loads(resp.text)["contacts"]) != 0:
            resp = json.loads(resp.text)["contacts"][0]
            tag_name = None
            list_id = None
            list_url = resp["links"]["contactLists"]
            list_url = list_url.replace('\\','')

            tag_url = resp["links"]["contactTags"]
            tag_url = tag_url.replace('\\','')

            api_token = context['headers']['api_key']
            headers = {
                "Api-Token": f"{api_token}",
                "Content-Type": "application/json"
            }
            
            # Get list data 
            list_data = requests.request('GET', list_url, headers=headers).text
            list_data = json.loads(list_data)["contactLists"]
            if len(list_data) != 0:
                list_id = list_data[0]["list"]

            # Get tag data
            tag_data = requests.request('GET', tag_url, headers=headers).text
            tag_data = json.loads(tag_data)["contactTags"]

            if len(tag_data) != 0:
                tag = tag_data[0]["links"]["tag"]
                tag = tag.replace('\\','')
                tag = requests.request('GET', tag, headers=headers).text
                tag_name = json.loads(tag)["tag"]["tag"]

            data = ActiveCampaignContact(
                contact_id= resp['id'],
                first_name= resp['firstName'],
                last_name= resp['lastName'],
                email_address= resp['email'],
                phone_number= resp['phone'],
                organization_name= resp['orgname'],
                tags= tag_name,
                list_id = list_id,
                full_name = resp['firstName']+" "+resp['lastName']
            )
            return data.__dict__

        return json.loads(resp.text)

 
    def deal(self, context, params):
        """ Find deal by deal title"""

        resp = util.rest('GET', "deals?limit=100", context, None)

        if len(json.loads(resp.text)["deals"]) != 0:
            for deal in json.loads(resp.text)["deals"]:
                if deal.get("title") == params.get("deal_name"):      
                    account_details = deal['links']['account']      
                    contact_details = deal['links']['contact']      

                    api_token = context['headers']['api_key']
                    headers = {
                        "Api-Token": f"{api_token}",
                        "Content-Type": "application/json"
                    }

                    # Get account data
                    account_data = requests.request('GET', account_details, headers=headers).text
                    account_data = json.loads(account_data)
                    account_id = None
                    if len(account_data) != 0:
                        account_id = account_data["account"]["id"]

                    # Get contact data
                    contact_data = requests.request('GET', contact_details, headers=headers).text
                    contact_data = json.loads(contact_data)
                    contact_email = None
                    if len(account_data) != 0:
                        contact_email = contact_data["contact"]["email"]

                    # Get forecast date
                    contact_data = requests.request('GET', deal["links"]["dealCustomFieldData"], headers=headers).text
                    contact_data = json.loads(contact_data)["dealCustomFieldData"]
                    forecast_date = None                    
                    if len(contact_data)!=0:
                        forecast_date = contact_data[0]["fieldValue"]

                    # Get deal group data
                    deal_Group = requests.request('GET', deal["links"]["group"], headers=headers).text
                    deal_Group = json.loads(deal_Group)["dealGroup"]
                    pipline_id = None
                    pipline_name = None                    
                    if len(deal_Group)!=0:
                        pipline_name = deal_Group["title"]
                        pipline_id = deal_Group["id"]
                        
                    data = ActiveCampaignDeal(
                        deal_id= deal['id'],
                        title= deal['title'],
                        value= deal['value'],
                        owner_id= deal['owner'],
                        currency= deal['currency'],
                        stage= deal['stage'],
                        contact_id= deal['contact'],
                        forecasted_close_date= forecast_date,
                        account_id= account_id,
                        contact_email_address= contact_email,
                        pipeline_title= pipline_name,
                        pipeline_id= pipline_id
                    )
                    return data.__dict__            
            return {"Message":"No deals are found"}
        return json.loads(resp.text)
 
    def deals_by_owner(self, context, params):
        """ Find deal by owner id"""

        resp = util.rest('GET', "deals?limit=100", context, None)
        deals_data = []

        if len(json.loads(resp.text)["deals"]) != 0:
            for deal in json.loads(resp.text)["deals"]:
                if deal.get("owner") == params.get("deal_owner_id"):                    
                    # resp = json.loads(resp.text)["deals"][0]
                    data = ActiveCampaignDeal(
                        deal_id= deal['id'],
                        title= deal['title'],
                        value= deal['value'],
                        owner_id= deal['owner'],
                        currency= deal['currency'],
                        stage= deal['stage'],
                        contact_id= deal['contact']
                    )
                    deals_data.append(data.__dict__)

            if len(deals_data) == 0:
                return {"Message":"No deals are found"}
                
            return json.dumps(deals_data)
        return json.loads(resp.text)

    def deal_owner(self, context, params):
        """ Find owner details by id"""

        resp = util.rest('GET', "deals", context, None)

        if len(json.loads(resp.text)["deals"]) != 0:
            for deal in json.loads(resp.text)["deals"]:
                if deal.get("owner") == params.get("deal_owner_id"): 
                    owner_url = deal['links']['owner']
                    api_token = context['headers']['api_key']
                    headers = {
                        "Api-Token": f"{api_token}",
                        "Content-Type": "application/json"
                    }

                    # Get owner details
                    owner_data = requests.request('GET', owner_url, headers=headers).text
                    owner_data = json.loads(owner_data)["user"]
                    response = {
                        "owner_id":owner_data.get("id"),
                        "first_name": owner_data.get("firstName"),
                        "user_name": owner_data.get("username"),
                        "last_name":  owner_data.get("lastName"),
                        "email_address": owner_data.get("email"),
                        "phone_number": owner_data.get("lastName")
                    }
                    return response
                return {"Message": "Owner details not found"}

    def profile(self, context, params):
        """Get profile details"""

        response_data = util.rest('GET', "users", context, None)
        response = json.loads(response_data.text)
        if response_data.ok:
            response = response["users"][0]
            data = {
                "id": response["id"],
                "name": response["firstName"]+" "+response["lastName"],
                "email": response["email"]
            }
            return data
        return response
    
    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params)