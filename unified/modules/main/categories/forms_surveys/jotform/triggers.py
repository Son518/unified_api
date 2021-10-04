from unified.core.triggers import Triggers
import json


class JotFormTriggers(Triggers):

    def new_form_submission(self, context, payload):
        """ Trigger for new form submission""" 

        if payload.get("rawRequest") is not None:
            return payload.get("rawRequest")
        return {"Message": "Unsupported data and Content-Type"}