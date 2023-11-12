def add():
    a = int(input("a = "))
    b = int(input("b = "))
    return a**2 / b

def add_catcher():
    try:
        result = add()
    except ValueError:
        return "Введені значення не є числами!"
    except ZeroDivisionError:
        return "Значення b не може дорівнювати нулю!"
    else:
        return result

print(add_catcher())