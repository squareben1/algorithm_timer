from random import randint
from collections import Counter

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = round((low + high) / 2)
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


def linear_search(arr, find):
    for x in arr:
        if x == find:
            return True
    return False


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    copy_arr = arr[:]
    new_arr = []
    for i in range(len(copy_arr)):
        smallest = find_smallest(copy_arr)
        new_arr.append(copy_arr.pop(smallest))
    return new_arr


# this was our first attempt and resulted in a very slow, quadratic algorithm
def slow_find_dups(arr):
    duplicates = []

    for i in range(len(arr)):
        for y in range(i+1, len(arr)):
            if arr[i] == arr[y] and arr[i] not in duplicates:
                duplicates.append(arr[i])
                break
    return duplicates


def find_dups(arr):  # second, much faster attempt,
    sorted_arr = sorted(arr)
    duplicates = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1] and arr[i] not in duplicates:
            duplicates.append(arr[i])
    return duplicates


def find_uniq(arr):
    seen = []
    uniq = []
    for x in arr:
        if x not in seen:
            uniq.append(x)
            seen.append(x)
    return uniq


def slow_shuffle(array):
    new_array = []

    while array:
        random_index = randint(0, len(array)-1)
        new_array.append(array[random_index])
        del array[random_index]

    return new_array

def shuffle(array):
    new_array = []

    while array:
        random_index = randint(0, len(array)-1)
        array[random_index], array[-1] = array[-1], array[random_index]
        new_array.append(array.pop())

    return new_array

def knuth_shuffle(arr):
    num = len(arr)
    for i in range(num):
        index = randint(0, i)
        arr[i], arr[index] = arr[index], arr[i]
    
    return arr

def reverse(arr):
    return arr[::-1]


# def find_most_freq_word_dup(arr):
#     if len(arr) > 0:
#         word_dict = {}
#         for word in arr:
#             if word not in set(word_dict.keys()):
#                 word_dict[word] = 1
#             else:
#                 value = word_dict[word]
#                 word_dict[word] = value + 1

#         return [k for k, v in sorted(word_dict.items(), key=lambda item: item[1])][-1]


def find_most_freq_word_dup(arr): 
    counter = 0
    item = 0 

    for i in arr: 
        curr_frequency = arr.count(i) 
        if(curr_frequency > counter): 
            counter = curr_frequency 
            item = i 
  
    return item 


def find_most_common_counter_dups(arr):
    if len(arr) > 0:
        return [word for word, word_count in Counter(arr).most_common(1)][0]