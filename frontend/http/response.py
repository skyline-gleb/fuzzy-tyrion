
class Response(object):

	def __init__(self, error_msg = None, request = None, status_code = None,
				 status_msg = None, encoding = None, time = None, content = None):
		self.request     = request
		self.error_msg   = error_msg
		self.status_code = status_code
		self.status_msg  = status_msg
		self.encoding    = encoding
		self.time        = time
		self.content     = content