import json
from project_management.podio import util
from project_management.podio.entities.podio_item import PodioItem
from project_management.podio.entities.podio_user import PodioUser



class PodioApi():

    def users(self, context, params):
        ''' returns users data'''
        
        podio_item = util.podio_oauth(context["headers"])
        user = podio_item.User.current()
        user_obj = PodioUser(id=user["user_id"],
                            email=user["mail"],
                            created_on=user["created_on"])
        return user_obj.__dict__

    def item(self,context,params):
        ''' returns items data'''
        
        podio_item = util.podio_oauth(context["headers"])
        item_response = podio_item.Item.find(int(params["item_id"]))
        item = PodioItem(app_name=item_response["app"]["item_name"],
                      application_id=item_response["app"]["app_id"],
                      item_id=item_response["item_id"],
                      workspace_id=item_response["app"]["space_id"],
                      organization_id=item_response["app"]["item_accounting_info"]["org_id"],
                      link=item_response["link"],
                      url=item_response["app"]["url"],
                      tag=item_response["tags"],
                      description=item_response["fields"][0]["config"]["description"],
                      title=item_response["fields"][0]["label"],
                      priority=item_response["priority"])
        return item.__dict__

    def profile(self,context,params):
        """
        get call to show user authenticated information
        """
        podio_item = util.podio_oauth(context["headers"])
        user = podio_item.User.current()
        profile = {
            'id':user['user_id'],
            'email':user['email']
        }
        return user