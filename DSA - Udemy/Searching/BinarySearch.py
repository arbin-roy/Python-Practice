from math import floor


def binarySearch(array, searchValue):
    start = 0
    end = len(array) - 1
    middle = floor((start + end) / 2)

    while not array[middle] == searchValue and start <= end:
        if searchValue < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = floor((start + end) / 2)
        # print(start, middle, end)

    return middle if array[middle] == searchValue else -1


cArr = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(cArr, 20))
