import random

secret_number = random.randint(1,10)
attempts = 3

print("I'm thinking of a number between 1 and 10")

while attempts > 0:
    guess = int(input("Take a Guess: "))
    if guess == secret_number:
        print("congrat's you guessed the number")
        attempts = 0
    elif guess > secret_number:
        print("you guessing too high")
    else:
        print("you guessing too low")
    attempts -= 1

if attempts == 0:
    print("sorry, you have run out of attempts the secret number was", secret_number)
    


