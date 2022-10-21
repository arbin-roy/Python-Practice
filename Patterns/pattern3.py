# 12345
#  1234
#   123
#    12
#     1
#
row = int(input('Enter how many rows: '))
for i in range(row):
    print(' ' * i + ''.join([str(j + 1) for j in range(row - i)]))
