from mymod import test as test_string

def make_file(value):
    f = open("newfile.txt", "w")
    for i in range(value):
        f.write("Hello!\n")
    f.close

make_file(10)
test_string("newfile.txt")