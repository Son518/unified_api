from notes.onenote import util
from unified.core.actions import Actions
from notes.onenote.entities.onenote_image import OnenoteImage
from notes.onenote.entities.onenote_section import OnenoteSection
from notes.onenote.entities.onenote_note import OnenoteNote
from notes.onenote.entities.onenote_url import OnenoteUrl
import json
import requests
import base64

class OnenoteActions(Actions):

    def create_note(self, context, payload):
        '''adding data to note'''

        access_token = util.get_access_token(context["headers"])
        note_entity = OnenoteNote(**payload)
        endpoint="pages"
        data=f"<!DOCTYPE html><html><head><title>{note_entity.title}</title><meta name=\"created\" content= {note_entity.content} /></head><body><p> {note_entity.body}</p></body></html>"
        response = util.rest("POST", endpoint, access_token, data)
        return json.loads(response.text)

    def create_note_in_section(self, context, payload):
        '''creates a note in section'''

        access_token = util.get_access_token(context["headers"])
        section_entity = OnenoteSection(**payload)
        endpoint=f"sections/{section_entity.section_id}/pages"
        data=f"<!DOCTYPE html><html><head><title>{section_entity.title}</title><meta name=\"created\" content= {section_entity.content} /></head><body><p>{section_entity.body} </p></body></html>"
        response = util.rest("POST", endpoint, access_token, data)
        return json.loads(response.text)

    def create_image(self, context, payload):
        '''creates a note in section'''

        access_token = util.get_access_token(context['headers'])
        image_entity = OnenoteImage(**payload)
        endpoint="pages"
        url=self.get_as_base64(image_entity.image_url)
        data=f"<!DOCTYPE html><html><head><title>{image_entity.title}</title><meta name=\"created\"/></head><body><img src={url} alt='image page' height='1000' width='1000'/></p></body></html>"
        response = util.rest("POST",endpoint,access_token,data)
        return json.loads(response.text)

    def get_as_base64(self, url):
        return base64.b64encode(requests.get(url).content).decode("utf-8")
        
    def note_from_url_link(self, context, payload):
        '''creates a note in section'''

        access_token = util.get_access_token(context['headers'])
        url_entity = OnenoteUrl(**payload)
        endpoint=f"pages"
        data=f"<!DOCTYPE html><html><head><title>{url_entity.title}</title><meta name=\"created\"/></head><body><p>{url_entity.url_link}</p></body></html>"
        response = util.rest("POST", endpoint, access_token, data)
        return json.loads(response.text) 