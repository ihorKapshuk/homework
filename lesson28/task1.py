import threading
import time

def make_sqr_list(your_list : list):
    new_list = []
    for el in your_list:
        time.sleep(0.005)
        new_list.append(el ** 2)

def make_cube_list(your_list : list):
    new_list = []
    for el in your_list:
        time.sleep(0.005)
        new_list.append(el ** 3)

def count_time(your_list : list):
    start = time.perf_counter()
    make_sqr_list(your_list)
    make_cube_list(your_list)
    end = time.perf_counter()
    return end - start

def count_time_th(your_list : list):
    start = time.perf_counter()
    t1 = threading.Thread(target=make_sqr_list, args=(your_list,))
    t2 = threading.Thread(target=make_cube_list, args=(your_list,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end = time.perf_counter()
    return end - start

if __name__ == "__main__":
    my_list = [i for i in range(1, 101)]

    print(count_time(my_list))
    print(count_time_th(my_list))