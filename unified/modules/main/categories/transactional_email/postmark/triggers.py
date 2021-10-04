import json
from requests.models import Response
from core.triggers import Triggers
from transactional_email.postmark.entities.postmark_bounce import PostmarkBounce
from transactional_email.postmark.entities.postmark_email_open import PostmarkEmailOpen

class PostmarkTriggers(Triggers):

    def new_bounce(self,context,payload):
        """
        triggers when new_bounce created 
        context holds the headers 
        payload holds the request.body
        """
        data = PostmarkBounce(
                    record_type=payload['RecordType'],
                    id=payload["ID"],
                    type=payload["Type"],
                    type_code=payload["TypeCode"],
                    name=payload["Name"],
                    tag=payload["Tag"],
                    message_id=payload["MessageID"],
                    server_id=payload["ServerID"],
                    message_stream=payload["MessageStream"],
                    description=payload["Description"],
                    details=payload["Details"],
                    content=payload["Content"],
                    email=payload["Email"],
                    From=payload["From"],
                    bounced_at=payload["BouncedAt"],
                    dump_available=payload["DumpAvailable"],
                    inactive=payload["Inactive"],
                    canActivate=payload["CanActivate"],
                    subject=payload["Subject"],
                    metadata=payload["Metadata"]
                )
        return data.__dict__
            
    def new_email_open(self,context,payload):
        """
        triggers when new email open created
        context holds the headers 
        payload holds the request.body
        """
        email = PostmarkEmailOpen(
                    record_type=payload["RecordType"],
                    first_open=payload["FirstOpen"],
                    client=payload["Client"],
                    platform=payload["Platform"],
                    user_Agent=payload["UserAgent"],
                    read_Seconds=payload["ReadSeconds"],
                    geo=payload["Geo"],
                    message_id=payload["MessageID"],
                    received_At=payload["ReceivedAt"],
                    tag=payload["Tag"],
                    recipient=payload["Recipient"],
                    message_stream=payload["MessageStream"],
                    metadata=payload["Metadata"]
                    )                  
        return email.__dict__
