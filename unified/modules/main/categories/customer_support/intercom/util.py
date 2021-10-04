import json
import requests
from datetime import datetime, timezone


def rest(method, endpoint, access_token, data={}, id=None):
    """
    Makes rest api call based on method and endpoint
    """
    headers = {
        'Authorization': f"Bearer {access_token}",
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    base_url = "https://api.intercom.io/"

    # for creating and updating a companies api using POST method only
    if endpoint in ['contacts', 'companies', 'events', 'tags'] and method == 'POST':
        url = f"{base_url}{endpoint}"
    elif endpoint == 'add_tags' and method == "POST":
        url = f"{base_url}contacts/{id}/tags"
    elif (endpoint == 'contacts') and method == 'POST':
        url = f"{base_url}{endpoint}/{id}"
    elif endpoint == 'contact_email' and method == 'POST':
        url = f"{base_url}contacts/search"
    elif endpoint == 'notes' and method == 'POST':
        url = f"{base_url}contacts/{id}/notes"
    elif endpoint == 'contacts' and method == 'PUT':
        url = f"{base_url}{endpoint}/{id}"
    elif endpoint == 'tags' and method == 'DELETE':
        url = f"{base_url}contacts/{id[0]}/tags/{id[1]}"
    elif endpoint == 'contacts' and method == 'GET':
        url = f"{base_url}{endpoint}/{id}"
    elif endpoint == 'companies' and method == 'GET':
        url = f"{base_url}{endpoint}?company_id={id}"
    elif endpoint == 'admin' and method == 'GET':
        url = f'{base_url}admins'

    response = requests.request(
        method, url, headers=headers, data=json.dumps(data))
    return response


def epoch_to_date(epoch):
    if not('-' in str(epoch)):
        format = "%Y-%m-%d"
        return datetime.fromtimestamp(int(str(epoch)[:10]), tz=timezone.utc).strftime(format)
