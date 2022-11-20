import threading
import time


class TestThread(threading.Thread):
    def __init__(self, length, name=None):
        threading.Thread.__init__(self, name=name)
        self.result = None
        self.args = length

    def run(self):
        self.result = loop(self.args)

    def get_result(self):
        return self.result


def loop(length):
    for i in range(length):
        print(threading.current_thread().name + ' test ', i)
        time.sleep(1)
    return 'done'


thread = TestThread(5, name='TestThread')
thread.start()

print("Main thread ")

thread.join()
print(thread.get_result())

print("Main thread end")
