# -*- coding:utf-8 -*-
import os
import sys
import traceback
from flask import Flask, jsonify
from flask_cors import CORS
from flask_log_request_id import RequestID

# pip install flask_apiexceptions
from flask_apiexceptions import (
    JSONExceptionHandler, ApiException, ApiError, api_exception_handler)


# A list of app modules and their prefixes. Each APP entry must contain a
# 'name', the remaining arguments are optional.
MODULES = [
    {'name': 'health-check', 'url_prefix': '/_unified2'},
    {'name': 'main', 'url_prefix': '/'},
]

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Create the Skeleton app
def create_app(name=__name__):
    app = Flask(__name__, static_folder='static')
    RequestID(app)
    load_config(app)
    register_local_modules(app)

    app.wsgi_app = ProxyFixupHelper(app.wsgi_app)

    ext = JSONExceptionHandler(app)
    ext.register(code_or_exception=ApiException, handler=api_exception_handler)

    # Cors
    CORS(app, supports_credentials=True)

    return app


def load_config(app):
    app.config.from_object(__name__)
    app.config.from_object('unified.default_settings')


def register_local_modules(app):
    cur = os.path.abspath(__file__)
    sys.path.append(os.path.dirname(cur))
    sys.path.append(os.path.dirname(cur) + '/modules')
    sys.path.append(os.path.dirname(cur) + '/modules/main/categories')
    
    for m in MODULES:
        module_name = '%s.application' % m['name']
        try:
            application = __import__(module_name, globals(), locals(), [], 0)
        except ImportError as err:
            # raise ImportError
            # exit()
            print(module_name, err)
        else:
            url_prefix = None
            if 'url_prefix' in m:
                url_prefix = m['url_prefix']

            if app.config['DEBUG']:
                print('[UNIFIED] registering modules in %s to prefix: %s' %
                      (module_name, url_prefix))
            if url_prefix == '/':
                url_prefix = None
            # This is being done at the app level now
            # CORS(application.module)
            app.register_blueprint(application.module, url_prefix=url_prefix)


# Seeing 127.0.0.1 is almost never correct, promise.  We're proxied 99.9% of
# the time behind a load balancer or proxying webserver. Pull the right IP
# address from the correct HTTP header. In my hosting environments, I inject
# X-Real-IP as the HTTP header of choice instead of appending to
# X-Forwarded-For. Mixing and matching HTTP headers used by a client's proxy
# infrastructure and the server's infrastructure is almost always a bad idea.
class ProxyFixupHelper(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Only perform this fixup if the current remote host is localhost.
        if environ['REMOTE_ADDR'] == '127.0.0.1':
            host = environ.get('HTTP_X_REAL_IP', False)
            if host:
                environ['REMOTE_ADDR'] = host
        return self.app(environ, start_response)


# create flask instance
unified = create_app()

@unified.errorhandler(Exception)
def all_exception_handler(error):
    traceback.print_exc()
    return jsonify({'error': 'Error {error}'.format(error=str(error))}), 400
