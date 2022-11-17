# Write a function called recursiveRange which accepts a number and adds up all the numbers from 0 to the number passed to the function.

def recursiveRange(num):
    assert num == int(num) and num >= 0, "Number should be a positive integer only"
    if num == 0:
        return 0
    return num + recursiveRange(num - 1)


if __name__ == "__main__":
    print(recursiveRange(3))
