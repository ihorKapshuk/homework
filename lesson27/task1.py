import time
import multiprocessing

def create_indata():
    my_str = ""
    for i in range(1, 10001):
        if i != 10000:
            my_str += str(i) + "\n"
        else:
            my_str += str(i)
    with open("lesson27/indata.txt", "w") as create:
        create.write(my_str)

# create_indata()

def make_int(n):
    return int(n)

def make_sqr(a):
    result = 0
    for i in range(1, a):
        result += i
    return result

def make_calc():
    with open("lesson27/indata.txt") as r:
        my_list = r.read().split("\n")
    start = time.perf_counter()
    my_int = [make_int(el) for el in my_list]
    my_res = [make_sqr(el) for el in my_int]
    end = time.perf_counter()
    print(end - start)

def make_mul_calc():
    with open("lesson27/indata.txt") as r:
        my_list = r.read().split("\n")
    start = time.perf_counter()
    with multiprocessing.Pool(6) as p:
        my_int = p.map(make_int, my_list)
        my_res = p.map(make_sqr, my_int)
    end = time.perf_counter()
    print(end - start)

if __name__ == "__main__":
    make_calc()
    make_mul_calc()