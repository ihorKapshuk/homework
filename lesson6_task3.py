start_list = []

while len(start_list) < 100:
    start_list.append(len(start_list) + 1)
else:
    finish_list = []
    index = 0
    while index < len(start_list) - 1:
        if start_list[index] % 7 == 0 and start_list[index] % 5 != 0:
            finish_list.append(start_list[index])
        index += 1
    else:
        print("\nСписок з усіма числами від 1 до 100 : ", start_list)
        print("\nСписок з усіма числами, що діляться на 7 але не кратні 5 : ", finish_list)