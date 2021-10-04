import json
import sys
from urllib import parse
from flask import request
from lib import helper
import cachetools.func
from unified.default_settings import S3_BUCKET

folder = "/Downloads"
is_local = False

class s3(object):
    """docstring for s3"""

    def __init__(self):
        super(s3, self).__init__()
        cnx = helper.utils()
        self.aws = cnx.aws().client('s3')
        self.aws_res = cnx.aws().resource('s3')

    def get_body(self):
        # Read Variables
        data = request.json

        # If Post is not  found, go to get
        if (data is None):
            print("Getting get")
            data = request.query_string.decode()

        try:
            data = json.loads(data)
        except Exception as err:
            e = sys.exc_info()[0]
            print('Ignore', e)

        # # If it is not query string or raw body, we will see if it is url encoded
        if isinstance(data, str):
            print("Getting xformencoded ")
            data = dict(parse.parse_qsl(data))

        return data

    def get_s3(self, key, default={}):
        try:
            if is_local:
                file = '{folder}{key}'.format(key=key.lower(), folder=folder)
                print('opening', file)
                with open(file, 'r') as file:
                    data = json.loads(file.read())
                    return data
            else:
                print("opening native", key)
                # making a copy of data returned, to escape cache
                result = json.loads(json.dumps(self.get_core_s3(key)))
                return result

        except Exception as err:
            print(err)
            return default

    # @cachetools.func.ttl_cache(maxsize=128, ttl=10 * 60)
    # TODO Uncomment the above line while moving to uat / production
    # Caching is causing delay in developmen phase.
    def get_core_s3(self, key):
        client = self.aws
        obj = client.get_object(Bucket=S3_BUCKET, Key=key.lower())
        return json.loads(obj['Body'].read())

    def get_files_in_folder(self, prefix):
        client = self.aws
        response = client.list_objects(Bucket=S3_BUCKET, Prefix=prefix)
        for content in response.get('Contents', []):
            yield content.get('Key')

    def write_s3(self, key, body):
        client = self.aws
        return client.put_object(Bucket=S3_BUCKET, Key=key, Body=json.dumps(body))

    def delete_app(self, appName):
        if not appName:
            raise NameError('App Empty')

        bucket = self.aws_res.Bucket(S3_BUCKET)
        prefix = "apps/" + appName
        print("prefix ", prefix)
        bucket.objects.filter(Prefix=prefix).delete()
        # read apps
        apps = self.get_s3("sys/apps.json")
        new_json = [app for app in apps if app.get("name", None) != appName]
        print(new_json)
        self.write_s3("sys/apps.json", new_json)

        # Read apps
        return "Deleted Successfully"
