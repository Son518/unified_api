import json
from scheduling_bookings.schedule_once import util


class ScheduleOnce_Api():

    def profile(self, context, params):
        """Get profile details"""

        response_data = util.rest("GET", "users", context)
        response = json.loads(response_data.text)

        if response_data.ok:
            response = response["data"][0]
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