import re
import requests
from log.log import *
from statuscode import *
from itertools import chain

class Fuzzer(object):

	def __init__(self, api_url, rps = 10, headers = {}, parameters = {}):
		self.api_url = api_url
		self.rps = rps
		self.headers = headers
		self.parameters = parameters

	def test(self, http_method, api_method, data = {}):

		payload = dict(chain(self.parameters.items(), data.items()))

		url = re.sub(r'{(.+?)}',
					 lambda m: str(payload[m.group(1)]) if m.group(1) in payload else m.group(0),
					 self.api_url + api_method)

		r = requests.request(http_method, url, data = payload, headers = self.headers)
		Log.write(http_method + ' ' + r.request.url + '?' + r.request.body)
		Log.write(str(r.status_code) + ' ' + StatusCode.getMsg(r.status_code) + '\n')