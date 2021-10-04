import json
from anydo_api import user
from anydo_api.client import Client
from datetime import datetime, timezone

def anydo_client(headers):
    user = Client(headers["email"],headers["password"]).get_user()
    return user