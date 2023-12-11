def with_index(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1

my_str = "qwerty"
for i, el in with_index(my_str):
    print(i, " : ", el)