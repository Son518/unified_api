from crm.freshworks import util
from crm.freshworks.entities.freshworks_contact import FreshworksContact
from crm.freshworks.entities.freshworks_deal import FreshworksDeal
from crm.freshworks.entities.freshworks_account import FreshworksAccount
from crm.freshworks.entities.freshworks_note import FreshworksNote
from crm.freshworks.entities.freshworks_task import FreshworksTask
from unified.core.actions import Actions
import json


class FreshworksApi():

    def account(self, context, params):
        """
        gets account data based on account_id
        context holds the headers 
        params holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/sales_accounts/{params['account_id']}"
        response = json.loads(
            util.rest("GET", url, {}, context["headers"]).text)
        response = response["sales_account"]
        account = FreshworksAccount(account_name=response["name"],
                                    annual_revenue=response["annual_revenue"],
                                    created_date=response["created_at"],
                                    updated_date=response["updated_at"],
                                    facebook=response["facebook"],
                                    twitter=response["twitter"],
                                    linkedin=response["linkedin"],
                                    address=response["address"],
                                    city=response["city"],
                                    state=response["state"],
                                    zipcode=response["zipcode"],
                                    country=response["country"]
                                    )
        return account.__dict__

    def account_by_name(self, context, params):
        """
        gets account data based on account name
        context holds the headers 
        params holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/lookup?q={params['name']}&f=name&entities=sales_account"
        response = json.loads(
            util.rest("GET", url, {}, context["headers"]).text)
        response = response["sales_accounts"]["sales_accounts"][0]
        account = FreshworksAccount(account_name=response["name"],
                                    annual_revenue=response["annual_revenue"],
                                    created_date=response["created_at"],
                                    updated_date=response["updated_at"],
                                    facebook=response["facebook"],
                                    twitter=response["twitter"],
                                    linkedin=response["linkedin"],
                                    address=response["address"],
                                    city=response["city"],
                                    state=response["state"],
                                    zipcode=response["zipcode"],
                                    country=response["country"]
                                    )
        return account.__dict__

    def contact(self, context, params):
        """
        gets contact data based on contact_id
        context holds the headers 
        params holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/contacts/{params['contact_id']}"
        response = json.loads(
            util.rest("GET", url, {}, context["headers"]).text)
        response = response["contact"]
        contact = FreshworksContact(facebook=response["facebook"],
                                    twitter=response["twitter"],
                                    linkedin=response["linkedin"],
                                    address=response["address"],
                                    mobile_number=response["mobile_number"],
                                    created_date=response["created_at"],
                                    updated_date=response["updated_at"],
                                    display_name=response["display_name"],
                                    job_title=response["job_title"],
                                    external_id=response["external_id"],
                                    first_name=response["first_name"],
                                    last_name=response["last_name"]
                                    )
        return contact.__dict__

    def contact_by_email(self, context, params):
        """
        gets contact data based on contact_email
        context holds the headers 
        params holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/lookup?q={params['email']}&f=email&entities=contact"
        response = json.loads(
            util.rest("GET", url, {}, context["headers"]).text)
        response = response["contacts"]["contacts"][0]
        contact = FreshworksContact(facebook=response["facebook"],
                                    twitter=response["twitter"],
                                    linkedin=response["linkedin"],
                                    address=response["address"],
                                    mobile_number=response["mobile_number"],
                                    created_date=response["created_at"],
                                    updated_date=response["updated_at"],
                                    display_name=response["display_name"],
                                    job_title=response["job_title"],
                                    external_id=response["external_id"],
                                    first_name=response["first_name"],
                                    last_name=response["last_name"]
                                    )
        return contact.__dict__

    def contact_by_name(self, context, params):
        """
        gets contact data based on contact name
        context holds the headers 
        params holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/lookup?q={params['name']}&f=display_name&entities=contact"
        response = json.loads(
            util.rest("GET", url, {}, context["headers"]).text)
        response = response["contacts"]["contacts"][0]
        contact = FreshworksContact(facebook=response["facebook"],
                                    twitter=response["twitter"],
                                    linkedin=response["linkedin"],
                                    address=response["address"],
                                    mobile_number=response["mobile_number"],
                                    created_date=response["created_at"],
                                    updated_date=response["updated_at"],
                                    display_name=response["display_name"],
                                    job_title=response["job_title"],
                                    external_id=response["external_id"],
                                    first_name=response["first_name"],
                                    last_name=response["last_name"]
                                    )
        return contact.__dict__

    
    def deal(self, context, params):
        """
        gets deal data based on deal_id
        context holds the headers 
        params holds the request.body
        """

        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/deals/{params['deal_id']}"
        response = json.loads(
            util.rest("GET", url, {}, context["headers"]).text)
        response = response["deal"]
        deal = FreshworksDeal(deal_id=response["id"],
                              name=response["name"],
                              created_date=response["created_at"],
                              updated_date=response["updated_at"],
                              close_date=response["closed_date"],
                              stage_id=response["deal_stage_id"],
                              value=response["expected_deal_value"],
                              probability=response["probability"])
        return deal.__dict__

    def deal_by_name(self, context, params):
        """
        gets deal data based on deal name
        context holds the headers 
        params holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/lookup?q={params['name']}&f=name&entities=deal"
        response = json.loads(
            util.rest("GET", url, {}, context["headers"]).text)
        response = response["deals"]["deals"][0]
        deal = FreshworksDeal(deal_id=response["id"],
                              name=response["name"],
                              created_date=response["created_at"],
                              updated_date=response["updated_at"],
                              close_date=response["closed_date"],
                              stage_id=response["deal_stage_id"],
                              value=response["expected_deal_value"],
                              probability=response["probability"])
        return deal.__dict__

    
    def tasks(self, context, contact_entity):
        """
        gets list pf tasks 
        context holds the headers 
        params holds the request.body
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/tasks?filter=open&include=owner"

        contact_data = {}
        response = json.loads(util.rest("GET", url, json.dumps(contact_data), context["headers"]).text)
        tasks = response["tasks"]
        tasks_list = []
        for task in tasks:
            print(task)
            task_obj = FreshworksTask(name=task["title"],
                                        task_id=task["id"],
                                        description=task["description"],
                                        created_date=task["created_at"],
                                        updated_date=task["updated_at"],
                                        due_date=task["due_date"],
                                        owner_id=task["owner_id"]
                                        )
            tasks_list.append(task_obj.__dict__)

        return json.dumps(tasks_list)

    def verify(self, context, params):
        """
        get call to verify user authenticated information
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/sales_accounts/filters"
        response =  util.rest("GET", url, {}, context["headers"])
        return response.json()
    
    def profile(self, context, params):
        """
        get call to show user authenticated information
        """
        domain = context["headers"]["domain"]
        url = f"https://{domain}.myfreshworks.com/crm/sales/api/selector/owners"
        response =  util.rest("GET", url, {}, context["headers"]).json()
        profile = {
            'id':response['users'][0]['id'],
            'name':response['users'][0]['display_name'],
            'email':response['users'][0]['email']
        }
        return profile