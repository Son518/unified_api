import clicksend_client

from flask import Response, request

def get_clicksend_configuration(clicksend_sms_headers):
    '''Authentication for Clicksend API'''

    configuration = clicksend_client.Configuration()
    configuration.username = clicksend_sms_headers['username']
    configuration.password = clicksend_sms_headers['password']

    return configuration
