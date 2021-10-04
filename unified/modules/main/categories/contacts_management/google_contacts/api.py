from contacts_management.entities.contact import Contact
from contacts_management.google_contacts import util
from unified.core.util import google_profile
import json


class GoogleContactsApi:
    def contacts(self, context, payload):
        access_token = util.get_access_token(context['headers'])
        url = "https://www.google.com/m8/feeds/contacts/default/full?alt=json"
        response = util.rest("GET", url, access_token)
        contacts_list = json.loads(response.text)['feed']['entry']
        contacts = []
        for contact in contacts_list:
            address = contact.get('gd$postalAddress')[0].get("$t").split(
                '\n') if contact.get('gd$postalAddress') else None
            contact_obj = Contact(
                contact_id=contact.get('id').get("$t").split(
                    '/')[-1] if contact.get('id') else None,
                first_name=contact.get('title').get("$t"),
                note=contact.get('content').get(
                    "$t") if contact.get('content') else None,
                company_name=contact.get('gd$organization')[0].get('gd$orgName').get(
                    '$t') if contact.get('gd$organization') else None,
                email=contact.get('gd$email')[0].get(
                    'address') if contact.get('gd$email') else None,
                phone_number=contact.get('gd$phoneNumber')[0].get(
                    "$t") if contact.get('gd$phoneNumber') else None,
                address_country=address[-1] if address else None,
                address_pincode=address[-2].split()[-1] if address else None,
                address_state=address[-2].split()[-2] if address else None,
                address_city=address[-2].split()[0] if address else None,
                address_street=address[0] if address else None,
                address_street_line2=address[1] if address else None
            ).__dict__
            contacts.append(contact_obj)
        return json.dumps(contacts), response.status_code
    
    def profile(self, context, params):
        '''Details of authenticated user'''

        return google_profile(context, params)
