from onepagecrm import OnePageCRMAPI
from crm.onepagecrm.entities.onepagecrm_contact import OnepagecrmContact
from crm.onepagecrm import util
import json
import requests,base64


class OnepagecrmApi():

    def contacts(self, context, payload):
        ''' gets all contacts'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contacts = client.get('contacts')['contacts']
        contact_obj = []

        for contact in contacts:
            contact = contact.get('contact') or None
            address_list = contact.get("address_list")
            print(contact.get('emails'))
            contact_value = OnepagecrmContact(
                        contact_id=contact.get("id") or None,
                        email=contact.get('emails')[0]['value'] if len(contact.get('emails')) > 0 else None,
                        first_name=contact.get("first_name") or None,
                        last_name=contact.get("last_name") or None,
                        job_title=contact.get("job_title") or None,
                        company_id=contact.get("company_id") or None,
                        owner_id=contact.get("owner_id") or None,
                        company=contact.get("company_name") or None,
                        company_size=contact.get("company_size") or None,
                        status=contact.get("status") or None,
                        tags=contact.get("tags") or None,
                        mailing_street=address_list[0]['address'] if address_list else None,
                        mailing_city=address_list[0]["city"] if address_list else None,
                        mailing_state=address_list[0]["state"] if address_list else None,
                        mailing_country=address_list[0]["country_code"] if address_list else None,
                        mailing_zip=address_list[0]["zip_code"] if address_list else None,
                        created_date=contact.get("created_at") or None,
                        updated_date=contact.get("modified_at") or None
                        )
            contact_obj.append(contact_value.__dict__)

        return json.dumps(contact_obj)

    def contact(self, context, payload):
        '''gets contact information based on id'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contact = client.get('contacts', payload['id'])['contact']
        address_list = contact.get("address_list")
        contact_obj = OnepagecrmContact(
            contact_id=contact.get("id") or None,
            first_name=contact.get("first_name") or None,
            last_name=contact.get("last_name") or None,
            job_title=contact.get("job_title") or None,
            company_id=contact.get("company_id") or None,
            owner_id=contact.get("owner_id") or None,
            company=contact.get("company_name") or None,
            company_size=contact.get("company_size") or None,
            status=contact.get("status") or None,
            tags=contact.get("tags") or None,
            mailing_street=address_list[0]['address'] if address_list else None,
            mailing_city=address_list[0]["city"] if address_list else None,
            mailing_state=address_list[0]["state"] if address_list else None,
            mailing_country=address_list[0]["country_code"] if address_list else None,
            mailing_zip=address_list[0]["zip_code"] if address_list else None,
            created_date=contact.get("created_at") or None,
            updated_date=contact.get("modified_at") or None
            )

        return contact_obj.__dict__

    def contact_by_email(self, context, payload):
        ''' gets contact information based on email'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contacts = client.get('contacts')['contacts']
        contact_obj = []

        for contact in contacts:
            if len(contact['contact']['emails']) > 0:
                if payload['email'] == contact['contact']['emails'][0]['value']:
                    contact = contact.get('contact') or None
                    address_list = contact.get("address_list")
                    contact_value = OnepagecrmContact(
                        contact_id=contact.get("id") or None,
                        email=contact.get('emails')[0]['value'] if len(contact.get('emails')) > 0 else None,
                        first_name=contact.get("first_name") or None,
                        last_name=contact.get("last_name") or None,
                        job_title=contact.get("job_title") or None,
                        company_id=contact.get("company_id") or None,
                        owner_id=contact.get("owner_id") or None,
                        company=contact.get("company_name") or None,
                        company_size=contact.get("company_size") or None,
                        status=contact.get("status") or None,
                        tags=contact.get("tags") or None,
                        mailing_street=address_list[0]['address'] if address_list else None,
                        mailing_city=address_list[0]["city"] if address_list else None,
                        mailing_state=address_list[0]["state"] if address_list else None,
                        mailing_country=address_list[0]["country_code"] if address_list else None,
                        mailing_zip=address_list[0]["zip_code"] if address_list else None,
                        created_date=contact.get("created_at") or None,
                        updated_date=contact.get("modified_at")
                        )
                    contact_obj.append(contact_value.__dict__)

        return json.dumps(contact_obj)

    def contact_by_name(self, context, payload):
        ''' gets contact information based on name'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contacts = client.get('contacts')['contacts']
        contact_obj = []

        for contact in contacts:
            if payload['first_name'] == contact.get('contact').get('first_name'):
                contact = contact.get('contact') or None
                address_list = contact.get("address_list")
                contact_value = OnepagecrmContact(
                    contact_id=contact.get("id") or None,
                    first_name=contact.get("first_name") or None,
                    last_name=contact.get("last_name") or None,
                    job_title=contact.get("job_title") or None,
                    company_id=contact.get("company_id") or None,
                    owner_id=contact.get("owner_id") or None,
                    company=contact.get("company_name") or None,
                    company_size=contact.get("company_size") or None,
                    status=contact.get("status") or None,
                    tags=contact.get("tags") or None,
                    mailing_street=address_list[0]['address'] if address_list else None,
                    mailing_city=address_list[0]["city"] if address_list else None,
                    mailing_state=address_list[0]["state"] if address_list else None,
                    mailing_country=address_list[0]["country_code"] if address_list else None,
                    mailing_zip=address_list[0]["zip_code"] if address_list else None,
                    created_date=contact.get("created_at") or None,
                    updated_date=contact.get("modified_at") or None
                    )
                contact_obj.append(contact_value.__dict__)
        
        return json.dumps(contact_obj)

    def updated_contacts_by_date_range(self, context, payload):
        ''' gets contact information based on date modified'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contacts = client.get('contacts')['contacts']
        contact_obj = []

        for contact in contacts:
            if int(payload["start_date"]) > util.date_format_to_epoch(contact['contact']['modified_at']) and util.date_format_to_epoch(contact['contact']['modified_at']) < int(payload["end_date"]):
                contact = contact.get('contact') or None
                address_list = contact.get("address_list")
                contact_value = OnepagecrmContact(
                    contact_id=contact.get("id") or None,
                    first_name=contact.get("first_name") or None,
                    last_name=contact.get("last_name") or None,
                    job_title=contact.get("job_title") or None,
                    company_id=contact.get("company_id") or None,
                    owner_id=contact.get("owner_id") or None,
                    company=contact.get("company_name") or None,
                    company_size=contact.get("company_size") or None,
                    status=contact.get("status") or None,
                    tags=contact.get("tags") or None,
                    mailing_street=address_list[0]['address'] if address_list else None,
                    mailing_city=address_list[0]["city"] if address_list else None,
                    mailing_state=address_list[0]["state"] if address_list else None,
                    mailing_country=address_list[0]["country_code"] if address_list else None,
                    mailing_zip=address_list[0]["zip_code"] if address_list else None,
                    created_date=contact.get("created_at") or None,
                    updated_date=contact.get("modified_at") or None
                    )
                contact_obj.append(contact_value.__dict__)

        return json.dumps(contact_obj)

    def new_contacts_by_date_range(self, context, payload):
        ''' gets contact information based on created'''

        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contacts = client.get('contacts')['contacts']
        contact_obj = []

        for contact in contacts:
            if int(payload["start_date"]) > util.date_format_to_epoch(contact['contact']['created_at']) and util.date_format_to_epoch(contact['contact']['created_at']) < int(payload["end_date"]):
                contact = contact.get('contact') or None
                address_list = contact.get("address_list")
                contact_value = OnepagecrmContact(
                    contact_id=contact.get("id") or None,
                    first_name=contact.get("first_name") or None,
                    last_name=contact.get("last_name") or None,
                    job_title=contact.get("job_title") or None,
                    company_id=contact.get("company_id") or None,
                    owner_id=contact.get("owner_id") or None,
                    company=contact.get("company_name") or None,
                    company_size=contact.get("company_size") or None,
                    status=contact.get("status") or None,
                    tags=contact.get("tags") or None,
                    mailing_street=address_list[0]['address'] if address_list else None,
                    mailing_city=address_list[0]["city"] if address_list else None,
                    mailing_state=address_list[0]["state"] if address_list else None,
                    mailing_country=address_list[0]["country_code"] if address_list else None,
                    mailing_zip=address_list[0]["zip_code"] if address_list else None,
                    created_date=contact.get("created_at") or None,
                    updated_date=contact.get("modified_at") or None
                    )
                contact_obj.append(contact_value.__dict__)

        return json.dumps(contact_obj)
    
    def contacts_by_phone_number(self, context, params):
        """
        get contacts by phone number
        """
        client = OnePageCRMAPI(context["headers"]['user_id'], context["headers"]['api_key'])
        contacts = client.get('contacts',phone=params['phone_number'])['contacts']
        contact_obj = []

        for contact in contacts:
            
            contact = contact.get('contact') or None
            address_list = contact.get("address_list")
            for phone in contact.get('phones'):
                if phone['type'] == 'work':
                    phone_number = phone['value']
                else:
                    phone_number = None
            contact_value = OnepagecrmContact(
                        contact_id=contact.get("id") or None,
                        email=contact.get('emails')[0]['value'] if len(contact.get('emails')) > 0 else None,
                        first_name=contact.get("first_name") or None,
                        last_name=contact.get("last_name") or None,
                        job_title=contact.get("job_title") or None,
                        phone_work=phone_number ,
                        company_id=contact.get("company_id") or None,
                        owner_id=contact.get("owner_id") or None,
                        company=contact.get("company_name") or None,
                        company_size=contact.get("company_size") or None,
                        status=contact.get("status") or None,
                        tags=contact.get("tags") or None,
                        mailing_street=address_list[0]['address'] if address_list else None,
                        mailing_city=address_list[0]["city"] if address_list else None,
                        mailing_state=address_list[0]["state"] if address_list else None,
                        mailing_country=address_list[0]["country_code"] if address_list else None,
                        mailing_zip=address_list[0]["zip_code"] if address_list else None,
                        created_date=contact.get("created_at") or None,
                        updated_date=contact.get("modified_at") or None
                        )
            contact_obj.append(contact_value.__dict__)

        return json.dumps(contact_obj)

    def profile(self, context, params):
        """
        get call to show authenticated user information
        """
        api_key = context["headers"]["user_id"]+str(":")+context["headers"]["api_key"]
        api_bytes = api_key.encode('ascii')
        access_token = (base64.b64encode(api_bytes)).decode("utf-8")
        url = f"https://app.onepagecrm.com/api/v3/bootstrap"
        headers = {
            "Authorization": f"Basic {access_token}"
        }
        response = requests.request("GET",url,headers=headers)
        profile = {
            'id' : (response.json())['data']['user']['user']['id'],
            "name" : (response.json())['data']['user']['user']['first_name'],
            "email" : (response.json())['data']['user']['user']['email']
        }
        return profile

    def verify(self, context, params):
        """
        get call to verify user authenticated information
        """
        api_key = context["headers"]["user_id"]+str(":")+context["headers"]["api_key"]
        api_bytes = api_key.encode('ascii')
        access_token = (base64.b64encode(api_bytes)).decode("utf-8")
        url = f"https://app.onepagecrm.com/api/v3/users"
        headers = {
            "Authorization": f"Basic {access_token}"
        }
        response = requests.request("GET",url,headers=headers)
        return response.json()