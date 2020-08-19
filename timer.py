from timeit import default_timer as timer
import random

arr = list(range(1000000))


def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = round((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


num = random.randint(1, len(arr))


def basic_timer(func, *args):
    start = timer()
    func(*args)
    end = timer()
    value = end - start
    print('%.12f' % value)


basic_timer(binary_search, arr, 999999)
