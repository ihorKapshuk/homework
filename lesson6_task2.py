import random

rand_list1 = []
rand_list2 = []

while len(rand_list1) < 10:
    rand_list1.append(random.randint(1, 10))
    rand_list2.append(random.randint(1, 10))
else:
    print("Список з випадковими числами #1 : ", rand_list1)
    print("Список з випадковими числами #2 : ", rand_list2)
    common_list = list(set(rand_list1).intersection(set(rand_list2)))
    print("Загальні числа для обох списків : ", common_list)