def count_lines(name):
    f = open(name, "r")
    return_value = len(f.readlines())
    f.close()
    return return_value

def count_chars(name):
    f = open(name, "r")
    return_value = len(f.read())
    f.close()
    return return_value

def test(name):
    print(count_lines(name))
    print(count_chars(name))