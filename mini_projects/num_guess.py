# Game to guess a random number between a range that the user selects
import random

while (True):
    print("")
    print("Choose two numbers, and try to guess the number I choose between those numbers! 👍\n")
    num_lower = int(input("Pick a number between 1 and 100 for the lower limit: "))
    num_upper = int(input("Pick a number between 1 and 100 for the upper limit: "))
    num_rand = random.randint(num_lower, num_upper)

    for i in range(10):
        print("")
        user_guess = int(input(f"Guess number between {num_lower} and {num_upper}: "))

        if user_guess == num_rand:
            print("🎉 Wow! You got it! 🎉")
            break
        elif user_guess > num_rand:
            print("Too high!")
        elif user_guess < num_rand:
            print("Too low!")
    
    print(f"The correct number was {num_rand}!")
    restart = input("Would you like to play again? ")
    if restart == "yes" or "Yes":
        continue
    else:
        quit()