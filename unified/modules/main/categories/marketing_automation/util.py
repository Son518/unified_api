from datetime import datetime, timezone
import requests
import base64


def rest(method, url, body, context):
    ''' returns response from request'''

    api_key = context.get("headers").get("Api-Key")
    api_appid = context.get("headers").get("Api-Appid")
    headers = {
        "Api-Key": f"{api_key}",
        "Api-Appid": f"{api_appid}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.request(method, url, headers=headers, data=body)

    return response


def epoch_to_format(format, epoch):
    '''Convert  epoch to given format '''
    return datetime.fromtimestamp(int(epoch[:10]), tz=timezone.utc).strftime(format)
