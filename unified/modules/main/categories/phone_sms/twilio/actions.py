import json
from twilio.rest.api.v2010.account import message
from core.actions import Actions
from phone_sms.twilio import util
from phone_sms.twilio.entities.twilio_sms import TwilioSms
from phone_sms.twilio.entities.twilio_phone import TwilioPhone
from flask import jsonify


class TwilioActions(Actions):

    def call_phone(self,context,phone_payload):
        """
        creates a new ticket 
        context holds the headers 
        phone_payload holds the request.body
        """
        client = util.twilio_client(context["headers"])
        phone_entity = TwilioPhone(**phone_payload)
        call = client.calls.create(
                                to=phone_entity.to_number,
                                from_=phone_entity.from_number,
                                url=phone_entity.media_url
                                )
        return call.__dict__["_properties"]

    def send_sms(self,context,sms_payload):
        """
        creates a new ticket 
        context holds the headers 
        sms_payload holds the request.body
        """
        client = util.twilio_client(context["headers"])
        sms_entity = TwilioSms(**sms_payload)
        sms = client.messages.create(
                                to=sms_entity.to_number,
                                from_=sms_entity.from_number,
                                body=sms_entity.message
                                )                                 
        return sms.__dict__["_properties"]