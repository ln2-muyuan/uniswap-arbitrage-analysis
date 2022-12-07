import time
from thread import *
from update import *


def main():
    start_time = time.time()
    if len(pairs) < 200:
        updated_pairs = get_reserves(pairs)
    else:
        threads = []
        updated_pairs = []
        length = 200
        finished_count = 0
        while finished_count < len(pairs):
            if finished_count + length > len(pairs):
                length = len(pairs) - finished_count
            threads.append(MyThread(get_reserves, (pairs[finished_count:finished_count + length],)))
            finished_count += length
        for t in threads:
            t.start()
        for t in threads:
            t.join()
            updated_pairs += t.get_result()
    end_time = time.time()
    print("Updating cost time: " + str(end_time - start_time) + "s")
    # for pair in updated_pairs:
    #     print(pair)


if __name__ == "__main__":
    main()
