from agilecrm.client import Client
from unified.core.actions import Actions
from crm.agilecrm.entities.agilecrm_contact import AgilecrmContact
from crm.agilecrm.entities.agilecrm_deal import AgilecrmDeal
from crm.agilecrm.entities.agilecrm_event import AgilecrmEvent
from crm.agilecrm.entities.agilecrm_task import AgilecrmTask
from crm.agilecrm.util import agilecrm_authentication
import json
from crm.agilecrm import util


class AgilecrmApi():

    def contact(self, context, params):
        ''' gets contact by id'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])

        # sdk requires a str type id
        contact = agilecrm_client.get_contact_by_id(str(params["contact_id"]))
        contact_obj = AgilecrmContact(id=contact["id"],
                                      domain=contact["owner"]["domain"],
                                      email=util.property_conversion(
                                          contact["properties"])["email"],
                                      owner_id=contact["owner"]["id"],
                                      first_name=util.property_conversion(
                                          contact["properties"])["first_name"],
                                      last_name=util.property_conversion(
                                          contact["properties"])["last_name"],
                                      company_name=util.property_conversion(
                                          contact["properties"])["company"],
                                      business_phone=util.property_conversion(
                                          contact["properties"])["phone"],
                                      business_website=util.property_conversion(
                                          contact["properties"])["website"],
                                      mailing_zip=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["zip"],
                                      mailing_country=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["countryname"],
                                      mailing_state=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["state"],
                                      mailing_street=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["address"],
                                      mailing_city=json.loads(util.property_conversion(contact["properties"])["address"])["city"],)

        return contact_obj.__dict__

    def contact_by_email(self, context, params):
        ''' gets contact by email'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        contact = agilecrm_client.get_contact_by_email(params["email"])
        contact_obj = AgilecrmContact(id=contact["id"],
                                      domain=contact["owner"]["domain"],
                                      email=util.property_conversion(
                                          contact["properties"])["email"],
                                      owner_id=contact["owner"]["id"],
                                      first_name=util.property_conversion(
                                          contact["properties"])["first_name"],
                                      last_name=util.property_conversion(
                                          contact["properties"])["last_name"],
                                      company_name=util.property_conversion(
                                          contact["properties"])["company"],
                                      business_phone=util.property_conversion(
                                          contact["properties"])["phone"],
                                      business_website=util.property_conversion(
                                          contact["properties"])["website"],
                                      mailing_zip=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["zip"],
                                      mailing_country=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["countryname"],
                                      mailing_state=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["state"],
                                      mailing_street=json.loads(util.property_conversion(
                                          contact["properties"])["address"])["address"],
                                      mailing_city=json.loads(util.property_conversion(contact["properties"])["address"])["city"],)

        return contact_obj.__dict__

    def deal(self, context, params):
        ''' gets deal by id'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        deal = agilecrm_client.get_deal_by_id(params['deal_id'])
        deal_obj = AgilecrmDeal(deal_id=deal.get("id") or None,
                                description=deal.get("description") or None,
                                expected_value=deal.get(
                                    "expected_value") or None,
                                discount_amt=deal.get("discount_amt") or None,
                                discount_value=deal.get(
                                    "discount_value") or None,
                                probability=deal.get("probability") or None,
                                )

        return deal_obj.__dict__

    def deals(self, context, params):
        ''' gets all deals'''

        domain = context["headers"]["domain"]
        url = f"https://{domain}.agilecrm.com/dev/api/opportunity"
        deals = json.loads(
            util.rest(url, context["headers"], "GET", None, "application/json"))

        deal_value = []
        for deal in deals:
            deal_obj = AgilecrmDeal(deal_id=deal.get("id") or None,
                                    description=deal.get(
                                        "description") or None,
                                    expected_value=deal.get(
                                        "expected_value") or None,
                                    discount_amt=deal.get(
                                        "discount_amt") or None,
                                    discount_value=deal.get(
                                        "discount_value") or None,
                                    probability=deal.get(
                                        "probability") or None,
                                    created_date=str(
                                        deal.get("created_time")) or None
                                    )
            deal_value.append(deal_obj.__dict__)

        return json.dumps(deal_value)

    def accounts(self, context, params):
        ''' gets all accounts'''

        domain = context["headers"]["domain"]
        url = f"https://{domain}.agilecrm.com/dev/api/contacts/companies/list"
        response = util.rest(
            url, context["headers"], "GET", None, "application/json")
        # as response is sending only status code unable to unification
        return json.loads(response)

    def contacts(self, context, contact_entity):
        ''' gets all contacts'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        contacts = agilecrm_client.get_contacts()
        contact_value = []
        for contact in contacts:
            contact_obj = AgilecrmContact(id=contact.get('id'),
                                          domain=contact.get(
                                              'owner').get("domain"),
                                          email=util.property_conversion(
                                              contact.get("properties")).get("email") or None,
                                          owner_id=contact.get(
                                              'owner').get("id"),
                                          first_name=util.property_conversion(
                                              contact.get("properties")).get("first_name"),
                                          last_name=util.property_conversion(
                                              contact.get("properties")).get("last_name"),
                                          company_name=util.property_conversion(
                                              contact.get("properties")).get("company") or None,
                                          business_phone=util.property_conversion(
                                              contact.get("properties")).get("phone") or None,
                                          business_website=util.property_conversion(
                                              contact.get("properties")).get("website") or None
                                          )
            contact_value.append(contact_obj.__dict__)

        return json.dumps(contact_value)

    def contact_by_name(self, context, params):
        ''' gets contact by name'''

        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        contacts = agilecrm_client.get_contacts()
        contact_value = []
        for contact in contacts:
            if params["first_name"] == util.property_conversion(contact.get("properties")).get("first_name") and params["last_name"] == util.property_conversion(contact.get("properties")).get("last_name"):
                contact_obj = AgilecrmContact(id=contact.get('id'),
                                              domain=contact.get(
                                                  'owner').get("domain"),
                                              email=util.property_conversion(
                                                  contact.get("properties")).get("email") or None,
                                              owner_id=contact.get(
                                                  'owner').get("id"),
                                              first_name=util.property_conversion(
                                                  contact.get("properties")).get("first_name"),
                                              last_name=util.property_conversion(
                                                  contact.get("properties")).get("last_name"),
                                              company_name=util.property_conversion(
                                                  contact.get("properties")).get("company") or None,
                                              business_phone=util.property_conversion(
                                                  contact.get("properties")).get("phone") or None,
                                              business_website=util.property_conversion(
                                                  contact.get("properties")).get("website") or None
                                              )
                contact_value.append(contact_obj.__dict__)

        return json.dumps(contact_value)

    def tasks(self, context, params):
        ''' gets all tasks'''

        domain = context["headers"]["domain"]
        url = f"https://{domain}.agilecrm.com/dev/api/tasks"
        tasks = json.loads(
            util.rest(url, context["headers"], "GET", None, "application/json"))
        task_value = []
        for task in tasks:
            task_obj = AgilecrmTask(task_id=task.get("id"),
                                    priority=task.get("priority_type"),
                                    name=task.get("subject"),
                                    task_type=task.get("type"),
                                    due_date=task.get("due"),
                                    status=task.get("status"),
                                    description=task.get("taskDescription"),
                                    progress=task.get("progress"),
                                    owner_id=task.get("taskOwner").get("id"),
                                    email=task.get("taskOwner").get("email"),
                                    is_complete=task.get("is_complete")
                                    )
            task_value.append(task_obj.__dict__)

        return json.dumps(task_value)

    def new_contacts_by_date_range(self, context, params):
        ''' gets contacts by filtered date range'''

        domain = context["headers"]["domain"]
        url = f"https://{domain}.agilecrm.com/dev/api/contacts?start={params['start']}"
        tasks = json.loads(
            util.rest(url, context["headers"], "GET", None, "application/json"))
        task_value = []
        for task in tasks:
            task_obj = AgilecrmTask(task_id=task.get("id"),
                                    priority=task.get("priority_type"),
                                    name=task.get("subject"),
                                    task_type=task.get("type"),
                                    due_date=task.get("due"),
                                    status=task.get("status"),
                                    description=task.get("taskDescription"),
                                    progress=task.get("progress"),
                                    owner_id=task.get("taskOwner").get("id"),
                                    email=task.get("taskOwner").get("email"),
                                    is_complete=task.get("is_complete")
                                    )
            task_value.append(task_obj.__dict__)

        return json.dumps(task_value)

    def new_tasks_by_date_range(self, context, params):
        ''' gets tasks by filtered date range'''

        domain = context["headers"]["domain"]
        url = f"https://{domain}.agilecrm.com/dev/api/tasks?start={params['start']}"
        tasks = json.loads(
            util.rest(url, context["headers"], "GET", None, "application/json"))
        task_value = []
        for task in tasks:
            task_obj = AgilecrmTask(task_id=task.get("id"),
                                    priority=task.get("priority_type"),
                                    name=task.get("subject"),
                                    task_type=task.get("type"),
                                    due_date=task.get("due"),
                                    status=task.get("status"),
                                    description=task.get("taskDescription"),
                                    progress=task.get("progress"),
                                    owner_id=task.get("taskOwner").get("id"),
                                    email=task.get("taskOwner").get("email"),
                                    is_complete=task.get("is_complete")
                                    )
            task_value.append(task_obj.__dict__)

        return json.dumps(task_value)

    def new_deals_by_date_range(self, context, params):
        ''' gets deals by filtered date range'''

        domain = context["headers"]["domain"]
        url = f"https://{domain}.agilecrm.com/dev/api/opportunity?start={params['start']}"
        deals = json.loads(
            util.rest(url, context["headers"], "GET", None, "application/json"))
        deal_value = []
        for deal in deals:
            deal_obj = AgilecrmDeal(deal_id=deal.get("id") or None,
                                    description=deal.get(
                                        "description") or None,
                                    expected_value=deal.get(
                                        "expected_value") or None,
                                    discount_amt=deal.get(
                                        "discount_amt") or None,
                                    discount_value=deal.get(
                                        "discount_value") or None,
                                    probability=deal.get(
                                        "probability") or None,
                                    created_date=str(
                                        deal.get("created_time")) or None
                                    )
            deal_value.append(deal_obj.__dict__)

        return json.dumps(deal_value)

    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        response = agilecrm_client.get_contacts()
        return response[0]

    def profile(self, context, params):
        """
        get call to show authenticated user information
        """
        agilecrm_client = Client(
            context["headers"]["api_key"], context["headers"]["email"], context["headers"]["domain"])
        
        # as there is no specific call for profile data we are getting from owner object got in contacts
        response = agilecrm_client.get_contacts()[0]
        profile = {
            'id':response['owner']['id'],
            'name':response['owner']['name'],
            'email':response['owner']['email']
        }
        return profile