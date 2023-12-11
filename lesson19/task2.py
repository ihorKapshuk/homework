def in_range(start : int, end : int, step=1):
    if step == 0:
        raise ValueError
    elif step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step

for i in in_range(10, 0, -1):
    print(i)