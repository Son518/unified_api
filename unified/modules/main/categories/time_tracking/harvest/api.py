import json
from time_tracking.harvest import util


class HarvestApi():

    def profile(self, context, params):
        """Get profile details"""

        response_data = util.rest("GET", "users/me", context)
        response = json.loads(response_data.text)
        if response_data.ok:
            data = {
                "id": response["id"],
                "name": response["first_name"]+" "+response["last_name"],
                "email": response["email"]
            }
            return data
        return response

    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params)
