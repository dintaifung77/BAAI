#
# Zach
# 11/6/24
# Calculate BMI
#

while True:
    w = float(input('Enter your weight in kilograms: '))
    h = float(input('Enter your height in meters: '))

    bmi = w / (h**2)
    print(f'Your BMI is: {bmi}')

    answer = input('Continue? (yes/no): ')
    if answer == 'no':
        break