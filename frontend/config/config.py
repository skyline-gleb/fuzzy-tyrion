import json
from .configvalidator import *


class Config(object):
    @staticmethod
    def load(filename):
        with open(filename, 'r') as config_file:
            data = json.loads(config_file.read())

        obj = Check(data)
        obj.Run()

        for item in data:
            setattr(Config, item, data[item])
