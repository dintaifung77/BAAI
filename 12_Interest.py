#
# Zach
# 11/6/24
# calculate interest = (principal * rate * time)/100
#

# define function
def calculate_interest(p,r,t):
        interest = (p * r * t)/100
        return interest

# 2. Process
# Call function
y = calculate_interest(1000,5,2)

# 3. Output
print(f'Answer: {y}')