from config import *

class App(object):

	config = {'version': '0.1'}

	args = {}

	@staticmethod
	def init():
		# TODO: parse arguments
		App.args = {'config': '../config.json', 'report': 'report.xml'}

		Config.load(App.args['config'])