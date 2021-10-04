import json
import plivo 

def plivo_client(headers):
  client = plivo.RestClient(auth_id=headers["auth_id"], auth_token=headers["auth_token"])
  return client
