import random

user_string = input("Введіть строку : ")

for i in range(5):
    rand_string = list(user_string)
    random.shuffle(rand_string)
    print("".join(rand_string))