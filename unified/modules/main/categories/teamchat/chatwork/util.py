import json
from pychatworkAPI import Chatwork
from datetime import datetime, timezone


def get_chatwork_client(headers):
    ''' returns sdk client'''
    client = Chatwork(headers["api_key"])
    return client


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def date_format_to_epoch(date):
    ''' convert date format to epoch'''

    return int(datetime.strptime(date, "%Y-%m-%d").timestamp())
