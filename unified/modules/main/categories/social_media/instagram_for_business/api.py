from social_media.instagram_for_business import util
from social_media.instagram_for_business.entities.instagram_account import InstagramAccount
from social_media.entities.page import Page
from social_media.entities.profile import Profile
import json

from flask import request
import requests

class InstagramforbusinessApi:
    def pages(self, context, payload):
        '''Get list of pages '''

        access_token = context['headers'].get('access_token')
        url = 'v11.0/me/accounts?fields=name,id,access_token'
        pages_list = json.loads(
            util.rest('GET', url, access_token).text)['data']
        pages = []
        for page in pages_list:
            page_obj = Page(
                id=page['id'],
                name=page['name'],
                access_token=page['access_token']
            )
            pages.append(page_obj.__dict__)
        return json.dumps(pages)

    def instagram_accounts(self, context, payload):
        '''Get instagram account for a facebook page'''

        access_token = context['headers'].get('access_token')
        url = 'v11.0/page_id?fields=instagram_business_account{id,username,profile_picture_url}'.replace(
            'page_id', payload['page_id'])
        print(url)
        response = util.rest('GET', url, access_token)
        accounts = json.loads(response.text)
        account = InstagramAccount(
            account_id=accounts['instagram_business_account']['id'] if accounts.get(
                'instagram_business_account') else None,
            user_name=accounts['instagram_business_account']['username'] if accounts.get(
                'instagram_business_account') else None,
            page_id=accounts.get('id')
        )
        return account.__dict__, response.status_code
    
    def profile(self, context, payload):
        '''Get user details/profile details of authenticated user'''

        url = "me?fields=id,name,email"
        access_token = context['headers'].get('access_token')
        response = json.loads(util.rest('GET', url, access_token).text)
        profile = Profile(
            id=response['id'],
            name=response.get('name'),
            email=response.get('email')
        )
        
        return profile.__dict__
