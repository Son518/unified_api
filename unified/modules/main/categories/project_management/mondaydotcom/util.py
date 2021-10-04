import json
import requests

url = "https://api.monday.com/v2"

def rest(method,headers_data,payload):

    headers = {
            'Authorization': headers_data["access_token"]
            }
    data = {"query": payload}
    
    response = requests.request(method, url, json=data, headers=headers)
    return response


def epoch_to_format(format,epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
