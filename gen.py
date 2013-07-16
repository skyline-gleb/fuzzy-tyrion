#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from ctypes import *
#Исправить биндинг таким образом, чтобы была возможность создать несколько генераторов.
class DataGenerator:
	def __init__(self):
		self.lib = cdll.LoadLibrary('./libBackEnd.so')
		self.lib.generate_string.restype = c_char_p
		self.lib.generate_string.argtypes = [c_int]
		self.lib.generate_wstring.restype = c_wchar_p
		self.lib.generate_wstring.argtypes = [c_int]
		self.lib.generate_int32.restype = c_int
		self.lib.generate_int32.argtypes = [c_int, c_int]
		self.lib.mutate_int32.restype = c_int
		self.lib.mutate_int32.argtypes = [c_int, c_int]
	def getString(self, length = 10):
		return self.lib.generate_string(length)
	def getInteger32(self, minInt = 0, maxInt = 1000):
		return self.lib.generate_int32(minInt, maxInt)
	def getUnicodeString(self, length = 10):
		return self.lib.generate_wstring(length)
	def getMutationInteger32(self, value, numberOfMutations = 10):
		return self.mutate_in32.argtypes(value, numberOfMutations)

