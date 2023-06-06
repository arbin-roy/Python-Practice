def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quickSort(customList, left, right):
    if left < right:
        pivot_index = pivot(customList, left, right)
        quickSort(customList, left, pivot_index - 1)
        quickSort(customList, pivot_index + 1, right)
    return customList


cList = [3, 5, 0, 6, 2, 1, 4]
print(quickSort(cList, 0, 6))
