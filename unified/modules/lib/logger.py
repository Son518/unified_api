import json

import logging
from pythonjsonlogger import jsonlogger

from flask import request
from unified.default_settings import APP_NAME

class ulogger(object):
	"""custom logger (json)"""
	def __init__(self, app_name=None, domain_id=None, user_id=APP_NAME, log_level="DEBUG"):
		super(ulogger, self).__init__()
		self.log_level=log_level
		self.app_name = app_name
		self.domain_id = domain_id
		self.user_id = user_id

	def log(self, level, message, log_type, sub_type=None):
		logger = logging.getLogger()
		logger.setLevel(self.log_level)
		json_handler = logging.StreamHandler()
		formatter = jsonlogger.JsonFormatter(
			fmt='%(threadName)s \
				%(name)s \
				%(thread)s \
				%(created)s \
				%(process)s \
				%(processName)s \
				%(relativeCreated)s \
				%(module)s \
				%(funcName)s \
				%(levelno)s \
				%(msecs)s \
				%(pathname)s \
				%(lineno)s \
				%(asctime)s \
				%(message)s \
				%(filename)s \
				%(levelname)s \
				%(special)s \
				%(run)s'
		)
		json_handler.setFormatter(formatter)
		logger.addHandler(json_handler)
		logger.removeHandler(logger.handlers[0])

		log = {}
		log['app_name'] = self.app_name
		log['domain_id'] = self.domain_id
		log['user_id'] = self.user_id

		log['url'] = request.url
		log['method'] = request.method
		log['remote_addr'] = request.remote_addr

		log['level'] = level
		log['message'] = message
		log['log_type'] = log_type
		log['sub_type'] = sub_type

		logger.info(log)