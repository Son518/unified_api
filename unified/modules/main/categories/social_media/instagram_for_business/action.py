
from unified.core.actions import Actions
from social_media.instagram_for_business.entities.instagram_publish_photo import InstagramPublishPhoto
from social_media.instagram_for_business import util
import json

class InstagramforbusinessAction(Actions):

    def publish_photo(self, context, payload):
        '''Publish a photo to your feed.'''

        access_token = context['headers'].get('access_token')
        publish_photo = InstagramPublishPhoto(**payload)
        url = f'{publish_photo.instagram_account_id}/media'
        payload = {
            "image_url": publish_photo.photo_url,
            "caption": publish_photo.caption
        }
        if publish_photo.tagged_users:
            payload["user_tags"]= [{
                    "username": publish_photo.tagged_users,
                    "x": 0.5,
                    "y": 1.0
                }]
        response = util.rest("POST", url, access_token, payload)
        result = json.loads(response.text)
        if 'id' in result:
            creation_id = result['id']

            # Publish media url to instagram
            second_url = f'{publish_photo.instagram_account_id}/media_publish'
            publish_content = {
                'creation_id': creation_id
            }
            response = util.rest("POST", second_url,
                                 access_token, publish_content)
            return response.text
        else:
            raise Exception("Cannot Publish!!")
