phone_number = "1234567890"

if phone_number.isdigit():
    if len(phone_number) == 10:
        print("Номер введено вірно")
    else:
        print("Номер повинен складатися з 10 цифр")
else:
    print("Номер повинне містити лише цифри")