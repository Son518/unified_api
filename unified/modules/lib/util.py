# util.py
# common utility functions
import json
import jwt
import base64
from default_settings import logger,PROJECT_JWT_SECRET
from flask_httpauth import HTTPTokenAuth
from default_settings import logger
from datetime import datetime, timezone


applet_token = HTTPTokenAuth(scheme='Bearer')

# TODO: Use cache?
def get_json_from_file(path):
    """Get json object from .json file
    """

    try:
        with open(path) as f:
            return json.load(f)

    except Exception as err:
        logger.error(err)
        return None


# for the mapping as below. This is faster:
# {
#     "first": "first_name",
#     "firstname": "first_name",
#     "first-name": "first_name",

#     "last": "last_name",
#     "lastname": "last_name",
#     "last_name": "last_name",
# }

def unify_payload(input_payload, payload_mapping):
    if not payload_mapping:
        return input_payload

    unified_payload = {}

    for key in input_payload:
        if key in payload_mapping:
            unified_payload[payload_mapping[key]] = input_payload[key]
        else:  # copy as-is
            unified_payload[key] = input_payload[key]

    return unified_payload


# for the mapping as below. This slower, looks cleaner.
# field_mapping2 = {
#     "first_name" : ["first", "firstname", "first_name", "fname", "first name", "first-name"],
#     "last_name" : ["last", "lastname", "last_name", "lname", "last name", "last-name"],
#     "phone" : ["phone", "home_phone", "home-phone", "personal_phone", "personal-phone", "mobile", "mobile-number"],
#     "work_phone" : ["phone2", "business_phone", "work_phone", "office_phone", "work-phone", "office-phone"],
# }

def unify_payload2(input_payload, field_mapping):
    unified_payload = {}

    for in_key in input_payload:
        in_key_found = False
        for fld_key in field_mapping:
            if in_key in field_mapping[fld_key]:
                unified_payload[fld_key] = input_payload[in_key]
                in_key_found = True
                break

        if not in_key_found:  # copy as-is
            unified_payload[in_key] = input_payload[in_key]

    return unified_payload    

@applet_token.verify_token
def verify_project_token(token):

    if not token:
        return False

    payload = jwt.decode(token, base64.b64decode(PROJECT_JWT_SECRET), algorithms=["HS256"])
    email = payload.get("email", None)
    domain_id = payload.get("tenant_id", None)
    user_id = payload.get("user_id", None)
    project_id = payload.get("project_id", None)

    # 0 (zero) is passed for project_id in plugins call
    if not (email and domain_id and user_id) and project_id is None:
        return False

    return {
        "email": email,
        "domain_id": domain_id,
        "user_id": user_id,
        "project_id": project_id,
        "token": token,
    }
    return unified_payload

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''

    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)