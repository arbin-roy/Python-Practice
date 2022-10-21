#     1
#    212
#   32123
#  4321234
# 543212345
#
row = int(input('Enter how many row: '))
gap = row - 1
for i in range(row):
    num = i + 1
    print(' ' * gap, end='')
    while num > 1:
        print(num, end='')
        num -= 1
    else:
        while num <= (i + 1):
            print(num, end='')
            num += 1
    print()
    gap -= 1
