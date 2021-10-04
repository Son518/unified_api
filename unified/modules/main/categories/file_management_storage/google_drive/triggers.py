from unified.core.triggers import Triggers
from file_management_storage.google_drive import util
import json


class GoogledriveTriggers(Triggers):

    # Get webhook response from Google drive  
    # As it required to be on a verified domain to save a webhook
    def notification(self, context, payload):
        url = "https://googledriveapplication.free.beeceptor.com"
        res = {
            'payload': payload,
            'headers': context,
            'params' : {**request.args}
        }
        response = util.rest("post", url, 'token', res)
        return json.dumps(response.text)
