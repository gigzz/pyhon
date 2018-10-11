from threading import Thread
import time

class tests(Thread):
    def __init__(self):
        super(tests, self).__init__()

    def run(self):
        for i in range(100):
            time.sleep(1)
            print('ss')

a = tests()
a.start()