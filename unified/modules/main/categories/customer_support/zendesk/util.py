from zenpy import Zenpy
from datetime import datetime ,timezone

def get_zendesk_client(headers):
    '''
    There are several ways to authenticate with the Zendesk API:
            * Email and password
    subdomain: your Zendesk subdomain
    '''
    credentials = {
                    "email":headers["username"],
                    "password":headers["password"],
                    "subdomain":headers["domain"]
                  }
    zenpy_client = Zenpy(**credentials)
    return zenpy_client

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)

