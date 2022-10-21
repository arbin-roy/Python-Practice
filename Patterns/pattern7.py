# *****
# ****
# ***
# **
# *
# **
# ***
# ****
# *****

row = v = int(input('Enter how many row: '))
while row > 0:
    print('*' * row)
    row -= 1
else:
    for i in range(2, v + 1):
        print('*' * i)
