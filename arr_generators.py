import random


def arr_generator(num_arrs, limit):
    output_arr = [[]]
    step = limit // num_arrs
    for i in range(1, num_arrs+1):
        output_arr.append(list(range(1, (i * step)+1)))
    return output_arr


def insert_dup(arr, dup_percent=10):
    interval = int(100 / dup_percent)
    for sub_arr in arr:
        for i in range(0, len(sub_arr), interval):
            sub_arr[i] += 1
    return arr
