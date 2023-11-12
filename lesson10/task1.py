def oops():
    raise IndexError
    # raise KeyError   в цьому разі помилка не буде оброблена в блоці except та буде викликана в терміналі

def oops_inside():
    try:
        oops()
    except IndexError:
        print("Index error")

oops_inside()