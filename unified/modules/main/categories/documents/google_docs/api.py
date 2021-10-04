from documents.google_docs import util
from unified.core.util import google_profile
from documents.google_docs.entities.google_docs_document import GoogledocsDocument
import json


class GoogledocsApi:
    def document_by_name(self, context, params):
        access_token = util.get_access_token(context["headers"])
        url = f"https://www.googleapis.com/drive/v2/files?q=title='{params['name']}' and mimeType='application/vnd.google-apps.document'"
        document_list = json.loads(util.rest("GET", url, access_token).text)['items']
        documents=[]
        for document in document_list:
            file_obj = GoogledocsDocument(
                document_id=document['id'],
                name=document.get('title'),
                media_mime_type=document.get('mimeType'),
                permission=document['userPermission'].get('id'),
                document_size=document.get('fileSize')
            )
            documents.append(file_obj.__dict__)
        
        return json.dumps(documents)
        
    def profile(self, context, params):
        '''Details of authenticated user'''

        return google_profile(context, params)
