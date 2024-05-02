# Game to guess a random number between a range that the user selects
import random

num_range_lower = int(input("Pick a number between 1 and 100 for the lower limit: "))
num_range_upper = int(input("Pick a number between 1 and 100 for the upper limit: "))
num_rand = random.randint(num_range_lower, num_range_upper)

