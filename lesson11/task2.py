from module import make_phonebook, add_record, find_record, delete_record, update_record

my_phonebook_name = "lesson11/phonebook.json"

def phonebook_start(file_name):
    make_phonebook(phonebook_name=file_name)
    user_state = ""
    print("Це електронна телефонна книга!\n\
Напишіть a якщо хочете додати запис до телефонної книги\n\
Напишіть f якщо хочете знайти запис в телефонній книзі\n\
Напишіть d якщо хочете видалити запис з телефонної книги\n\
Напишіть u якщо хочете оновити телефонний номер запису телефонної книги\n\
Напишіть q якщо хочете вийти з телефонної книги")
    while user_state != "q":
        user_state = input("Введіть ваше рішення : ")
        if user_state == "a":
            first_name = input("Введіть ваше ім'я : ")
            last_name = input("Введіть ваше прізвище : ")
            tel_number = input("Введіть ваш номер телефону : ")
            city = input("Введіть назву вашого міста : ")
            add_record(new_first_name=first_name, new_last_name=last_name, new_tel_number=tel_number, new_city=city, phonebook_name=file_name)
        elif user_state == "f":
            my_value = input("Введіть ім'я, прізвище, повне ім'я, номер телефону чи назву міста : ")
            find_record(value=my_value, phonebook_name=file_name)
        elif user_state == "d":
            del_tel_number = input("Введіть телефонний номер запису, який хочите видалити : ")
            delete_record(tel_number=del_tel_number, phonebook_name=file_name)
        elif user_state == "u":
            old_t_n = input("Введіть телефонний номер запису, який хочете оновити : ")
            new_t_n = input("Введіть новий телефонний номер : ")
            update_record(old_tel_number=old_t_n, new_tel_number=new_t_n, phonebook_name=file_name)

phonebook_start(my_phonebook_name)