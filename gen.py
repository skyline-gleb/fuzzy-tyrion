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
		self.lib.generate_short.restype = c_short
		self.lib.generate_short.argtypes = [c_short, c_short]
		self.lib.generate_ushort.restype = c_ushort
		self.lib.generate_ushort.argtypes = [c_ushort, c_ushort]
		self.lib.generate_int32.restype = c_int
		self.lib.generate_int32.argtypes = [c_int, c_int]
		self.lib.generate_uint32.restype = c_uint
		self.lib.generate_uint32.argtypes = [c_uint, c_uint]
		self.lib.generate_int64.restype = c_longlong
		self.lib.generate_int64.argtypes = [c_longlong, c_longlong]
		self.lib.generate_uint64.restype = c_ulonglong
		self.lib.generate_uint64.argtypes = [c_ulonglong, c_ulonglong]
		self.lib.mutate_int32.restype = c_int
		self.lib.mutate_int32.argtypes = [c_int, c_int]
	def getString(self, length = 10):
		return self.lib.generate_string(length)
	def getUnicodeString(self, length = 10):
		return self.lib.generate_wstring(length)
	def getShort(self, minShort = 0, maxShort = 1000):
		return self.lib.generate_short(minShort, maxShort)
	def getUnShort(self, minUnShort = 0, maxUnShort = 1000):
		return self.lib.generate_ushort(minUnShort, maxUnShort)
	def getInteger32(self, minInt32 = 0, maxInt32 = 1000):
		return self.lib.generate_int32(minInt32, maxInt32)
	def getUnInteger32(self, minUnInt32 = 0, maxUnInt32 = 1000):
		return self.lib.generate_uint32(minUnInt32, maxUnInt32)
	def getInteger64(self, minInt64 = 0, maxInt64 = 1000):
		return self.lib.generate_int32(minInt64, maxInt64)
	def getUnInteger64(self, minUnInt64 = 0, maxUnInt64 = 1000):
		return self.lib.generate_uint32(minUnInt64, maxUnInt64)
	def getMutationInteger32(self, value, numberOfMutations = 10):
		return self.mutate_in32.argtypes(value, numberOfMutations)

