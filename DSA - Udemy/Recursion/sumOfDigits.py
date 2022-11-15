# How to find the sum of digits of a positive integer number using recursion?

def sumOfDigits(n):
    assert n >= 0 and n == int(n), 'The number has to be a positive integer only'
    if n < 10:
        return n
    else:
        return n % 10 + sumOfDigits(n // 10)


if __name__ == "__main__":
    num = 156
    print(sumOfDigits(num))
