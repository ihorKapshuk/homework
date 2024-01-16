from multiprocessing import Lock, Process, Value
import time

def adder(result, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            result.value += 10

def subber(result, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            result.value -= 10

if __name__ == "__main__":
    res = Value("i", 1000)
    lock = Lock()

    add_p = Process(target=adder, args=(res, lock))
    sub_p = Process(target=subber, args=(res, lock))

    add_p.start()
    sub_p.start()

    add_p.join()
    sub_p.join()

    print(res.value)