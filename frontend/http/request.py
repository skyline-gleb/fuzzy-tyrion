import requests
from response import *

class Request(object):

	def __init__(self, method, url, fields = {}, headers = {}, timeout = 10):
		self.method      = method.upper()
		self.url         = url
		self.headers     = headers
		self.timeout     = timeout

		if method in ['POST', 'PUT', 'PATCH', 'TRACE']:
			self.data = fields
			self.params = {}
		else:
			self.data = {}
			self.params = fields

	def send(self):
		response = requests.request(self.method, self.url, headers = self.headers,
							 		params = self.params, data = self.data, timeout = self.timeout)
		return Response(self.method, self.url, response.status_code, response.reason)