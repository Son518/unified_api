import json
import requests
from datetime import datetime, timezone
from getresponse.client import GetResponse
from datetime import date
from getresponse.excs import UniquePropertyError


def getresponse_authentication(headers):
    ''' returns Getresponse client'''
    
    getresponse = GetResponse(f'{headers["api_key"]}')
    return getresponse

def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)


def property_conversion(properties):
    '''converts list of values into required fields'''

    return {item['name']: item.get('value') for item in properties}