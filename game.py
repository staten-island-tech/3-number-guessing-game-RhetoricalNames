""" You will be creating a program that creates a random number and then
have the user guess the number. The code must contain all of the following
-Generate a random number between 1 and 10 (you can do more if you
want)
-Use a while loop that breaks only when the user correctly guesses the
number
-create a guess variable based on user input. There will be a global guess
variable equal to 0 and then another guess variable inside the while loop
based on user input
-using conditional statements, inform the user if their guess is less than or
greater than the random number
-push the users incorrect guess into a guess_history list. Print the used
letters at every wrong guess
-When the user guesses correctly inform them and show them their guess
history using a for loop """

import random
number = random.randint(1, 1000)

guess = 0
guess_history = [ ]
while not number == guess:
    guess = input("Guess a number")
    guess = int(guess)
    if number == guess:
        print(f"Correct. Your guess history is {guess_history}. You guessed {len(guess_history)} times.")
        quit()
    else:
        if guess < number:
            guess_history.append(guess)
            print(f"Incorrect, greater than {guess}. Numbers guessed are {guess_history}")
        else:
            guess_history.append(guess)
            print(f"Incorrect, less than {guess}. Numbers guessed are {guess_history}")