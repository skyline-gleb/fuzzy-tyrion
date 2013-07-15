import os
from ctypes import *
#Исправить биндинг таким образом, чтобы была возможность создать несколько генераторов.
class DataGenerator:
	def __init__(self):
		lib = cdll.LoadLibrary('./libBackEnd.so')
		lib.generate_string.restype = c_char_p
		lib.generate_string.argtypes = [c_int]
		lib.generate_int32.restype = c_int
		lib.generate_int32.argtypes = [c_int, c_int]
	def getString(self, length = 10):
		return lib.generate_string(length)
	def getInteger32(self, minInt = 0, maxInt = 1000):
		return lib.generate_int32(minInt, maxInt)

