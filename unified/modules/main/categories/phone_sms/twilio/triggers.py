import json
from core.triggers import Triggers
from phone_sms.twilio.entities.twilio_phone import TwilioPhone
from phone_sms.twilio.entities.twilio_sms import TwilioSms


class TwilioTriggers(Triggers):

    def new_phone_number(self,context,payload):
        """
        triggers when new_phone call made  
        context holds the headers 
        payload holds the request.body
        """
        phone=TwilioPhone(
                    to_number=payload["To"],
                    from_number=payload["From"]
                    )
        return phone.__dict__
         
    def new_sms(self,context,payload):
        """
        triggers when new message sended 
        context holds the headers 
        payload holds the request.body
        """
        sms = TwilioSms(
                    to_number=payload["To"],
                    from_number=payload["From"]
                    )                  
        return sms.__dict__
