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


def socks(n, socksList):
    tPair = 0
    for i in set(socksList):
        tPair += int(socksList.count(i) / 2)
    return tPair


def books(book_stack, user_request):
    output = []
    for i in user_request:
        if book_stack.count(i) != 0:
            output.append(book_stack.index(i) + 1)
            book_stack.remove(i)
        else:
            output.append(-1)
    return output


def test(val):
    for i in range(val):
        print(i)


def removeDuplicateElements(l):
    return sorted(list(set(l)))


def stringProcessor(input1, input2):
    if len(input1) > 25 or len(input2) > 25:
        return -1
    else:
        s1 = sorted(input1.replace(' ', '').lower())
        s2 = sorted(input2.replace(' ', '').lower())
        return 1 if s1 == s2 else 0


if __name__ == "__main__":
    # data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    # num = 5
    # rec(num)
    # print(powerOfTwo(num))
    # print(socks(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
    # print(books([34, 67, 8, 98, 34, 2, 34, 65, 76, -1], [8, 25, 34, 98]))
    # test(5)
    # print(removeDuplicateElements([10, 23, 65, 34, 78, 23, 45, 18, 34]))
    print(stringProcessor('Samsung galaxy s4', 'galaxy s4 Samsung'))
    print([0] * (3 * 3))
