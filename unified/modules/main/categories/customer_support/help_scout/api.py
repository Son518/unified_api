import json
from customer_support.help_scout import util
from customer_support.help_scout.entities.help_scout_conversation import HelpscoutConversation
from customer_support.help_scout.entities.help_scout_customer import HelpscoutCustomer
from customer_support.help_scout.entities.help_scout_user import HelpscoutUser


class HelpscoutApi():

    def find_customer(self, context, params):
        """
        gets a customer using email
        context holds the headers 
        params holds email
        """
        client = util.helpscout_client(context["headers"])
        customer = client.customer.list(email=params["email"])
        customer = customer.get("_embedded").get("customers")[0]
        customer_embedded = customer.get("_embedded") or {}
        customer_obj = HelpscoutCustomer(first_name=customer.get("firstName") or None,
                                         last_name=customer.get(
                                             "lastName") or None,
                                         phone=customer_embedded.get(
                                             "phones") if customer_embedded.get("phones") else None,
                                         email=customer_embedded.get(
                                             "emails") if customer_embedded.get("emails") else None,
                                         website=customer_embedded.get(
                                             "websites") if customer_embedded.get("websites") else None,
                                         customer_id=customer.get(
                                             "id") or None,
                                         job_title=customer.get(
                                             "jobTitle") or None,
                                         organization=customer.get(
                                             "organization") or None,
                                         address=customer_embedded.get(
                                             "address") or None
                                         )

        return customer_obj.__dict__

    def find_user_email(self, context, params):
        """
        gets a user using email
        context holds the headers 
        params holds email
        """
        client = util.helpscout_client(context["headers"])
        user = client.user.list(email=params["email"])
        user = user.get("_embedded").get("users")[0]
        user_obj = HelpscoutUser(email=user.get("email") or None,
                                 first_name=user.get("firstName") or None,
                                 user_id=user.get("id") or None,
                                 initials=user.get("initials") or None,
                                 job_title=user.get("job_title") or None,
                                 last_name=user.get("lastName") or None,
                                 phone=user.get("phone") or None,
                                 role=user.get("role") or None
                                 )
        return user_obj.__dict__

    def verify(self,context,params):
        """
        get call to verify user authenticated information
        """
        client = util.helpscout_client(context["headers"])
        user = client.user.list()
        return user


    def profile(self,context,params):
        """
        get call to show authenticated user information
        """
        client = util.helpscout_client(context["headers"])
        user = client.user.list()['_embedded']['users'][0]
        profile = {
            'id':user['id'],
            'name':user['firstName'],
            'email':user['email']
        }
        return profile