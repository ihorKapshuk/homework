class TypeDecorators:

    @classmethod
    def to_int(cls, your_func):
        def wrapper(arg):
            result = your_func(arg)
            try:
                int(result)
            except ValueError:
                return "Конвертування в int не можливе"
            else:
                result = int(result)
                return result
        return wrapper
    
    @classmethod
    def to_bool(cls, your_func):
        def wrapper(arg):
            result = your_func(arg)
            try:
                bool(result)
            except ValueError:
                return "Конвертування в bool не можливе"
            else:
                result = bool(result)
                return result
        return wrapper
    
    @classmethod
    def to_str(cls, your_func):
        def wrapper(arg):
            result = your_func(arg)
            try:
                str(result)
            except ValueError:
                return "Конвертування в str не можливе"
            else:
                result = str(result)
                return result
        return wrapper
    
    @classmethod
    def to_float(cls, your_func):
        def wrapper(arg):
            result = your_func(arg)
            try:
                float(result)
            except ValueError:
                return "Конвертування в float не можливе"
            else:
                result = float(result)
                return result
        return wrapper

@TypeDecorators.to_int
def do_nothing(your_str : str):
    return your_str

@TypeDecorators.to_bool
def do_something(your_str : str):
    return your_str

@TypeDecorators.to_str
def do_string(value):
    return value

@TypeDecorators.to_float
def do_float(your_str : str):
    return your_str

assert do_nothing('25') == 25
assert do_something('True') is True
assert do_float("10") == 10.0
assert do_string(True) == "True"