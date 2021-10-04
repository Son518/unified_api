from file_management_storage.dropbox import util
from file_management_storage.entities.profile import Profile
import requests
import json


class DropboxApi:
    def profile(self, context, payload):
        '''profile details of user'''

        access_token = util.get_access_token(context['headers'])
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        url = "https://api.dropboxapi.com/2/users/get_current_account"
        payload = json.dumps(None)
        response = json.loads(requests.request(
            "POST", url, headers=headers, data=payload).text)
        profile = Profile(
            id=response.get("account_id"),
            email=response.get('email'),
            logo=response.get('profile_photo_url'),
            name=response.get('name').get("display_name"),
        ).__dict__
        return profile
