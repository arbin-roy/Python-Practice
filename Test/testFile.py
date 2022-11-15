def rec(n):
    if n < 1:
        print("n is less than 1")
    else:
        rec(n - 1)
        print(n)


def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n - 1)
        return power * 2


if __name__ == "__main__":
    num = 5
    # rec(num)
    print(powerOfTwo(num))
