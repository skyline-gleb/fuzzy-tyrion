
class Log(object):

	@staticmethod
	def write(response):
		print(response.method + ' ' + response.url + ' ' + str(response.status_code))