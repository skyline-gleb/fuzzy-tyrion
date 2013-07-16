import json
from .configvalidator import *


class Config(object):
    @staticmethod
    def load(filename):
        with open(filename, 'r') as config_file:
            data = json.loads(config_file.read())

        obj = Check(data)
        try:
            obj.Run()
        except Exception:
            value = -1
        
        if value == -1:
            print("Error")

        for item in data:
            setattr(Config, item, data[item])
