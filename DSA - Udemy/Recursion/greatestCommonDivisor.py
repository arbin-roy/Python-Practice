# Calculate the greatest common divisor of two given number
# Euclidian algorithm

def gcd(n0, n1):
    assert n0 == int(n0) and n1 == int(n1), "Numbers should be integers only"

    # if numbers are negative, converting it to positive as the results are same
    n0 = -1 * n0 if n0 < 0 else n0
    n1 = -1 * n1 if n1 < 0 else n1

    r = n0 % n1
    if r == 0:
        return n1
    return gcd(n1, r)


if __name__ == "__main__":
    num1 = 18
    num2 = 48
    print(gcd(num1, num2))
