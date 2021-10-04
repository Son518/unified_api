# from unified.modules.main.categories.crm.entities.contact import Contact
from pipedrive.client import Client
from requests.api import request
from crm.pipedrive.entities.pipedrive_lead import PipedriveCRMLead
from crm.pipedrive.entities.pipedrive_deal import PipedriveCRMDeal
from crm.pipedrive.entities.pipedrive_note import PipedriveCRMNote
from crm.pipedrive.entities.pipedrive_account import PipedriveCRMAccount
from crm.pipedrive.entities.pipedrive_activity import PipredriveCRMActivity
from crm.pipedrive.entities.pipedrive_person import PipedriveCRMPerson
from crm.pipedrive import util
import json
from flask import jsonify
import requests


class PipedriveAPI():

    def account(self, context, params):
        """ Search an account by ID"""

        if "id" not in params:
            return "Please provide Id"

        client = util.pipedrive_authentication(context["headers"])
        account = client.organizations.get_organization(params["id"])
        
        if account["data"] is None:
            return "No data found"
            
        account_obj = PipedriveCRMAccount(
            account_id = account["data"]["id"],
            owner_id = account["data"]["owner_id"]["id"],
            name = account["data"]["name"]
        )
        return account_obj.__dict__

    def organization(self, context, params):
        """ Get orgnization by Id"""

        return self.account(context, params)

    def contact_by_name(self, context, params):
        """ Search an account by Name"""

        if "name" not in params:
            return "Please provide name"           

        params = {
            'term': params["name"]
        }
        client = util.pipedrive_authentication(context["headers"])
        contact = client.persons.get_persons_by_name(params = params)

        if contact["data"] is None:
            return "No data found"
        
        contact_obj = PipedriveCRMPerson(
            contact_id = contact["data"][0]["id"],
            name = contact["data"][0]["name"],
            phone = contact["data"][0]["phone"],
            organization_id = contact["data"][0]["org_id"],
            visible_to = contact["data"][0]["visible_to"]
        )

        # Note: deprecation_warning': {'#': 'Warning! This endpoint will be removed soon. Please check API documentation at developers.pipedrive.com.
        return contact_obj.__dict__

    def deal(self, context, params):
        """ Search a deal by ID"""

        if "id" not in params:
            return "Please provide Id"           

        client = util.pipedrive_authentication(context["headers"])
        deal = client.deals.get_deal(params["id"])

        if deal["data"] is None:
            return "No data found"
        deal_obj = PipedriveCRMDeal(
            deal_id = deal["data"]["id"],
            owner_id = deal["related_objects"]["person"]["2"]["owner_id"],
            visible_to = deal["data"]["visible_to"],
            title = deal["data"]["title"],
            organization_id = deal["related_objects"]["organization"]["2"]["id"],
            expected_close_date = deal["data"]["expected_close_date"],
            status = deal["data"]["status"],
            currency = deal["data"]["currency"],
            probability = deal["data"]["probability"]
        )
        return deal_obj.__dict__

    def lead(self, context, params):
        """ Search lead"""

        if "id" not in params:
            return "Please provide Id"
            
        lead = util.rest(f'https://{context["headers"]["domain"]}.pipedrive.com/v1/leads/{params["id"]}', context["headers"]["api_token"], "GET", "", "")
        lead = json.loads(lead)

        if lead["data"] is None:
            return "No data found"

        lead_obj = PipedriveCRMLead(
            lead_id = lead["data"]["id"],
            title = lead["data"]["title"],
            owner_id = lead["data"]["owner_id"],
            organization_id = lead["data"]["organization_id"],
            person_id = lead["data"]["person_id"],
            note = lead["data"]["note"],
            expected_close_date = lead["data"]["expected_close_date"],
            lead_value = lead["data"]["value"],
            label_id = lead["data"]["label_ids"]
        )
        return lead_obj.__dict__

    def accounts(self, context, params):
        """ Get list of all organizations"""

        client = util.pipedrive_authentication(context["headers"])
        accounts = client.organizations.get_all_organizations()
        
        if len(accounts["data"]) == 0:
            return "No data found"

        final_data = []
        for account in accounts["data"]:
            account_obj = PipedriveCRMAccount(
                account_id = account["id"],
                owner_id = account["owner_id"]["id"],
                name = account["name"]
            )
            final_data.append(account_obj.__dict__)
        return json.dumps(final_data)

    def deals(self, context, params):
        """ Get list of all deals"""

        client = util.pipedrive_authentication(context["headers"])
        deals = client.deals.get_all_deals()
        if len(deals["data"]) == 0:
            return "No data found"
        obj = PipedriveCRMDeal(
            owner_id = deals["related_objects"]["person"]["2"]["owner_id"],
            organization_id = deals["related_objects"]["organization"]["2"]["id"]
        )
        obj = obj.__dict__
        final_data = []
        for deal in deals["data"]:
            deal_obj = PipedriveCRMDeal(
                deal_id = deal["id"],
                visible_to = deal["visible_to"],
                title = deal["title"],
                expected_close_date = deal["expected_close_date"],
                status = deal["status"],
                currency = deal["currency"],
                probability = deal["probability"],
                owner_id = obj["owner_id"],
                organization_id = obj["organization_id"]
            )
            final_data.append(deal_obj.__dict__)
        return json.dumps(final_data)

    def leads(self, context, params):
        """ Get list of all leads"""

        leads = util.rest(f'https://{context["headers"]["domain"]}.pipedrive.com/v1/leads', context["headers"]["api_token"], "GET", "", "")
        leads = json.loads(leads)
        final_data = []
        for lead in leads["data"]:
            lead_obj = PipedriveCRMLead(
                lead_id = lead["id"],
                title = lead["title"],
                owner_id = lead["owner_id"],
                organization_id = lead["organization_id"],
                person_id = lead["person_id"],
                note = lead["note"],
                expected_close_date = lead["expected_close_date"],
                lead_value = lead["value"],
                label_id = lead["label_ids"]
            )
            final_data.append(lead_obj.__dict__)
        return json.dumps(final_data)

    def person(self, context, params):
        """ Get Person by ID"""

        if "id" not in params:
            return "Please provide Id"

        client = util.pipedrive_authentication(context["headers"])
        person = client.persons.get_person(params["id"])
        
        if person["data"] is None:
            return "No data found"
        person_obj = PipedriveCRMPerson(
            organization_id = person["data"]["org_id"],
            name = person["data"]["name"],
            visible_to = person["data"]["visible_to"],
            phone = person["data"]["phone"][0]["value"],
            person_id = person["data"]["id"],
            contact_id = person["data"]["id"],
            account_id = person["data"]["org_id"],
            last_name = person["data"]["last_name"],
            first_name = person["data"]["first_name"],
            email = person["data"]["email"][0]["value"],
            owner_id = person["data"]["owner_id"]["id"]
        )
        return person_obj.__dict__

    def person_by_email(self, context, params):
        """ Get Person by Email"""

        if "email" not in params:
            return "Please provide email"
        
        person = requests.request(url=f'https://{context["headers"]["domain"]}.pipedrive.com/v1/persons/search?term={params["email"]}&api_token={context["headers"]["api_token"]}', method="GET").text
        person = json.loads(person)

        if person["data"] is None:
            return "No data found"

        person_obj = PipedriveCRMPerson(
            organization_id = person["data"]["items"][0]["item"]["organization"]["id"],
            name = person["data"]["items"][0]["item"]["name"],
            visible_to = person["data"]["items"][1]["item"]["visible_to"],
            phone = person["data"]["items"][2]["item"]["phones"][0],
            person_id = person["data"]["items"][0]["item"]["id"],
            contact_id = person["data"]["items"][0]["item"]["id"],
            account_id = person["data"]["items"][0]["item"]["organization"]["id"],
            email = person["data"]["items"][1]["item"]["emails"][0],
            owner_id = person["data"]["items"][1]["item"]["owner"]["id"]
        )
        return person_obj.__dict__

    def person_by_name(self, context, params):
        """ Get Person by Email"""

        if "name" not in params:
            return "Please provide name"
        
        person = requests.request(url=f'https://{context["headers"]["domain"]}.pipedrive.com/v1/persons/search?term={params["name"]}&api_token={context["headers"]["api_token"]}', method="GET").text
        person = json.loads(person)

        if person["success"] is False:
            return "No data found"
        person_obj = PipedriveCRMPerson(
            organization_id = person["data"]["items"][0]["item"]["organization"]["id"],
            name = person["data"]["items"][0]["item"]["name"],
            visible_to = person["data"]["items"][1]["item"]["visible_to"],
            phone = person["data"]["items"][2]["item"]["phones"][0],
            person_id = person["data"]["items"][0]["item"]["id"],
            contact_id = person["data"]["items"][0]["item"]["id"],
            account_id = person["data"]["items"][0]["item"]["organization"]["id"],
            email = person["data"]["items"][0]["item"]["emails"][0],
            owner_id = person["data"]["items"][1]["item"]["owner"]["id"]
        )
        return person_obj.__dict__

    def persons(self, context, params):
        """ List of persons"""

        client = util.pipedrive_authentication(context["headers"])
        persons = client.persons.get_all_persons()
        
        if len(persons["data"]) == 0:
            return "No data found"

        final_data = []
        for person in persons["data"]:
            person_obj = PipedriveCRMPerson(
                organization_id = person["org_id"],
                name = person["name"],
                visible_to = person["visible_to"],
                phone = person["phone"][0]["value"],
                person_id = person["id"],
                contact_id = person["id"],
                account_id = person["org_id"],
                last_name = person["last_name"],
                first_name = person["first_name"],
                email = person["email"][0]["value"],
                owner_id = person["owner_id"]["id"]
            )
            final_data.append(person_obj.__dict__)
        return json.dumps(final_data)

    def account_by_name(self, context, params):
        """ Search an account by Name"""

        if "name" not in params:
            return "Please provide name"

        account = requests.request(url=f'https://{context["headers"]["domain"]}.pipedrive.com/v1/organizations/search?term={params["name"]}&api_token={context["headers"]["api_token"]}', method="GET").text
        account = json.loads(account)

        account_obj = PipedriveCRMAccount(
            account_id = account["data"]["items"][0]["item"]["id"],
            owner_id = account["data"]["items"][0]["item"]["owner"]["id"],
            name = account["data"]["items"][0]["item"]["name"]
        )
        return account_obj.__dict__


    def deal_by_name(self, context, params):
        """ Search an account by Name"""

        if "name" not in params:
            return {"message":"Please provide name"}

        deal = requests.request(url=f'https://{context["headers"]["domain"]}.pipedrive.com/v1/deals/search?term={params["name"]}&api_token={context["headers"]["api_token"]}', method="GET").text
        deal = json.loads(deal)
        
        if deal["success"] is False:
            return {"Error": deal["error"]}
        if len(deal["data"]["items"]) == 0:
            return {"message":"Data not found"}
            
        deal_obj = PipedriveCRMDeal(
            deal_id = deal["data"]["items"][0]["item"]["id"],
            owner_id = deal["data"]["items"][0]["item"]["owner"]["id"],
            visible_to = deal["data"]["items"][0]["item"]["visible_to"],
            title = deal["data"]["items"][0]["item"]["title"],
            organization_id = deal["data"]["items"][0]["item"]["organization"]["id"],
            status = deal["data"]["items"][0]["item"]["status"],
            currency = deal["data"]["items"][0]["item"]["currency"]
        )
        return deal_obj.__dict__

    def profile(self, context, params):
        """Get profile details"""

        response_data = requests.request(url=f'https://{context["headers"]["domain"]}.pipedrive.com/v1/users/me?api_token={context["headers"]["api_token"]}', method="GET")
        response = json.loads(response_data.text)
        
        if response_data.ok:
            response = response["data"]
            data = {
                "id": response["id"],
                "name": response["name"],
                "email": response["email"]
            }
            return data
        return response

    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params)        