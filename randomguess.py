import random

number = random.randint(1, 20)
guess = int(input("Guess a number between 1 and 20: "))

while guess != number:
    if guess < number:
        print("Your guess is too low.")
        guess = int(input("Guess again: "))
    else:
        print("Your guess is too high.")
        guess = int(input("Guess again: "))

print("Congratulations! You guessed the number!")