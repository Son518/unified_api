import json
from customer_support.intercom import util
from customer_support.intercom.entities.intercom_company import IntercomCompany
from customer_support.intercom.entities.intercom_contact import IntercomContact


class IntercomApi():

    def company(self, context, params):
        """
        gets company data based on company_id specified in params
        context holds headers
        params hold company_id
        """
        response = json.loads(util.rest(
            "GET", "companies", context["headers"]["access_token"], id=params["company_id"]).text)
        response = response or {}
        company = IntercomCompany(company=response["company_id"],
                                  monthly_revenue=response["monthly_spend"],
                                  plan=response["plan"]["name"],
                                  tag_name=response["tags"]
                                  )
        return company.__dict__

    def lead(self, context, params):
        """
        gets lead data based on lead_id specified in params
        context holds headers
        params hold lead_id
        """
        response = json.loads(util.rest(
            "GET", "contacts", context["headers"]["access_token"], id=params["lead_id"]).text)
        lead_obj = IntercomContact(email=response["email"],
                                   full_name=response["name"],
                                   lead_id=response["id"],
                                   lead=response["id"],
                                   created_date=util.epoch_to_date(response["created_at"]),
                                   unsubscribed=response["unsubscribed_from_emails"],                        
                                   lookup_email=response["email"],
                                   phone_number=response["phone"],
                                   unsubscribed_from_emails=response["unsubscribed_from_emails"],
                                   company=response["companies"],
                                   tag_name=response["tags"],
                                   tag_id=response["tags"],
                                   id=response["id"],
                                )
        return lead_obj.__dict__

    def lead_by_email(self, context, params):
        """
        gets lead data based on email specified in params
        context holds headers
        params hold email
        """
        data = {
            "query": {
                "field": "email",
                "operator": "=",
                "value": params["email"]
            }
        }
        response = json.loads(util.rest(
            "POST", "contact_email", context["headers"]["access_token"], data).text)
        response = response["data"][0]
        lead_obj = IntercomContact(email=response["email"],
                                   full_name=response["name"],
                                   lead_id=response["id"],
                                   lead=response["id"],
                                   created_date=util.epoch_to_date(response["created_at"]),
                                   unsubscribed=response["unsubscribed_from_emails"],
                                   lookup_email=response["email"],
                                   phone_number=response["phone"],
                                   unsubscribed_from_emails=response["unsubscribed_from_emails"],
                                   company=response["companies"],
                                   tag_name=response["tags"],
                                   tag_id=response["tags"],
                                   id=response["id"],
                                )
        return lead_obj.__dict__

    def user(self, context, params):
        """
        gets user data based on user_id specified in params
        context holds headers
        params hold id
        """
        response = json.loads(util.rest(
            "GET", "contacts", context["headers"]["access_token"], id=params["user_id"]).text)
        user_obj = IntercomContact(email=response["email"],
                                   full_name=response["name"],
                                   user_id=response["id"],
                                   user=response["id"],
                                   created_date=util.epoch_to_date(response["created_at"]),
                                   unsubscribed=response["unsubscribed_from_emails"],
                                   lookup_email=response["email"],
                                   phone_number=response["phone"],
                                   unsubscribed_from_emails=response["unsubscribed_from_emails"],
                                   company=response["companies"],
                                   tag_name=response["tags"],
                                   tag_id=response["tags"],
                                   id=response["id"],
                                )
        return user_obj.__dict__

    def user_by_email(self, context, params):
        """
        gets user data based on email specified in params
        context holds headers
        params hold email
        """
        data = {
            "query": {
                "field": "email",
                "operator": "=",
                "value": params["email"]
            }
        }
        response = json.loads(util.rest(
            "POST", "contact_email", context["headers"]["access_token"], data).text)
        response = response["data"][0]
        user_obj = IntercomContact(email=response["email"],
                                   full_name=response["name"],
                                   user_id=response["id"],
                                   user=response["id"],
                                   created_date=util.epoch_to_date(response["created_at"]),
                                   unsubscribed=response["unsubscribed_from_emails"],
                                   lookup_email=response["email"],
                                   phone_number=response["phone"],
                                   unsubscribed_from_emails=response["unsubscribed_from_emails"],
                                   company=response["companies"],
                                   tag_name=response["tags"],
                                   tag_id=response["tags"],
                                   id=response["id"],
                                )
        return user_obj.__dict__

    def profile(self, context, params):
        """
        get call to show authenticated user information
        """
        response = json.loads(util.rest("GET", "admin", context["headers"]["access_token"]).text)
        profile = {
            'id': response['admins'][0]['id'],
            'name':response['admins'][0]['name'],
            'email':response['admins'][0]['email'],
        }
        return profile

    def verify(self, context, params):
        """
        get call to verify user authenticated information
        """
        response = util.rest("GET", "admin", context["headers"]["access_token"])
        return response.json()