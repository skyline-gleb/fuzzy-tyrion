
class Response(object):

	def __init__(self, method, url, status_code, status_msg):
		self.method      = method
		self.url         = url
		self.status_code = status_code
		self.status_msg  = status_msg