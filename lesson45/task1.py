from random import randint
import time

def get_sorted_list(val : int) -> list:
    my_list = [randint(1, 100) for i in range(10000)]
    my_list.append(val)
    my_list = sorted(my_list)
    return my_list

def linear_search(your_list : list [int], val : int) -> str:
    start = time.perf_counter()

    for num in your_list:
        if num == val:
            break
    
    end = time.perf_counter()
    res = (end - start) * 1000
    return f"Linear search : {res} ms"

def binary_search(your_list : list [int], val : int, low : int, high : int) -> str:
    start = time.perf_counter()

    while low <= high:
        mid = low + (high - low)//2
        if your_list[mid] == val:
            break
        elif your_list[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    end = time.perf_counter()
    res = (end - start) * 1000
    return f"Binary search : {res} ms"

my_value = 77

sorted_list = get_sorted_list(my_value)
print(linear_search(sorted_list, my_value))
print(binary_search(sorted_list, my_value, 0, len(sorted_list) - 1))