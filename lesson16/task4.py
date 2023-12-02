class CustomException(Exception):

    def __init__(self, msg):
        with open("lesson16/logs.txt", "a") as write_log:
            new_log = msg + "\n"
            write_log.write(new_log)

def div(a, b):
    try:
        if b == 0:
            raise CustomException(f"Zero division attempt in fucnction {div.__name__}")
    except CustomException:
        return "Спроба ділення на нуль"
    else:
        return a / b

print(div(5, 0))