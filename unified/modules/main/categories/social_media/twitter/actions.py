import json
from unified.core.actions import Actions
from social_media.twitter import util
from social_media.twitter.entites.twitter_userlist import TwitterUserList
from social_media.twitter.entites.twitter_tweet import TwitterTweet
from social_media.twitter.entites.twitter_profileimage import TwitterProfileImage
import requests
import base64
from requests_oauthlib import OAuth1


class TwitterAction(Actions):

    def add_user_to_list(self, context, payload):
        """ Add user to list"""

        api = util.get_access_token(context["headers"])
        payload = TwitterUserList(**payload)
        response = api.CreateListsMember(list_id=payload.list_id, screen_name=payload.username)
        return response._json

    def create_tweet(self, context, payload):
        """ Create a new tweet in twitter"""

        api = util.get_access_token(context["headers"])
        payload = TwitterTweet(**payload)

        if payload.video_url is not None:
            # return api.PostUpdate(payload.message, media=payload.video_url)._json   
            return {"message":"Video upload is not working"}    

        if payload.gif_url is not None:
            return api.PostUpdate(payload.message, media=payload.gif_url)._json

        if payload.image_url is not None:
            return api.PostUpdate(payload.message, media=payload.image_url)._json
        return api.PostUpdate(payload.message)._json

    def get_as_base64(self, url):
        return base64.b64encode(requests.get(url).content)

    def upload_profile_image(self, context, payload):
        """ Upload profile image
            Image size should not exceed 700KB. Here is the reference 
            https://snipboard.io/NzyRMm.jpg
        """

        payload = TwitterProfileImage(**payload)
        headers = context["headers"]
        auth_1 = OAuth1(headers['client_id'], headers['client_secret'],
                        headers['token'], headers['token_secret'])
        data = {"image": self.get_as_base64(payload.image_url)}
        response = requests.request(
            "POST", f"https://api.twitter.com/1.1/account/update_profile_image.json", auth=auth_1, data=data)
        return json.loads(response.text)
