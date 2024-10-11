#
# Zach
# Enter number of class subjects, type in subject names, enter and sum those grades and print the average
#

# 1. Input
s = int(input('How many subjects do you have? '))
print("\n")
sum = 0
count = 1 # count is currently equal to 1, but after the loop has run, it will increase to 2, 3, 4, and so on

while (count <= s):
    s1 = input(f'Enter the name of subject {count}: ')
    n1 = int(input(f'Enter the grade for {s1}: '))
    print("\n")
    sum = sum + n1
    count += 1     # count= count + 1

# 2. Process
avg = int(sum / s)

# 3. Output
print (f'Your average grade is: {avg}')