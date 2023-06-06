from math import sqrt, ceil


def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i + 1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    # print(customList)
    return customList


def bucketSort(customList):
    numberOfBuckets = round(sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    # creation of buckets
    for i in range(numberOfBuckets):
        arr.append([])

    # entering items into appropriate bucket
    for j in customList:
        index = ceil(j * numberOfBuckets / maxValue)
        arr[index - 1].append(j)

    # sorting each bucket
    for i in range(numberOfBuckets):
        arr[i] = insertionSort(arr[i])

    # merging the buckets
    customList.clear()
    for i in range(numberOfBuckets):
        customList += arr[i]
    print(customList)

    # k = 0
    # for i in range(numberOfBuckets):
    #     for j in range(len(arr[i])):
    #         customList[k] = arr[i][j]
    #         k += 1
    # print(customList)


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    if l < r:
        m = (l + (r - 1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList


def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and customList[l] < customList[smallest]:
        smallest = l
    if r < n and customList[r] < customList[smallest]:
        smallest = r

    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)

    for i in range(n-1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)

    customList.reverse()
    return customList


cList = [2, 7, 6, 5, 3, 4, 9, 8, 1]
# bubbleSort(cList)
# selectionSort(cList)
# insertionSort(cList)
# bucketSort(cList)
# print(mergeSort(cList, 0, 8))
print(heapSort(cList))
