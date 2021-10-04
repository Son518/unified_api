import json
from core.actions import Actions
from social_media.linkedin import util
from social_media.linkedin.entities.linkedin_share import LinkedinShare


class LinkedinActions(Actions):
        
    def create_share_update(self,context,share_payload):
        """
        Shares update on page
        context holds the headers 
        share_payload holds the request.body
        """
        access_token = util.get_access_token(context['headers'])
        share_entity = LinkedinShare(**share_payload)
        person_id = json.loads(util.rest("GET","https://api.linkedin.com/v2/me",access_token).text)['id']
        data = {
                "content": {
                    "contentEntities": [
                        {
                            "entityLocation": share_entity.url
                        }
                    ],
                    "thumbnails": [
                                {
                                    "resolvedUrl": share_entity.content_image_url
                                }
                            ]
                },
                "owner": f"urn:li:person:{person_id}",
                "text": {
                    "text": share_entity.comment
                }
            }
        if share_entity.description:
            data["subject"] = share_entity.description
        if share_entity.title:
            data["content"]["title"] = share_entity.title
        response = util.rest("POST","https://api.linkedin.com/v2/shares",access_token,data).text
        return json.loads(response)