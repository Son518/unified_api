import requests

def rest(method, url, context, body=None):
    api_key = context['headers'].get('api_key')
    if method == 'GET':
        # https://api.hubapi.com/companies/v2/companies/6247773847
        BASE_URL = f"https://api.hubapi.com/{url}?hapikey={api_key}"
    else:
        BASE_URL = f"https://api.hubapi.com/crm/v3/objects/{url}?hapikey={api_key}"
    print(BASE_URL)

    headers = {
        "Content-Type": "application/json"
    }
    return requests.request(method, BASE_URL, headers=headers, json=body)