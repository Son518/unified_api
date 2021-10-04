import json
import base64

from unified.core.actions import Actions
from marketing_automation.keap_max_classic.entities.keap_company import KeapCompany
from marketing_automation.keap_max_classic.entities.keap_contact import KeapContact
from marketing_automation.keap_max_classic.entities.keap_note import KeapNote
from marketing_automation.keap_max_classic.entities.keap_product import KeapProduct
from marketing_automation.keap_max_classic.entities.keap_email import KeapEmail
from marketing_automation.keap_max_classic.entities.keap_tag import KeapTag
from marketing_automation.keap_max_classic import util

class KeapMaxClassicActions(Actions):

    def create_company(self, context, task_entity):
        '''Creates a company'''

        task_schema = KeapCompany(**task_entity)
        method = "POST"
        url = "/companies"
        task_data = {
            "address":
                {
                  "country_code": task_schema.country,
                  "line1": task_schema.street_address1,
                  "line2": task_schema.street_address2,
                  "locality": task_schema.city,
                  "region": task_schema.state,
                  "zip_code": task_schema.postal_code
                },
            "company_name": task_schema.company,
            "email_address": task_schema.email,
            "phone_number": {
                "number": task_schema.phone1
            },
            "fax_number": {
                "number": task_schema.fax1
            },
            "website": task_schema.website
            }
        result = util.get_keap_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_contact(self, context, task_entity):
        '''Creates a contact'''

        task_schema = KeapContact(**task_entity)
        method = "POST"
        url = "/contacts"
        task_data = util.create_task_payload(task_schema)
        result = util.get_keap_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_note(self, context, task_entity):
        '''Creates a note'''

        task_schema = KeapNote(**task_entity)
        method = "POST"
        url = "/notes"
        task_data = {
            "contact_id": task_schema.contact_id,
            "title": task_schema.title,
            "body": task_schema.description,
            "user_id": task_schema.created_by
            }

        result = util.get_keap_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def create_product(self, context, task_entity):
        '''Creates a product'''

        task_schema = KeapProduct(**task_entity)
        method = "POST"
        url = "/products"
        task_data = {
            "product_name": task_schema.product_name,
            "product_price": task_schema.product_price,
            "product_short_desc": task_schema.description,
            "sku": task_schema.sku
            }

        result = util.get_keap_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)

    def send_email(self, context, task_entity):
        '''Send an email'''

        task_schema = KeapEmail(**task_entity)
        method = "POST"
        url = "/emails/queue"

        encoded_data = base64.b64encode(task_schema.file_data.encode("utf-8"))
        task_schema.file_data = str(encoded_data, "utf-8")

        task_data = {
            "contacts": [task_schema.contacts_id],
            "attachments": [
                {
                  "file_data": task_schema.file_data,
                  "file_name": task_schema.file_name
                }
              ],
            "user_id": task_schema.user_id,
            "subject": task_schema.subject,
            }

        if task_schema.text_body:
            encoded_body = base64.b64encode(task_schema.text_body.encode("utf-8"))
            encoded_str = str(encoded_body, "utf-8")
            task_data["plain_content"] = encoded_str
        if task_schema.html_body:
            encoded_body = base64.b64encode(task_schema.html_body.encode("utf-8"))
            encoded_str = str(encoded_body, "utf-8")
            task_data["html_content"] = encoded_str
        result = util.get_keap_request(method, url, context['headers'], body=task_data)
        if result.status_code == 202:
            response = {"completed": 202}
        return response

    def update_contact(self, context, task_entity):
        '''Updates a contact'''

        task_schema = KeapContact(**task_entity)
        method = "PATCH"
        url = "/contacts/{}".format(task_schema.contact_id)
        task_data = util.create_task_payload(task_schema)
        result = util.get_keap_request(method, url, context['headers'], body=task_data)
        return json.loads(result.text)
