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


def linear_search(mylist, find):
    for x in mylist:
        if x == find:
            return True
    return False


def find_dups(arr):
    return []
