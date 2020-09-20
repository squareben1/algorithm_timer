import random


def arr_generator(num_arrs, limit):
    output_arr = [[]]
    step = limit // num_arrs
    for i in range(1, num_arrs+1):
        output_arr.append(list(range(1, (i * step)+1)))
    return output_arr
