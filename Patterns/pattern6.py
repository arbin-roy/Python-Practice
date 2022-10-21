# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *

row = v = int(input('Enter how many rows: '))
for i in range(0, (row * 2) - 1):
    if row >= 1:
        print(' ' * i + '* ' * row)
        row -= 1
    else:
        val = ((i + 1) - v) + 1
        print(' ' * (v - val) + '* ' * val)
