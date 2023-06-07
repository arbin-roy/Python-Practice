def linerSearch(array, searchValue):
    for i in array:
        if i is searchValue:
            return array.index(i)
    return -1


cList = [2, 7, 6, 5, 3, 4, 9, 8, 1]
print(linerSearch(cList, 6))
