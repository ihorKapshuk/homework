import json

def make_phonebook(phonebook_name):
    try:
        with open(phonebook_name) as try_read:
            test = json.load(try_read)
    except FileNotFoundError:
        with open(phonebook_name, "w") as try_read:
            json.dump([], try_read)

def add_record(new_first_name, new_last_name, new_tel_number, new_city, phonebook_name):
    my_record = {
            "first_name" : new_first_name,
            "last_name" : new_last_name,
            "tel_number" : new_tel_number,
            "city" : new_city
        }
    with open(phonebook_name) as get_records:
        records_list = json.load(get_records)
    with open(phonebook_name, "w") as set_record:
        records_list.append(my_record)
        json.dump(records_list, set_record)
        print("Запис додано!")

def find_record(value, phonebook_name):
    with open(phonebook_name) as get_records:
        records_list = json.load(get_records)
    if len(records_list) == 0:
        print("Телефонна книга пуста!")
    else:
        for record in records_list:
            full_name = record["first_name"] + " " + record["last_name"]
            if record["first_name"] == value or record["last_name"] == value or record["tel_number"] == value or record["city"] == value or full_name == value:
                print("Запис знайдено!")
                for k, v in record.items():
                    print(k, " : ", v)
                break
        else:
            print("Запис не знайдено!")

def delete_record(tel_number, phonebook_name):
    with open(phonebook_name) as get_records:
        records_list = json.load(get_records)
    for record in records_list:
        if record["tel_number"] == tel_number:
            records_list.remove(record)
            with open(phonebook_name, "w") as del_record:
                json.dump(records_list, del_record)
            break
    else:
        print("Нема запису з введеним номером!")

def update_record(old_tel_number, new_tel_number, phonebook_name):
    with open(phonebook_name) as get_records:
        records_list = json.load(get_records)
    for record in records_list:
        if record["tel_number"] == old_tel_number:
            record["tel_number"] = new_tel_number
            with open(phonebook_name, "w") as up_record:
                json.dump(records_list, up_record)
            break
    else:
        print("Нема запису з введеним номером!")