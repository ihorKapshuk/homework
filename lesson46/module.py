from random import randint
import time



# unsorted list generation
def create_unsorted_list() -> list[int]:
    return [randint(1, 100) for _ in range(500)]



# time counter for algorithms speed analize
def count_time(func, your_list : list[int]) -> str:
    start = time.perf_counter()
    if func.__name__ == "quick_sort":
        func(your_list, 0, len(your_list) - 1)
    else:
        func(your_list)
    end = time.perf_counter()
    res_time = (end - start) * 1000
    return f"{func.__name__} : {res_time} ms"



# bubble sort algorithm
def bubble_sort(your_list : list[int]) -> list[int]:
    n = len(your_list)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if your_list[j] > your_list[j+1]:
                your_list[j], your_list[j+1] = your_list[j+1], your_list[j]
                swapped = True
        if (swapped == False):
            break
    return your_list



# helper function for quick sort algorithm
def partition(your_list : list[int], low : int, high : int) -> int:
    pivot = your_list[high]
    i = low - 1
 
    for j in range(low, high):
        if your_list[j] <= pivot:
            i = i + 1
            (your_list[i], your_list[j]) = (your_list[j], your_list[i])
    (your_list[i + 1], your_list[high]) = (your_list[high], your_list[i + 1])

    return i + 1



# quick sort algorithm 
def quick_sort(your_list : list[int], low : int, high : int) -> list[int]:
    if low < high:
        pi = partition(your_list, low, high)
        quick_sort(your_list, low, pi - 1)
        quick_sort(your_list, pi + 1, high)
    return your_list



# merge sort algorithm
def merge_sort(your_list : list[int]) -> list[int]:
    if len(your_list) > 1:

        mid = len(your_list)//2
        L = your_list[:mid]
        R = your_list[mid:]
        merge_sort(L)
        merge_sort(R)
 
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                your_list[k] = L[i]
                i += 1
            else:
                your_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            your_list[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            your_list[k] = R[j]
            j += 1
            k += 1
    return your_list