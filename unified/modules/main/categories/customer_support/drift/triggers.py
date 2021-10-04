from unified.core.triggers import Triggers
from customer_support.drift.entities.drift_message import DriftMessage

class DriftTriggers(Triggers):
    
    def new_message(self, context, payload):
        """
        triggers when new message created
        context holds the headers 
        payload holds the request.body
        """
        author=payload['data']['author']
        location=payload['data']['context']['location']
        data=payload['data']
        message = DriftMessage(
                                orgId=payload['orgId'],
                                type=payload['type'],
                                data_id=data['id'],
                                conversationId=data['conversationId'],
                                body=data['body'],
                                author_id=author['id'],
                                author_type=author['type'],
                                author_bot=author['bot'],
                                data_type=data['type'],
                                createdAt=data['createdAt'],
                                context_ip=data['context']['ip'],
                                location_city=location['city'],
                                region=location['region'],
                                country=location['country'],
                                countryName=location['countryName'],
                                postalCode=location['postalCode'],
                                latitude=location['latitude'],
                                longitude=location['longitude'],
                                attributes=data['attributes'],
                                token=payload['token']
                            )
        return message.__dict__