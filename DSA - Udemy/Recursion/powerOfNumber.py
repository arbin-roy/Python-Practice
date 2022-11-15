def power(n, po):
    if p == 0:
        return 1
    else:
        return n * power(n, po - 1)


if __name__ == "__main__":
    num = 2
    p = 4
    print(power(num, p))
