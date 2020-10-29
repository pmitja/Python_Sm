import random

SECRET = random.randint(1,50)
guess = None
number_of_tries = 10

while number_of_tries > 0:
    try:
        guess = int(input("Please pick one number between 1 and 30: "))
    except ValueError:
        print("Input need to be integer.")
        continue
    number_of_tries -= 1
    if 0 > guess or guess > 50:
        print("Number is not in range.")
        continue
    if SECRET == guess:
        print(f"You guess right number! The number is {guess}")
        break
    else:
        print(f"Sorry you picked wrong number.")

print(f"Thanks for playing, the secret number was {SECRET}.")