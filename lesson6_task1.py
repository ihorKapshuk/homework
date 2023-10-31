import random

rand_list = []

while len(rand_list) < 10:
    rand_list.append(random.randint(1, 10))
else:
    print("Список з випадковими числами довжиною 10 : ", rand_list)
    print("Його найбільший елемент : ", max(rand_list))