import json
from twilio.rest import Client


def twilio_client(headers):
    client = Client(headers["accountsid"],headers["authtoken"])
    return client