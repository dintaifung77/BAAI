#
# Zach
# Repeat the task three times
#

# 1. Input
i = 1
while i < 4:
    n1 = input('Number 1: ')
    n2 = input('Number 2: ')

    # 2. Process
    if int(n1) > int(2):
        bigger = int(n1)
    elif int(n1) < int(n2):
        bigger = int(n2)
    else:
        bigger = 'Same'

    # 3. Output
    print(f'Bigger : {bigger}')
    i += 1