from unified.core.actions import Actions
from social_media.medium import util
from social_media.medium.entities.medium_story import MediumStory
import json


class MediumAction(Actions):

    def create_story(self, context, payload):
        """Create a story"""

        payload = MediumStory(**payload)
        access_token = context['headers'].get("access_token")
        user_id = context['headers'].get("user_id")
        data = {
            "title": payload.title,
            "contentFormat": payload.format,
            "content": payload.content
        }

        if payload.tags is not None:
            data["tags"] = payload.tags.split(',')

        if payload.canonical_url is not None:
            data["canonicalUrl"] = payload.canonical_url

        if payload.publish_status is not None:
            data["publishStatus"] = payload.publish_status

        if payload.license is not None:
            data["license"] = payload.license

        if payload.notify_followers is not None:
            data["notifyFollowers"] = payload.notify_followers

        response = util.rest("POST", f"users/{user_id}/posts", access_token, data)
        return json.loads(response.text)