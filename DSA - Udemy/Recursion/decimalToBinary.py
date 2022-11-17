def decimalToBinary(n):
    assert n == int(n), "Number should be an integer only"
    if n == 0:
        return 0
    return n % 2 + 10 * decimalToBinary(int(n / 2))


if __name__ == "__main__":
    num = 25
    print(decimalToBinary(num))
