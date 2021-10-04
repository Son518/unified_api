import json
from social_media.facebook_pages import util
from flask import request
import requests
from social_media.facebook_pages.entites.facebookpage_page import Facebookpages_page

class FacebookpageAPI:

    def profile(self, context, params):
        """ Get profile data"""
        
        access_token = context['headers'].get('access_token')
        url = 'me?fields=accounts,id,name'
        page_list = json.loads(util.rest('GET', url, access_token).text)
        pages_list = page_list["accounts"]["data"]
        page_data = []

        if len(pages_list) != 0:            
            for page in pages_list:
                page_obj = {}
                page_obj["id"] = page["id"]
                page_obj["name"] = page["name"]
                page_data.append(page_obj)

        data = Facebookpages_page(
            id= page_list.get("id"),
            name= page_list.get("name"),
            page_data= page_data
        )
        return data.__dict__