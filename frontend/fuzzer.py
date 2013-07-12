import re
import time
from request import *
from log import *
from itertools import chain
from datagenerator import *

class Fuzzer(object):

	def __init__(self, api_url, rps = 10, headers = {}, parameters = {}):
		self.api_url    = api_url
		self.rps        = rps
		self.headers    = headers
		self.parameters = parameters

	def test_methods(self, methods):
		for api_method, options in methods.items():
			for index in range(options['count']):
				self.test_method(api_method, options['http_method'],
								 self.prepare_data(options['parameters']))
			time.sleep(1.0 / self.rps)

	def test_method(self, api_method, http_method, data):
		payload = dict(chain(self.parameters.items(), data.items()))
		url = re.sub(r'{(.+?)}',
					 lambda m: str(payload[m.group(1)]) if m.group(1) in payload else m.group(0),
					 self.api_url + api_method)
		request = Request(http_method, url, payload, self.headers)
		response = request.send()
		msg = response.request['method'] + ' ' + response.request['url'] + '\n'
		msg += str(response.status_code) + ' ' + response.status_msg + '\n'
		Log.write(msg)

	def prepare_data(self, parameters):
		data = {}
		for parameter, options in parameters.items():
			value = options['value']
			if options['action'] == 'generate':
				if options['data_type'] == 'int':
					value = DataGenerator.random_int()
				else:
					DataGenerator.random_string()
			data[parameter] = value
		return data