from contacts_management.entities.contact import Contact
from contacts_management.microsoft_office_365_contacts import util
import json

class Microsoftoffice365contactsApi:
    def contacts(self, context, payload):
        access_token = util.get_access_token(context['headers'])
        url = 'https://graph.microsoft.com/beta/me/contacts'
        response = util.rest(method="GET", url=url, access_token=access_token)
        contacts_list = json.loads(response.text)['value']
        contacts = []
        for contact in contacts_list:
            contact_obj = Contact(
                contact_id=contact['id'],
                first_name=contact.get('givenName'),
                last_name=contact.get('surname'),
                email=contact.get('emailAddresses')[0]['address'] if contact.get(
                    'emailAddresses') else None,
                phone_number=contact.get(
                    'phones')[0]['number'] if contact.get('phones')else None,
                address_city=contact.get('postalAddresses')[
                    0]['city'] if contact.get('postalAddresses') else None,
                address_country=contact.get('postalAddresses')[
                    0]['countryOrRegion'] if contact.get('postalAddresses') else None,
                address_pincode=contact.get('postalAddresses')[
                    0]['postalCode'] if contact.get('postalAddresses') else None,
                address_state=contact.get('postalAddresses')[
                    0]['state'] if contact.get('postalAddresses') else None,
                address_street=contact.get('postalAddresses')[
                    0]['street'] if contact.get('postalAddresses') else None,
                company_name=contact.get('companyName'), note=contact.get('personalNotes')
            ).__dict__
            contacts.append(contact_obj)
        return json.dumps(contacts), response.status_code

    def profile(self, context, params):
        '''Details of authenticated user'''

        access_token = util.get_access_token(context['headers'])
        url = 'https://graph.microsoft.com/v1.0/me'
        response = util.rest("GET", url, access_token).json()
        profile = {
            'id':response['id'],
            'email':response['userPrincipalName'],
            'name':response['displayName']
        }
        return profile