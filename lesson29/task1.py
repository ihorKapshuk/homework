import asyncio
import multiprocessing
import time

async def my_fibonacci(your_list : list):
    result = []
    print("Почалось обчислення фібоначчі ...")
    for el in your_list:
        my_list = [0, 1]
        if el == 1:
            await asyncio.sleep(0.01)
            result.append(my_list[0])
        elif el == 2:
            await asyncio.sleep(0.01)
            result.append(my_list[1])
        else:
            for i in range(el - 2):
                await asyncio.sleep(0.01)
                my_list.append(my_list[len(my_list) - 1] + (my_list[len(my_list) - 2]))
            result.append(my_list[el - 1])
    print("Обчислення фібоначчі закінчилось.")
    return result

def my_fibonacci_mul(your_list : list):
    result = []
    for el in your_list:
        my_list = [0, 1]
        if el == 1:
            result.append(my_list[0])
        elif el == 2:
            result.append(my_list[1])
        else:
            for i in range(el - 2):
                my_list.append(my_list[len(my_list) - 1] + (my_list[len(my_list) - 2]))
            result.append(my_list[el - 1])

async def my_factorial(your_list : list):
    res = []
    print("Почалось обчислення факторіал ...")
    for el in your_list:
        f = 1
        for i in range(2, el + 1):
            await asyncio.sleep(0.01)
            f *= i
        res.append(f)
    print("Обчислення факторіал закінчилось.")
    return res

def my_factorial_mul(your_list : list):
    res = []
    for el in your_list:
        f = 1
        for i in range(2, el + 1):
            f *= i
        res.append(f)

async def my_sqr(your_list : list):
    print("Почалось обчислення квадрат ...")
    await asyncio.sleep(0.01)
    print("Обчислення квадрат закінчилось.")
    return [el ** 2 for el in your_list]

def my_sqr_mul(your_list : list):
    res = [el ** 2 for el in your_list]

async def my_cube(your_list : list):
    print("Почалось обчислення куб ...")
    await asyncio.sleep(0.01)
    print("Обчислення куб закінчилось.")
    return [el ** 3 for el in your_list]

def my_cube_mul(your_list : list):
    res = [el ** 3 for el in your_list]

async def gather_tasks(my_list):
    return await asyncio.gather(
        my_fibonacci(my_list),
        my_factorial(my_list),
        my_sqr(my_list),
        my_cube(my_list)
    )

def make_mul(my_list : list):
    p1 = multiprocessing.Process(target=my_fibonacci_mul, args=(my_list,))
    p2 = multiprocessing.Process(target=my_factorial_mul, args=(my_list,))
    p3 = multiprocessing.Process(target=my_sqr_mul, args=(my_list,))
    p4 = multiprocessing.Process(target=my_cube_mul, args=(my_list,))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

def count_time_as(my_list):
    start = time.perf_counter()
    data = asyncio.run(gather_tasks(my_list))
    end = time.perf_counter()
    print("Час виконання асинхронних функцій : ", end - start)

def count_time_mul(my_list):
    start = time.perf_counter()
    make_mul(my_list)
    end = time.perf_counter()
    print("Час виконання функцій, використовуючи мультипроцессорність : ", end - start)

def count_time_sync(my_list):
    start = time.perf_counter()
    my_fibonacci_mul(my_list)
    my_factorial_mul(my_list)
    my_sqr_mul(my_list)
    my_cube_mul(my_list)
    end = time.perf_counter()
    print("Час виконання синхронних функцій : ", end - start) 

if __name__ == "__main__":
    my_list = [i for i in range(1, 11)]
    
    count_time_as(my_list)
    count_time_mul(my_list)
    count_time_sync(my_list)