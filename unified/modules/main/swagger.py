import os
import yaml
import json
import sys
import boto3
import inspect
from lib import s3utils
import requests
from main import application
s3 = s3utils.s3()
# path to categories and headers can be achieved here
categories_path = os.path.abspath(__file__)
categories_path = f"{categories_path[:categories_path.rfind('/swagger')]}/categories"
headers_path = os.path.abspath(__file__)
headers_path = f"{headers_path[:headers_path.rfind('/modules/main/swagger')]}/test"

document = """
swagger: "2.0"
info:
  description: "Applet.io provides simple interface to interact with hundreds of applications with no changes.  You can find out more about Applet.io at [https://applet.io](https://applet.io)."
  version: "1.0.0"
  title: "Applet Unified API"
  termsOfService: "https://applet.io/terms/"
  contact:
    email: "apiteam@unified.ly"
host: "applet2.dev.500apps.com"

tags:
- name: "Applet.io"
  description: "Everything about categories and apps supported by Applet.io"
  externalDocs:
    description: "Find out more"
    url: "https://applet.io"
schemes:
- "https"
- "http"

paths:
  /categories:
    get:
      tags:
      - "Applet.io"
      summary: "Get Categories"
      description: ""
      operationId: "getCat"
      produces:
      - "application/json"
      security:
      - Authorization: []
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              type: "string"
  /apps:
    get:
      tags:
      - "Applet.io"
      summary: "Get Supported Apps"
      description: ""
      operationId: "getApps"
      produces:
      - "application/json"
      security:
      - Authorization: []
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: '#/definitions/Apps'

  /categories/{name}:
    get:
      tags:
      - "Applet.io"
      summary: "Get Apps under a category"
      description: ""
      operationId: "getAppsUnderCategory"
      produces:
      - "application/json"
      security:
      - Authorization: []
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              $ref: '#/definitions/Apps'
      parameters:
      - in: path
        name: "name"
        required: true
        type: "string"
        description: Name of the category

  /categories/{name}/entities:
    get:
      tags:
      - "Applet.io"
      summary: "Get entities under a category"
      description: ""
      operationId: "getEntitiesUnderCategory"
      produces:
      - "application/json"
      security:
      - Authorization: []
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              type: "string"
      parameters:
      - in: path
        name: "name"
        required: true
        type: "string"
        description: Name of the category

  /categories/{name}/triggers:
    get:
      tags:
      - "Applet.io"
      summary: "Get triggers under a category"
      description: ""
      operationId: "getTriggersUnderCategory"
      produces:
      - "application/json"
      security:
      - Authorization: []
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              type: "string"
      parameters:
      - in: path
        name: "name"
        required: true
        type: "string"
        description: Name of the category

  /categories/{name}/actions:
    get:
      tags:
      - "Applet.io"
      summary: "Get actions under a category"
      description: ""
      operationId: "getActionsUnderCategory"
      produces:
      - "application/json"
      security:
      - Authorization: []
      responses:
        "200":
          description: "successful operation"
          schema:
            type: "array"
            items:
              type: "string"
      parameters:
      - in: path
        name: "name"
        required: true
        type: "string"
        description: Name of the category

securityDefinitions:
  Authorization:
    type: "apiKey"
    name: "Authorization"
    in: "header"

definitions:
  Apps:
    type: "object"
    properties:
      name:
        type: "string"
        description: "Name of the application"
      category:
        type: "string"
        description: "Category under which the application belongs"
      description:
        type: "string"
        description: "Description of the app"
      api:
        type: "string"
        description: "Comma Separated inputs for the app for user data"


externalDocs:
  description: "Signup for a free account"
  url: "https://applet.io"
"""

def get_parameters(userdata, action, payload,method_type):
    headers = []
    for key in userdata:
        headers.append({
            "in": "header",
            "type": "string",
            "name": key,
            "default": f"<{key}>",
            "required": True
        })
    request_test = payload.get("request_test", {})
    mappings = payload.get("mappings",{})
    path = payload.get("path",{})
    properties = {}
    if method_type == "actions":
      for key in request_test:  
        properties[key] = {
            "type": "string",
            "default": f"<{key}>",
        }
      request_test_parameters = {"in": "body", "name": "request_test", "schema": {
        "type": "object",  "properties": properties}}
    elif method_type == "triggers":
        mappings = mappings[0] if (type(mappings) == list) else mappings
        for key in mappings:
          properties[key] = {
              "type": "object",
              "default": f"<{key}>",
              
          }
        mapping_parameters = {"in": "body", "name": "mappings", "schema": {
          "type": "object",  "properties": properties}}

    elif method_type == "apis":
      for key in path:
        properties[key] = {"type":"string",
                           "default":f"<{key}>"
                           }
      path_parameters = {"in": "query", "type": "string","name":key,"required": False if key == '' else True,"default":f"<{key}>"}
    

    parameters = []
    if payload.get("request_test", None):
        parameters = [request_test_parameters]
    elif payload.get("mappings", None):
        parameters = [mapping_parameters]
    elif payload.get("path",None):
        parameters = [path_parameters]

    parameters = parameters + headers

    return parameters

