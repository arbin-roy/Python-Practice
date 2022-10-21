# *        *
# **      **
# ***    ***
# ****  ****
# **********
#
row = int(input('Enter how many rows: '))
gap = (row * 2) - 2
for i in range(row):
    sc = i + 1
    print('*' * sc + ' ' * gap + '*' * sc)
    gap -= 2
