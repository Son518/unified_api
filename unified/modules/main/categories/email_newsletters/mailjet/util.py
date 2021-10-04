from mailjet_rest import Client
from flask import request


def mailjet_client(headers):

    api_key = headers["api_key"]
    api_secret = headers["api_secret"]
    mailjet_client = Client(auth=(api_key, api_secret), version='v3')
    return mailjet_client

