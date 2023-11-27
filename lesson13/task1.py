def make_op(a, b, c):
    result = a * a + b * b - c * c
    return result

num_of_vars = lambda your_func : your_func.__code__.co_nlocals

print("Кількість локальних зміннних в функції ", make_op.__name__, " : ", num_of_vars(make_op))