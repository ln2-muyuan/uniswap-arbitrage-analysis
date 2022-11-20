import json
import threading

test_pairs = json.load(open('../src/files/pairs_test_2.json'))


def handle_pairs(pairs):
    updated_pairs = []
    for i in range(len(pairs)):
        result = str(i) + "  " + pairs[i]['address']
        updated_pairs.append(result)
    return updated_pairs


class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        # print(self.func)
        print(self.args)
        # self.result = self.func(self.args)


# directly pass the list as an argument
t = MyThread(handle_pairs, test_pairs)
t.start()
