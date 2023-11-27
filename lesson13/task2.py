def say_hallo():
    return "Hello"

def say_goodbay():
    return "Goodbay"

def reactor(choise, hello, goodbay):
    if choise == 1:
        return hello()
    elif choise == 0:
        return goodbay()
    else:
        return "OK"

print(reactor(1, say_hallo, say_goodbay))