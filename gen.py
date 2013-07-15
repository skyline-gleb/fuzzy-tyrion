import os
from ctypes import *

class DataGenerator:
	def __init__(self):
		lib = cdll.LoadLibrary('./libBackEnd.so')
		lib.generateString.restype = c_char_p
		lib.generateString.argtypes = [c_int]
		lib.generateInt32.restype = c_int
		lib.generateInt32.argtypes = [c_int, c_int]
	def getString(self, length = 10):
		return lib.generateString(length)
	def getInteger32(self, minInt = 0, maxInt = 1000):
		return lib.generateInt32(minInt, maxInt)

