from unified.core.actions import Actions
from social_media.facebook_pages.entites.facebookpage_page import Facebookpages_page
from social_media.facebook_pages import util
import json


class FacebookpagesAction(Actions):

    def create_page_post(self, context, payload):
        """ Create a page post"""

        page_data = Facebookpages_page(**payload)
        access_token = context['headers'].get('access_token')
        url = f'me/feed?access_token={access_token}'
        data = {
            "message": page_data.message
        }

        if page_data.link_url is not None:
            data["link"] = page_data.link_url

        response = json.loads(util.rest('POST', url, access_token, data).text)
        return response

    def create_page_post(self, context, payload):
        """ Create a page post"""

        page_data = Facebookpages_page(**payload)
        access_token = context['headers'].get('access_token')
        url = f'me/feed?access_token={access_token}'
        data = {
            "message": page_data.message
        }

        if page_data.link_url is not None:
            data["link"] = page_data.link_url

        response = json.loads(util.rest('POST', url, access_token, data).text)
        return response

    def create_page_photo(self, context, payload):
        """ Create a page image post"""

        page_data = Facebookpages_page(**payload)
        access_token = context['headers'].get('access_token')
        url = f'me/photos?access_token={access_token}'
        data = {
            "url": page_data.photo_url
        }

        if page_data.description is not None:
            data["message"] = page_data.description

        response = json.loads(util.rest('POST', url, access_token, data).text)
        return response

    def create_page_video(self, context, payload):
        """ Create a page video post"""

        page_data = Facebookpages_page(**payload)
        access_token = context['headers'].get('access_token')
        url = f'me/videos'
        data = {
            "file_url": page_data.video_url,
            "access_token": access_token
        }

        if page_data.description is not None:
            data["description"] = page_data.description

        if page_data.title is not None:
            data["title"] = page_data.title

        response = json.loads(util.rest('POST', url, access_token, data).text)
        return response

    def change_page_profile_photo(self, context, payload):
        """ Change a page profile photo"""

        page_data = Facebookpages_page(**payload)
        access_token = context['headers'].get('access_token')
        url = f'{page_data.page_id}/picture?access_token={access_token}'
        data = {
            "picture": page_data.photo_url
        }
        json.loads(util.rest('POST', url, access_token, data).text)
        return {"message":"Profile photo updated"}