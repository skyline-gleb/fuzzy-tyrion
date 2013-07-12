import random
import sys
import string

class DataGenerator(object):

	@staticmethod
	def random_int(first = 0, last = sys.maxsize):
		return random.randint(first, last)

	@staticmethod
	def random_string(length = 16):
		return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(length))