# Write a recursive function called fib which accepts a number and returns the nth number in the Fibonacci sequence.

def fib(num):
    assert num == int(num) and num >= 0, "Number should be a positive integer only"
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


if __name__ == "__main__":
    print(fib(4))
