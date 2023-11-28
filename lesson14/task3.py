def arg_rules(type_ : type, max_length : int, contain : list):
    def arg_decorator(your_func):
        def wrapper(value):
            result = your_func(value)
            for element in contain:
                if  not (element in result):
                    print("Аргумент функції ", your_func.__name__, " не містить ", contain)
                    return False
            if type(result) != type_:
                print("Аргумент функції ", your_func.__name__, " не є ", type_)
                return False
            elif len(value) > max_length:
                print("Довжина аргументу функції", your_func.__name__, " перевищує ", max_length)
                return False
            else:
                return result
        return wrapper
    return arg_decorator

@arg_rules(type_=str, max_length=15, contain=["05", "@"])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'