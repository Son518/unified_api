import json
import requests


class JotFormAPI():

    def form_submissions(self, context, params):
        """ Get form submission"""

        params_obj = {
            "apiKey": context["headers"]["api_key"]
        }

        if "limit" in params:
            params_obj["limit"] = params["limit"]

        if "order_by" in params:
            params_obj["orderby"] = params["order_by"]

        form_id = params.get('form_id')
        response = requests.request(
            "GET", f"https://api.jotform.com/form/{form_id}/submissions", params=params_obj).text
        return json.loads(response)

    def profile(self, context, params):
        """Get profile details"""

        params_obj = {
            "apiKey": context["headers"]["api_key"]
        }
        response_data = requests.request(
            "GET", f"https://api.jotform.com/user", params=params_obj)
        response = json.loads(response_data.text)

        if response_data.ok:
            response = response["content"]
            data = {
                "id": response.get("id"),
                "name": response["username"],
                "email": response["email"]
            }
            return data
        return response

    def verify(self, context, params):
        """Verify the app"""

        return self.profile(context, params)