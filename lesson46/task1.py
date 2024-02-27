from module import create_unsorted_list, count_time, bubble_sort, quick_sort, merge_sort


if __name__ == "__main__":

    my_list = create_unsorted_list()
    my_funcs = [bubble_sort, quick_sort, merge_sort]

    for func in my_funcs:
        print(count_time(func, my_list))