def get_path(action, method, parameters, payload, app):

    action = action.lower().replace(" ", "-")
    '''
     /apps:
    get:
      description: ''
      operationId: getApps
      produces:
      - application/json
      responses:
        '200':
          description: successful operation
          schema:
            items:
              $ref: '#/definitions/Apps'
            type: array
      summary: Get Supported Apps
      tags:
      - unified.ly
      '''
    category = payload.get("category", "")
    entity = payload.get("entity", "")
    schema = '{category}{entity}'.format(category=category, entity=entity)
    schema = ''.join(filter(str.isalnum, schema))

    return {
        method: {
            "produces": ["application/json"],
            "security": [{"Authorization": []}],
            "tags": [app],
            "parameters": parameters,
            "responses": {
                "200": {
                    "description": "successful",
                },
                "400":{
                    "description": "unsuccessful",
                }
            }
        }
    }

def get_schema(swagger_category):
    categories = os.listdir(categories_path)
    apps_list = {}
    app_specific_list = []

    for category in categories:
        for app in (os.listdir(f"{categories_path}/{category}")):
            app_specific_list.append(app)
        if "entities" in app_specific_list:
            app_specific_list.remove("entities")
        if "__pycache__" in app_specific_list:
            app_specific_list.remove("__pycache__")
        if "util.py" in app_specific_list:
            app_specific_list.remove("util.py")

    # listing all categories
    for category in categories:
        apps_list[category] = os.listdir(f"{categories_path}/{category}")


    # preparing apps_json
    apps_json = []
    for category in categories:
      for apps in apps_list[category]:
        try:
          header_json = json.load(open(f"{headers_path}/{category}/{apps}/headers.json"))
          app_description = open(f"{categories_path}/{category}/{apps}/app.py")
          apps_dict={}
          apps_dict["api"] = ','.join(header_json.keys())
          apps_dict["category"] = category
          apps_dict["name"] = apps
          for description in app_description:
            if "description" in description:
              description = description.split("=")[1].replace('"',"")
              apps_dict["description"] = description.replace(",\n","")
          apps_json.append(apps_dict)
        except FileNotFoundError:
          x = "not found"
        except IsADirectoryError:
          x = "notfound"
    
    
    category_actions = {}
    category_triggers = {}
    category_api = {}
    for category in apps_list:
      for app in apps_list[category]:
        try:
          if app != "entities" and app != "__pycache__" and app != "util.py":
            category_actions[app] = []
            for action in os.listdir(f"{headers_path}/{category}/{app}/actions"):
              if action in dir(application.get_app_class(app)):
                category_actions[app].append(action)
        except FileNotFoundError:
          x = "keyerror"

    for category in apps_list:
      for app in apps_list[category]:
        try:
          if app != "entities" and app != "__pycache__" and app != "util.py":
            category_triggers[app] = []
            for trigger in os.listdir(f"{headers_path}/{category}/{app}/triggers"):
              if trigger in dir(application.get_app_class(app)):
                  category_triggers[app].append(trigger)
        except FileNotFoundError:
          x = "keyerror"

    for category in apps_list:
      for app in apps_list[category]:
        try:
          if app != "entities" and app != "__pycache__" and app != "util.py":
            category_api[app] = []
            for api in os.listdir(f"{headers_path}/{category}/{app}/apis"):
              if api in dir(application.get_app_class(app)):
                  category_api[app].append(api)
        except FileNotFoundError:
          x = "keyerror"
    data = {}
    if swagger_category == None:
      data["categories"] = categories
      data["apps"] = apps_json
    else:
      data["categories"] = [swagger_category]
      data["apps"] =[app for app in apps_json if app["category"] == swagger_category]

    
    data["triggers"] = {}
    data["actions"] = {}
    data["api"] = {}
    data["app_individual"] = {}

    
    for app in data["apps"]:
      name = app.get("name",None)
      category = app.get("category",None)
      data["app_individual"][name] = {}

      try:
        data["actions"][name]= category_actions[name]
        data["api"][name] = category_api[name]
        data["triggers"][name] = category_triggers[name]
      except KeyError:
        x = "keyerror"
      userdata = json.load(open(f"{headers_path}/{category}/{name}/headers.json"))
      data["app_individual"][name]["userdata"] = {}
      data["app_individual"][name]["actions"] = {}
      data["app_individual"][name]["api"] = {}
      data["app_individual"][name]["triggers"] = {}

      if userdata is not None:
            userdata = {k.replace('_', '-'): v for k, v in userdata.items()}
            data["app_individual"][name]['userdata'] = userdata
      try:
        for action in data["actions"][name]:
          try:
            if action in os.listdir(f"{headers_path}/{category}/{name}/actions"):
              data["app_individual"][name]["actions"][action.lower()] = {"request_test": json.load(open(f"{headers_path}/{category}/{name}/actions/{action}/1.json")), "category": category}
          except FileNotFoundError:
            x = "keyerror"
        for api in data["api"][name]:
          try:
            if api in os.listdir(f"{headers_path}/{category}/{name}/apis"):
              data["app_individual"][name]["api"][api.lower()] = {"path": json.load(open(f"{headers_path}/{category}/{name}/apis/{api}/1.json")), "category": category}
          except FileNotFoundError:
            x = "keyerror"
        for trigger in data["triggers"][name]:
          try:
            if trigger in os.listdir(f"{headers_path}/{category}/{name}/triggers"):
              data["app_individual"][name]["triggers"][trigger.lower()] = {"mappings": json.load(open(f"{headers_path}/{category}/{name}/triggers/{trigger}/1.json")), "category": category}
          except FileNotFoundError:
            x = "keyerror" 
      except KeyError:
        x = "keyerror"
    app_details = open("app_details.json","w") 
    app_details.write(json.dumps({"app_individual":data["app_individual"]}))
    return data

