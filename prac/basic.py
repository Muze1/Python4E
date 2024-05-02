# Basic Python stuffs
msg = "Hello World"
print(msg)

# BMI Calc
weight = 70
height = 175
bmi = weight / (height / 100)
print(bmi)

# Roll a dice - twice!
import random
roll = random.randint(1, 6)
print(roll)
roll = random.randint(1, 6)
print(roll)

# Roll a dice - loop
# Don't need to import random again
for i in range(5):
    loop_roll = random.randint(1, 6)
    print(loop_roll)

# Conditional or if statements
num = 5
if num > 10:
    print("Okay, good work!")
else:
    print("Oh no...")

# Ternary Operator
num2 = 10
print("It works!") if num2 >= 10 else print("Maybe next time...")