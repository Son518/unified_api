# Global configuration
import logging

from os import environ
import os

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
LOGGER_FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)

APP_NAME = "unified2"

S3_BUCKET = "flow.ly"

BROWSER_SECRET_KEY = 'J3pxgqJp9KZhNygU'

# When behind a load balancer, set CANONICAL_NAME to the value contained in
CANONICAL_NAME = '127.0.0.1'

# When behind a load balancer, set CANONICAL_PORT to the value contained in
# Host headers (normally it will be '80' in production)
CANONICAL_PORT = '8080'

JWT_SECRET = "DA693C13E7C5528473D915EB827E"

PROJECT_JWT_SECRET = "tMBLJZCQOnhuS5426KUH1mlm9TzmfXgP"

DEBUG = True
LISTEN_HOST = '127.0.0.1'
PASSWORD_HASH = 'J3pxgqJp9KZhNygU'
SECRET_KEY = 'J3pxgqJp9KZhNygU'
SESSION_BYTES = 25
SESSION_COOKIE_NAME = 'skeleton_session'
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True

AWS_ACCESS_KEY_ID = 'AKIATA54FKDA3R5EJHDO'
AWS_SECRET_ACCESS_KEY = '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'
REGION_NAME = 'us-east-1'
# If users want to pass specific werkzeug options
WERKZEUG_OPTS = {'host': LISTEN_HOST, 'port': 6050}

# Import user-provided values
try:
    from local_settings import *
except ImportError:
    pass

database = "sys"
if (environ.get('DB_HOSTNAME')):
    DB_CONFIG = {
        "host": environ.get('DB_HOSTNAME'),
        "user": environ.get('DB_USER_NAME'),
        "password": environ.get('DB_PASSWORD'),
        "database": database
    }
else:  # localhost
    DB_CONFIG = {
        "host": "aurora-infinity-cluster-ap1-dev.cluster-ca6wwmhuoxcw.ap-south-1.rds.amazonaws.com",
        "user": "developers",
        "password": "SE209aL@zR7yqK94",
        "database": database
    }