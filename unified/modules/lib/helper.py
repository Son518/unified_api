import boto3
from os import environ
from types import SimpleNamespace
from default_settings import AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,REGION_NAME


class utils(object):
    """docstring for aws"""

    def __init__(self):
        super(utils, self).__init__()

    def aws(self):
        session = boto3.session.Session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                                        region_name=REGION_NAME)
        return session
