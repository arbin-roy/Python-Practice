# Code will fail if input is an empty string

def isPalindrome(strng):
    length = len(strng)
    if length < 3:
        return True if strng[0] == strng[-1] else False
    if strng[0] == strng[-1]:
        isPalindrome(strng[1:-1])
    else:
        return False
    return True


if __name__ == "__main__":
    print(isPalindrome(''))
