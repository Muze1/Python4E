# Basic stuffs
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