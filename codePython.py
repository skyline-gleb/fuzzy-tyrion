import os
from ctypes import *
lib = cdll.LoadLibrary('./BackEnd/dist/Debug/GNU-Linux-x86/libBackEnd.so')
lib.func.restype = c_char_p
lib.func.argtypes = [c_char_p]
s = lib.func("{\"col\": \"5\","
            "\"par1\":{\"type\": \"int\",\"value\": \"val\",\"typeGen\": \"1\"},"
            "\"par2\":{\"type\": \"int32\",\"value\": \"val2\",\"typeGen\": \"0\"}}")
print s
