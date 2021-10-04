# -*- coding:utf-8 -*-
from . import module
from flask import jsonify
import psutil
import platform
from datetime import datetime
import socket
from unified import MODULES
from lib import logger

def get_system_info():

	datetime_format = '%d-%B-%Y %H:%M:%S (UTC)'

	raw_boot_time = psutil.boot_time()

	boot_time = datetime.utcfromtimestamp(raw_boot_time)
	boot_time = boot_time.strftime(datetime_format)
	hostname = platform.node()

	os_name = '{} {}'.format(platform.system(), platform.release()).strip()
	if 'Linux' in os_name:
	    import distro
	    os_name = ' '.join(distro.linux_distribution()).strip()

	architecture = platform.machine()

	python_version = '{} ver. {}'.format(
	    platform.python_implementation(), platform.python_version()
	)
	data = {}
	data['SERVER_START_TIME'] = boot_time
	data['BUILD_TIME'] = '{BUILD_TIME}'
	data['BUILD_NUMBER'] = '{BUILD_NUMBER}'
	data['HOSTNAME'] = hostname
	data['OS_NAME'] = os_name
	data['ARCHITECTURE'] = architecture
	data['PYTHON_VERSION'] = python_version
	data['PRIVATE_IP'] = socket.gethostbyname(hostname)
	data['MODULES'] = MODULES
	data['MODULES'] = MODULES
	return data


@module.route("/_version", methods=['GET'])
def ping():
    return jsonify(get_system_info())