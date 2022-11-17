def fac(num):
    assert num == int(num) and num >= 0, "Number should be a positive integer only"
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


if __name__ == "__main__":
    n = 4
    print(fac(n))
