import json
from requests.models import Response
from core.actions import Actions
from social_media.pinterest import util
from social_media.pinterest.entities.pinterest_pin import PinterestPin

class PinterestActions(Actions):
    
    def create_pin(self, context, payload):
        """
        Creates a pin
        context holds the headers 
        payload holds the request.body
        """
        access_token = util.get_access_token(context["headers"])
        pin_entity = PinterestPin(**payload)
        endpoint = "pins"
        data = {
                "board_id": pin_entity.board_id,
                "media_source": {
                    "source_type": pin_entity.source_type,
                    "url": pin_entity.image_url      
                }
            }       
        if pin_entity.link:
            data["link"]=pin_entity.link
        if pin_entity.title:
            data["title"]=pin_entity.title
        if pin_entity.description:
            data["description"]=pin_entity.description

        response = util.rest("POST",endpoint,access_token,data)
        # if the response code is 200,201 it will go to if condition.
        if response.ok:
            return json.loads(response.text)
        else:
            return {"error":json.loads(response.text)}, response.status_code