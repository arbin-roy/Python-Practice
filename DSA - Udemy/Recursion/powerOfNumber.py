# How to calculate the power of number using recursion?

def power(n, po):
    assert po == int(po), "Exponent must be integer number only"
    if po == 0:
        return 1
    elif po < 0:
        return 1 / n * power(n, po + 1)
    else:
        return n * power(n, po - 1)


if __name__ == "__main__":
    num = 5
    p = -3
    print(power(num, p))
