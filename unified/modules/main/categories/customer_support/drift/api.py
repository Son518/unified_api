import json
from customer_support.drift.entities.drift_anonymous_user_id import DriftAnonymousUserId
from customer_support.drift import util
from requests.models import Response

class DriftApi():

    def anonymous_user_id(self,context,params):
        """gets contact by anonymous_user_id"""
        response = json.loads(util.rest("GET","anonymous_user_id",{},context["headers"]["access_token"],params["user_id"]))
        response=response['data']
        data = DriftAnonymousUserId(
                                    email=response['email'],
                                    name=response['name'],
                                    bot=response['bot'],
                                    alias=response['alias'],
                                    availability=response['availability'],
                                    orgId=response['orgId'],
                                    role=response['role'], 
                                    createdAt=response['createdAt']
                                )
        return data.__dict__

    def profile(self, context, params):
        '''Details of authenticated user'''

        response = util.rest("GET","list",{},context["headers"]["access_token"])
        users = response.get("data")
        for user in users:
            if user.get('role')=="org_admin":
                profile = {
                    'id':user.get('id'),
                    'email':user.get('email'),
                    'name':user.get('name')
                }
                return profile
        return {"error":"provide proper details"}