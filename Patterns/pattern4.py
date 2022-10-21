# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

row = int(input('Enter how many rows: '))
for i in range(row):
    print('*' * (i + 1))
else:
    for j in range(row - 1, 0, -1):
        print('*' * j)
