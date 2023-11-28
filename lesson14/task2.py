def stop_words(words):
    def words_decorator(your_func):
        def wrapper(*args):
            your_func(*args)
            result = your_func(*args)
            for word in words:
                if word in result:
                    new_result = result.replace(word, "*")
                    result = new_result
            return result
        return wrapper
    return words_decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Vasil"))
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"