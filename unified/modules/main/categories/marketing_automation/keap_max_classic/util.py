import json
import requests

from flask import Response, request
from datetime import datetime, timezone
from unified.core.auth import Auth


def get_access_token(headers):
    # Rest api Instance
    auth_info = {
        "client_id": headers['client_id'],
        "client_secret": headers['client_secret'],
        "token": headers['refresh_token'],
        "refresh_url": headers['refresh_url'],
    }

    token = Auth().get_oauth2_token(auth_info)
    return (json.loads(token))
def get_keap_request(method: str, url:str, keap_headers, body=None):


    API_URL = "https://api.infusionsoft.com/crm/rest/v1/"
    final_url = API_URL + url

    keap_headers = {'Authorization' : 'Bearer '+keap_headers["token"],
                    "Content-Type" : "application/json",
               }

    return requests.request(method, final_url, headers=keap_headers, json=body)

def create_task_payload(task_schema):
    task_data = {
         "email_addresses": [
            {
              "email": task_schema.email,
              "field": "EMAIL1"
            }
          ],
        "given_name": task_schema.first_name,
        "family_name": task_schema.last_name,
        "job_title": task_schema.job_title,
        "suffix": task_schema.suffix,
        "company": {
            "id": task_schema.company
          },
        "birthday": task_schema.birthday,
        "anniversary": task_schema.anniversary,
        "phone_numbers": [
            {
              "field": "PHONE1",
              "number": task_schema.phone1
            }
          ],
        "fax_numbers": [
            {
              "field": "FAX1",
              "number": task_schema.fax1
            }
          ],
        "website": task_schema.website,
        "social_accounts": [
            {
              "name": task_schema.facebook,
              "type": "Facebook"
            },
            {
              "name": task_schema.linked_in,
              "type": "LinkedIn"
            },
            {
              "name": task_schema.twitter,
              "type": "Twitter"
            }
          ],
        "addresses": [
            {
              "country_code": task_schema.billing_address_country,
              "field": "BILLING",
              "line1": task_schema.billing_address_street_line1,
              "line2": task_schema.billing_address_street_line2,
              "locality": task_schema.billing_address_city,
              "region": task_schema.billing_address_state,
              "zip_code": task_schema.billing_address_zip_code

                },
            {
              "country_code": task_schema.shipping_address_country,
              "field": "SHIPPING",
              "line1": task_schema.shipping_address_street_line1,
              "line2": task_schema.shipping_address_street_line2,
              "locality": task_schema.shipping_address_city,
              "region": task_schema.shipping_address_state,
              "zip_code": task_schema.shipping_address_zip_code

                },
            {
              "country_code": task_schema.optional_address_country,
              "field": "OTHER",
              "line1": task_schema.optional_address_street_line1,
              "line2": task_schema.optional_address_street_line2,
              "locality": task_schema.optional_address_city,
              "region": task_schema.optional_address_state,
              "zip_code": task_schema.optional_address_zip_code

                }
              ],
    }
    return task_data
