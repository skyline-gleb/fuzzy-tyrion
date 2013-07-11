#!/usr/bin/env python

from core.app import *
from core.config import *
from request.fuzzer import *
from datagenerator.datagenerator import *
from time import sleep

def main():
	App.init()

	fuzzer = Fuzzer(Config.get('api_url'), Config.get('rps'),
					Config.get('headers'), Config.get('parameters'))
	
	data = {}

	# BackEnd emulation
	for api_method, options in Config.get('methods').items():
		data[api_method] = []
		for index in range(options['count']):
			parameters = {}
			for parameter, d in options['parameters'].items():
				if d['action'] == 'generate':
					if d['data_type'] == 'integer':
						parameters[parameter] = DataGenerator.generate_integer()
					elif d['data_type'] == 'float':
						parameters[parameter] = DataGenerator.generate_float()
					else:
						parameters[parameter] = DataGenerator.generate_string()
				else:
					parameters[parameter] = d['value']
			data[api_method].append(parameters)


	for api_method, parameters in data.items():
		http_method = Config.get('methods')[api_method]['http_method']
		count = Config.get('methods')[api_method]['count']
		for index in range(count):
			fuzzer.test(http_method, api_method, parameters[index])
			sleep(1.0 / Config.get('rps'))

if __name__ == '__main__':
	main();