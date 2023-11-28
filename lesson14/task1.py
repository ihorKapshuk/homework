import time

def time_decorator(your_func):
    def wrapper(*args):
        start = time.perf_counter()
        result = your_func(*args)
        end = time.perf_counter()
        print("Час виконання функції ", your_func.__name__, " : ", str((end - start) * 1000), " ms")
        return result
    return wrapper

@time_decorator
def adder(*values):
    result = 0
    for value in values:
        result += value
    return result

@time_decorator
def make_x_pow_list(x):
    my_list = [i ** x for i in range(1, 101)]
    return my_list

print(adder(3, 5, 89, 27, 90))
print(make_x_pow_list(2))