def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr.pop() * productOfArray(arr)


if __name__ == "__main__":
    print(productOfArray([1, 2, 3, 10]))
