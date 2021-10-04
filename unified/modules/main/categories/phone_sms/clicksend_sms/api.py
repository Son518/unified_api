import json

import clicksend_client

from phone_sms.clicksend_sms import util
from phone_sms.clicksend_sms.entities.clicksend_contact_list import ClickSend_Contact_List
from phone_sms.clicksend_sms.entities.clicksend_contact import ClickSend_Contact


class ClickSendApi():
    def search_contact_lists(self, context, params):
        '''Search for a contact list based on name'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.ContactListApi(clicksend_client.ApiClient(configuration))
        contact_lists = []

        api_response = api_instance.lists_get()
        api_response = api_response.replace("\'", "\"")
        api_response = json.dumps(api_response).replace("None", "null")
        api_response = json.loads(api_response)
        api_response = json.loads(api_response)
        for contact_list in api_response["data"]["data"]:
            if params["list_name"] == contact_list["list_name"]:
                clicksend_contact_list = ClickSend_Contact_List(
                    list_id = contact_list["list_id"],
                    list_name = contact_list["list_name"],
                    list_email_id = contact_list["list_email_id"])
                contact_lists.append(clicksend_contact_list.__dict__)
        return json.dumps(contact_lists)

    def search_contact_by_email_address(self, context, params):
        '''Search for a contact in a list based on email'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
        contact_lists = []
        list_id = params["contact_list"]

        api_response = api_instance.lists_contacts_by_list_id_get(list_id)
        api_response = api_response.replace("\'", "\"")
        api_response = json.dumps(api_response).replace("None", "null")
        api_response = json.loads(api_response)
        api_response = json.loads(api_response)
        for contact_list in api_response["data"]["data"]:
            if params["email_address"] == contact_list["email"]:
                clicksend_contact_list = ClickSend_Contact(
                    contact_list = contact_list["list_id"],
                    contact_id = contact_list["contact_id"],
                    last_name = contact_list["last_name"],
                    full_name = contact_list["first_name"],
                    phone_number = contact_list["phone_number"],
                    email = contact_list["email"],
                    fax_number = contact_list["fax_number"],
                    organization_name = contact_list["organization_name"],
                    city = contact_list["address_city"],
                    state = contact_list["address_state"],
                    postal_code = contact_list["address_postal_code"],
                    country = contact_list["address_country"],
                    custom_1 = contact_list["custom_1"],
                    custom_2 = contact_list["custom_2"],
                    custom_3 = contact_list["custom_3"],
                    custom_4 = contact_list["custom_4"])
                contact_lists.append(clicksend_contact_list.__dict__)
        return json.dumps(contact_lists)

    def search_contact_by_phone(self, context, params):
        '''Search for a contact in a list based on phone'''

        configuration = util.get_clicksend_configuration(context['headers'])
        api_instance = clicksend_client.ContactApi(clicksend_client.ApiClient(configuration))
        contact_lists = []
        list_id = params["contact_list"]

        api_response = api_instance.lists_contacts_by_list_id_get(list_id)
        api_response = api_response.replace("\'", "\"")
        api_response = json.dumps(api_response).replace("None", "null")
        api_response = json.loads(api_response)
        api_response = json.loads(api_response)
        params["phone_number"] = params["phone_number"].replace(" ", "")
        if "+" not in params["phone_number"]:
            phone_number = "+" + params["phone_number"]
        else:
            phone_number = params["phone_number"]
        for contact_list in api_response["data"]["data"]:
            if phone_number == contact_list["phone_number"]:
                clicksend_contact_list = ClickSend_Contact(
                    contact_list = contact_list["list_id"],
                    contact_id = contact_list["contact_id"],
                    last_name = contact_list["last_name"],
                    full_name = contact_list["first_name"],
                    phone_number = contact_list["phone_number"],
                    email = contact_list["email"],
                    fax_number = contact_list["fax_number"],
                    organization_name = contact_list["organization_name"],
                    city = contact_list["address_city"],
                    state = contact_list["address_state"],
                    postal_code = contact_list["address_postal_code"],
                    country = contact_list["address_country"],
                    custom_1 = contact_list["custom_1"],
                    custom_2 = contact_list["custom_2"],
                    custom_3 = contact_list["custom_3"],
                    custom_4 = contact_list["custom_4"])
                contact_lists.append(clicksend_contact_list.__dict__)
        return json.dumps(contact_lists)
