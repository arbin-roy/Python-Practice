def reverse(strng):
    if strng == '':
        return ''
    return strng[len(strng) - 1] + reverse(strng[:-1])


if __name__ == "__main__":
    print(reverse('arbin'))
