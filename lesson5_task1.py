import random

computer_number = random.randint(1, 10)
user_number = int(input("Вгадайте число від 1 до 10. Введіть ваш варіант : "))

if user_number == computer_number:
    print(f"Ви вгадали!))) Це {computer_number}!")
else:
    print(f"Ви не вгадали!((( Це {computer_number}!")