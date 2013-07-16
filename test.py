#/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from gen import DataGenerator

class TestSequenceFunctions(unittest.TestCase):
	def setUp(self):
		self.length = 10
		self.min = -100000000
		self.max = 100000000
		self.generator = DataGenerator()
	def test_length(self):
		string = self.generator.getString(self.length)
		self.assertEqual(self.length, len(string))
	def test_range(self):
		integer = self.generator.getInteger32(self.min, self.max)
		self.assertEqual((self.min < integer), (integer < self.max)) 
if __name__ == '__main__':
	unittest.main()
		
