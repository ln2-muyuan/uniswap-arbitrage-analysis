import threading
import time


class TestThread(threading.Thread):
    def __init__(self, length, name=None):
        threading.Thread.__init__(self, name=name)
        self.args = length

    def run(self):
        loop(self.args)


def loop(length):
    for i in range(length):
        print(threading.current_thread().name + ' test ', i)
        time.sleep(1)


thread = TestThread(5, name='TestThread')
thread.start()
