#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

row = int(input('Enter how many rows: '))
for i in range(1, (row * 2)):
    if i <= row:
        print(' ' * (row - i) + '*' * i)
    else:
        g = i - row
        print(' ' * g + '*' * (i - (g * 2)))
