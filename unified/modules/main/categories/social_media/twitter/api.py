import json
from social_media.twitter import util
from flask import request
import requests


class TwitterApi():

    def user_by_screen_name(self, context, params):
        """ Get user data by screen name"""

        api = util.get_access_token(context["headers"])
        response = api.GetUser(screen_name=params.get("screen_name"))._json
        data = {
            "followers_count": response["followers_count"],
            "friends_count": response["friends_count"],
            "id": response["id"],
            "name": response["name"],
            "profile_background_image_url_https": response["profile_background_image_url_https"],
            "screen_name": response["screen_name"],
            "profile_image_url_https": response["profile_image_url_https"]
        }
        return data

    def user_by_id(self, context, params):
        """ Get user data by id"""
    
        api = util.get_access_token(context["headers"])
        response = api.GetUser(user_id=params.get("user_id"))._json
        data = {
            "followers_count": response["followers_count"],
            "friends_count": response["friends_count"],
            "id": response["id"],
            "name": response["name"],
            "profile_background_image_url_https": response["profile_background_image_url_https"],
            "screen_name": response["screen_name"],
            "profile_image_url_https": response["profile_image_url_https"]
        }
        return data

    def profile(self, context, params):
        """Get profile data"""

        api = util.get_access_token(context["headers"])
        response = api.VerifyCredentials(include_email=True)._json
        data ={
            "id": response["id"],
            "name": response["name"],
            "screen_name": response["screen_name"],
            "email": response["email"]
        }
        return data