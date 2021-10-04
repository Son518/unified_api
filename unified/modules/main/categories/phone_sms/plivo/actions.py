import json
from plivo import plivoxml
from core.actions import Actions
from phone_sms.plivo import util
from phone_sms.plivo.entities.plivo_send_sms import PlivoSendsms
from flask import jsonify


class PlivoActions(Actions):

    def send_sms(self, context, sms_payload):
        """ 
        Send new sms 
        context holds the headers 
        send_sms_entity holds the request.body
        """
        client = util.plivo_client(context["headers"])
        sms_entity = PlivoSendsms(**sms_payload)
        response =client.messages.create(
            src=sms_entity.source_number,
            dst=sms_entity.destination_number,
            text=sms_entity.text).__dict__
       
        return response

