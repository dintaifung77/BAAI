#
# Zach
# Take two numbers then print the bigger one
#

# 1. Input
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