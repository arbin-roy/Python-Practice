#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *
#
row, sc = int(input('Enter any odd number as row: ')), 1
gap = row - 1
mid = row // 2
for i in range(row):
    print(' ' * gap + '* ' * sc)
    if i < mid:
        sc += 2
        gap -= 2
    else:
        sc -= 2
        gap += 2
