#
# Zach
# Shopping Cart
#

# 1. Input
s = int(input('How many items do you want to buy? '))
print("\n")
sum = 0
count = 1 # count is currently equal to 1, but after the loop has run, it will increase to 2, 3, 4, and so on

while (count <= s):
    n = input(f'Enter the name of item {count}: ')
    p = int(input(f'Enter the price of {n}: '))
    q = int(input(f'Enter the quantity of {n}: '))
    total = p * q
    print (f'Total cost for {n}: {total}')

    # 2. Process
    sum += total
    count += 1     # count= count + 1
    print("\n")

# 3. Output
print (f'Total cost of vour shopping cart: ${sum}')