import json
import requests
from unified.core.actions import Actions
from website_builders.webflow.entities.webflow_item import WebflowItem
from website_builders.webflow import util

class WebflowActions(Actions):
    
    def create_item(self, context, payload):
        """
        creates a item 
        context holds the headers 
        payloads holds the request.body  
        """
        item_entity = WebflowItem(**payload)
        endpoint = f"collections/{item_entity.collection_id}/items"
        data = {
                "fields": {
                        "name": item_entity.name,
                        "_archived": item_entity.archived,
                        "_draft": item_entity.draft
                    }
                }
        if item_entity.slug:
            data["slug"]="exciting-post"
        response = util.rest("POST", endpoint, context["headers"]["access_token"], data)
        return json.loads(response.text)

    def create_live_item(self, context, payload):
        """
        creates a live item 
        context holds the headers 
        payloads holds the request.body  
        """
        item_entity = WebflowItem(**payload)
        endpoint = f"collections/{item_entity.collection_id}/items?live=true"
        data = {
                "fields": {
                        "name": item_entity.name,
                        "_archived": item_entity.archived,
                        "_draft": item_entity.draft
                    }
                }
        if item_entity.slug:
            data["slug"]="exciting-post"
        response = util.rest("POST", endpoint, context["headers"]["access_token"], data)
        return json.loads(response.text)

    def update_item(self, context, payload):
        """
        updates a item 
        context holds the headers 
        payloads holds the request.body  
        """
        item_entity = WebflowItem(**payload)
        endpoint = f"collections/{item_entity.collection_id}/items/{item_entity.item_id}"
        data = {
                "fields": {
                        "name": item_entity.name,
                        "_archived": item_entity.archived,
                        "_draft": item_entity.draft,
                        "slug": item_entity.slug
                    }
                }
        response = util.rest("PUT", endpoint, context["headers"]["access_token"], data)
        return json.loads(response.text)

    def update_live_item(self, context, payload):
        """
        updates a live item 
        context holds the headers 
        payloads holds the request.body  
        """
        item_entity = WebflowItem(**payload)
        endpoint = f"collections/{item_entity.collection_id}/items/{item_entity.item_id}?live=true"
        data = {
                "fields": {
                        "name": item_entity.name,
                        "_archived": item_entity.archived,
                        "_draft": item_entity.draft,
                        "slug": item_entity.slug
                    }
                }
        response = util.rest("PUT", endpoint, context["headers"]["access_token"], data)
        return json.loads(response.text)