def get_swagger(swagger_category):

  data = get_schema(swagger_category)
  swagger = yaml.load(document, Loader=yaml.FullLoader)
  for category in data["categories"]:
        swagger.get('tags').append({"name": category.title(), "description": "Category {category}".format(category=category.title())})
        
  for app in data["apps"]:
          name = app.get("name", None)
          if name is None:
              continue
          category = app.get("category", "No Category")
          swagger.get('tags').append({
              "name": name,
              "description": f"{name.title()} in Category {category.title()}"
          })
        
  for app in data["app_individual"]:
          userdata = data["app_individual"][app].get('userdata', None)
          if userdata is None:
              continue

          actions = data["app_individual"][app].get('actions')
          if actions:
              paths = {}
              for action in actions:
                  payload = actions[action]
                  parameters = get_parameters(
                      userdata, action, payload,"actions")
                  path = "/{app}/{action}".format(app=app.lower().replace(
                      " ", "-"), action=action.lower().replace(" ", "-"))
                  swagger.get('paths')[path] = get_path(
                      action, "post", parameters, payload, app)

          # API calls
          apis = data["app_individual"][app].get('api')
          if apis:
              paths = {}
              for api in apis:
                  payload = apis[api]
                  parameters = get_parameters(
                      userdata, api, payload,"apis")
                  path = "/{app}/{api}".format(app=app.lower().replace(
                      " ", "-"), api=api.lower().replace(" ", "-"))
                  swagger.get('paths')[path] = get_path(
                      api, "get", parameters, payload, app)

          triggers = data["app_individual"][app].get('triggers')
          if triggers:
              for trigger in triggers:
                  payload = triggers[trigger]
                  parameters = get_parameters(
                      userdata, trigger, payload,"triggers")
                  path = "/{app}/{trigger}".format(app=app.lower().replace(
                      " ", "-"), trigger=trigger.lower().replace(" ", "-"))
                  swagger.get('paths')[path] = get_path(
                      trigger, "post", parameters, payload, app)
  yaml_data = yaml.dump(swagger)
  return yaml_data, data

def generate_swagger(swagger_category):
  
  data = {}
  data["categories"] = os.listdir(categories_path)
  if swagger_category == None:
    yaml_data, json_data = get_swagger(swagger_category)
    result = {}
    result["yaml"] = yaml_data
    result["json"] = yaml.load(yaml_data)
    s3.write_s3(f"unified2/swagger.yml", result)
    s3.write_s3(f"unified2/swagger.json", json.dumps(json_data))
    
  elif swagger_category == "all":
    for category in data["categories"]:
      yaml_data, json_data = get_swagger(category)
      result = {}
      result["yaml"] = yaml_data
      result["json"] = yaml.load(yaml_data)
      category = category.replace('_','')
      s3.write_s3(f"unified2/swagger-{category}.yml", result)
      s3.write_s3(f"unified2/swagger-{category}.json", json.dumps(json_data))

  else:
    yaml_data, json_data = get_swagger(swagger_category)
    result = {}
    result["yaml"] = yaml_data
    result["json"] = yaml.load(yaml_data)
    swagger_category = swagger_category.replace('_','')
    s3.write_s3(f"unified2/swagger-{swagger_category}.yml", result)
    s3.write_s3(f"unified2/swagger-{swagger_category}.json", json.dumps(json_data))
   
  return "ok"


def swagger_doc(category=None):
        
    if category is None:
      swagger_yml = s3.get_s3(f"swagger/swagger.yml")
    else:
      category = category.lower().replace('&','').replace('_','').replace(' ','')
      swagger_yml = s3.get_s3(f"unified2/swagger-{category}.yml")
    return swagger_yml.get("yaml")

if __name__ == '__main__':
    is_local = True
    boto3.setup_default_session(
        profile_name='500app-sites', region_name="us-east-1")
    yaml_data, json_data = get_swagger()
    with open("output/swagger.yml", "w") as file1:
        file1.write(yaml_data)