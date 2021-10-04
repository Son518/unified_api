import json


from marketing_automation.keap_max_classic import util
from marketing_automation.keap_max_classic.entities.keap_contact import KeapContact

class KeapMaxClassicApi():

    def contact(self, context, params):
        '''Finds contact by id'''

        headers = context['headers']
        method = 'GET'

        optional_properties = ("id,given_name,family_name,job_title,suffix,birthday,anniversary,website,company,"
            "phone_numbers,fax_numbers,social_accounts,addresses,social_accounts")
        url = '/contacts/{id}?optional_properties={optional_properties}'.format(id=params['contact_id'], optional_properties=optional_properties)
        result = json.loads(util.get_keap_request(method, url, headers).text)

        keap_contact = KeapContact(
            contact_id = result["id"],
            first_name = result["given_name"],
            last_name = result["family_name"],
            job_title = result["job_title"],
            suffix = result["suffix"],
            birthday = result["birthday"],
            anniversary = result["anniversary"],
            website = result["website"],
            company = result["company"]
            )
        for phone in result["phone_numbers"]:
            if phone["field"] == "PHONE1":
                keap_contact.phone1 = phone["number"]
                break
        for fax in result["fax_numbers"]:
            if fax["field"] == "FAX1":
                keap_contact.fax1 = fax["number"]
                break
        for email in result["email_addresses"]:
            if email["field"] == "EMAIL1":
                keap_contact.email = email["email"]
                break
        for address in result["addresses"]:
            if address["field"] == "BILLING":
                keap_contact.billing_address_country = address["country_code"]
                keap_contact.billing_address_street_line1 = address["line1"]
                keap_contact.billing_address_street_line2 = address["line2"]
                keap_contact.billing_address_city = address["locality"]
                keap_contact.billing_address_state = address["region"]
                keap_contact.billing_address_zip_code = address["zip_code"]
            if address["field"] == "SHIPPING":
                keap_contact.shipping_address_country = address["country_code"]
                keap_contact.shipping_address_street_line1 = address["line1"]
                keap_contact.shipping_address_street_line2 = address["line2"]
                keap_contact.shipping_address_city = address["locality"]
                keap_contact.shipping_address_state = address["region"]
                keap_contact.shipping_address_zip_code = address["zip_code"]
            if address["field"] == "OTHER":
                keap_contact.optional_address_country = address["country_code"]
                keap_contact.optional_address_street_line1 = address["line1"]
                keap_contact.optional_address_street_line2 = address["line2"]
                keap_contact.optional_address_city = address["locality"]
                keap_contact.optional_address_state = address["region"]
                keap_contact.optional_address_zip_code = address["zip_code"]
        for account in result["social_accounts"]:
            if account["type"] == "Facebook":
                keap_contact.facebook = account["name"]
            if account["type"] == "LinkedIn":
                keap_contact.linked_in = account["name"]
            if account["type"] == "Twitter":
                keap_contact.twitter = account["name"]

        return keap_contact.__dict__

    def invoice(self, context, params):
        '''Finds invoice by id'''

        pass
