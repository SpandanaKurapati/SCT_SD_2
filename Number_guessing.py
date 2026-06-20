import random
random_number = random.randint(1, 10)      # Generate a random number between 1 and 10

guess = int(input("Guess a number between 1 and 10: "))   # Take input from the user

if guess == random_number:      # Compare the guess with the random number
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry! Wrong guess.")
    print("The correct number was:", random_number)