#
# Zach
# Calculate BMI
#

# 1. Input
w = int(input('Enter your weight in kilograms: '))
h = int(input('Enter your height in meters: '))

bmi = w / (h**2)
print(f'Your BMI is: {bmi}')

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