import random
import sys
import string

class DataGenerator(object):

	@staticmethod
	def generate_integer(first = 0, last = sys.maxsize):
		return random.randint(first, last)

	@staticmethod
	def generate_float():
		return DataGenerator.generate_integer() / (10**DataGenerator.generate_integer(0, 10))

	@staticmethod
	def generate_string(length = 16):
		return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))