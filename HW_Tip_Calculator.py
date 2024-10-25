#
# Zach
# Enter number of people dining, type in amount spent per person and tip percentage, sum total bill
#

# 1. Input
s = int(input('How many people are dining? '))
print("\n")
sum = 0
count = 1 # count is currently equal to 1, but after the loop has run, it will increase to 2, 3, 4, and so on

while (count <= s):
    s1 = int(input(f'Enter the amount spent by person {count}: '))
    sum = sum + s1
    count += 1     # count= count + 1
print("\n")
s = int(input('Enter the tip percentage: '))

# 2. Process
total = sum * (1 + (s / 100))
print("\n")

# 3. Output3
print (f'The total bill including tip is: ${total}')