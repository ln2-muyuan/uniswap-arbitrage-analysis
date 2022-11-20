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
        # print(self.args)
        # print(*self.args)
        print("Thread " + str(self.ident) + " started")
        self.result = self.func(*self.args)

    def get_result(self):
        return self.result


# use tuple as an argument
finished_count = 0
start_index = 0
length = 5
while finished_count < len(test_pairs):
    end_index = start_index + length
    if end_index > len(test_pairs):
        end_index = len(test_pairs)
    t = MyThread(handle_pairs, (test_pairs[start_index:end_index],))
    t.start()
    start_index += length
    finished_count += length

