from threading import *
def test():
    while True:
        pass
th = Thread(target=test)
th.start()

while True:
    pass
