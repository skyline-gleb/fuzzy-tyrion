import json

class Config(object):

	collection = {}

	@staticmethod
	def load(filename):
		with open(filename, 'r') as config_file:
			Config.collection = json.loads(config_file.read())
	
	@staticmethod
	def get(key):
		return Config.collection[key]

	@staticmethod
	def set(key, value):
		Config.collection[key] = value