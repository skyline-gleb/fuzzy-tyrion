import os
from ctypes import *
from random import randint

lib = cdll.LoadLibrary('./example.so')
class DataGenerator:
	def __init__(self):
		lib.return_string.restype = c_char_p
		lib.return_string.argtypes = [c_char_p]
		lib.generate_int32 = c_int
	def getString(self, lenght = 10):
		name = create_string_buffer("TIMMAH!")
		return lib.return_string(name)
	def getInteger32(self, minInt = 0, maxInt = 1000):
		return randint(minInt, maxInt)

