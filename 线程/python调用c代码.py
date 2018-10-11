from ctypes import *
from threading import * 
lib = cdll.LoadLibrary("./test.so")

th = Thread(target=lib.Test)
th.start()

while True:
    pass
