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
    return_arr = []

    for i in range(len(arr)):
        for y in range(i+1, len(arr)):
            if arr[i] == arr[y] and arr[i] not in return_arr:
                return_arr.append(arr[i])
                break
    return return_arr


# TODO incorporate sorted list to speed up and remove nested for loop
"""
sort list A
sort list B (according to the same sort order)
I = 0
J = 0
repeat
  X = A[I]
  Y = B[J]
  if X matches Y then
    add (X, Y) to results
    increment I
    increment J
  else if X < Y then
    increment I
  else increment J
until either index reaches the end of its list
If you do it this way, instead of the number of matches operations being based on length(A) * length(B), it's now based on length(A) + length(B), which means your code will run much faster.
"""
