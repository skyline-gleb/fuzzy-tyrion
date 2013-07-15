import json
from configvalidator import *


class Config(object):

<<<<<<< HEAD
	@staticmethod
	def load(filename):
		with open(filename, 'r') as config_file:
			data = json.loads(config_file.read())
		obj = Check(data)
		if obj.Run() == -1:
			print("Error")
		for item in data:
			setattr(Config, item, data[item])
=======
    @staticmethod
    def load(filename):
        with open(filename, 'r') as config_file:
            data = json.loads(config_file.read())
        for item in data:
            setattr(Config, item, data[item])
>>>>>>> f25ea69f27d32c15416f3b024fea1528713921dc
