import os
from ctypes import *


class DataGenerator:
    def __init__(self):
        self.lib = cdll.LoadLibrary('backend/libBackEnd.so')
        self.lib.generateString.restype = c_char_p
        self.lib.generateString.argtypes = [c_int]
        self.lib.generateInt32.restype = c_int
        self.lib.generateInt32.argtypes = [c_int, c_int]
    def getString(self, length = 10):
        return self.lib.generateString(length)
    def getInteger32(self, minInt = 0, maxInt = 1000):
        return self.lib.generateInt32(minInt, maxInt)
