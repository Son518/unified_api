import json
import requests
from forms_surveys.surveymonkey import util
import lib


class SurveymonkeyAPI():
    
    def collector(self, context, params):
        """ Get collector details"""

        access_token = context["headers"]["access_token"]
        id = params.get('collector_id')
        response = util.rest("GET", f"/collectors/{id}", access_token).text
        return json.loads(response)

    def survey(self, context, params):
        """ Get survey details by Id"""

        access_token = context["headers"]["access_token"]
        id = params.get('survey_id')
        response = util.rest("GET", f"/surveys/{id}", access_token).text
        return json.loads(response)

    def surveys(self, context, params):
        """ Get survey list"""

        access_token = context["headers"]["access_token"]
        response = util.rest("GET", f"/surveys", access_token).text
        return json.loads(response)

    def collectors(self, context, params):
        """ Get survey list"""

        access_token = context["headers"]["access_token"]
        survey_id = params.get("survey_id")
        response = util.rest("GET", f"/surveys/{survey_id}/collectors", access_token).text
        return json.loads(response)

    def new_surveys_by_created_time(self, context, params):
        """ Get survey by time"""

        access_token = context["headers"]["access_token"]

        if params.get("start_date_time") is not None:
            start_time = lib.util.epoch_to_format("%Y-%m-%dT%H:%M:%S", params.get("start_date_time"))
        
        if params.get("end_date_time") is not None:
            end_time = lib.util.epoch_to_format("%Y-%m-%dT%H:%M:%S", params.get("end_date_time"))

        response = util.rest("GET", f"/surveys?start_modified_at={start_time}&end_modified_at={end_time}", access_token).text
        return json.loads(response)

    def profile(self, context, params):
        """Get user profile details"""

        access_token = context["headers"]["access_token"]
        response_data = util.rest("GET", f"/users/me", access_token)
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