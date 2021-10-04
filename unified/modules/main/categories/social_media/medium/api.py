from social_media.medium import util
import json
import requests

class MediumAPI:

    def profile(self, context, params):
        """Get profile details"""

        access_token = context['headers'].get("access_token")
        response_data = util.rest("GET", f"me", access_token)
        response = json.loads(response_data.text)
        response = response["data"]
        if response_data.ok:
            data = {
                "id": response["id"],
                "username": response["username"],
                "name": response["name"],
                "email": response.get("email")
            }
            return data
        return response
    
    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params)