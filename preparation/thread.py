import threading
import time


class TestThread(threading.Thread):
    def __init__(self, name=None):
        threading.Thread.__init__(self, name=name)

    def run(self):
        for i in range(5):
            print(threading.current_thread().name + ' test ', i)
            time.sleep(1)


thread = TestThread(name='TestThread')
thread.start()

for i in range(5):
    print(threading.current_thread().name + ' main ', i)
    time.sleep(1)
