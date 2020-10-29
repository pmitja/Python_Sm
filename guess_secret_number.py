secret = 3

user_number = int(input("Please pick one number between 1 and 30: "))

if secret == user_number:
    print(f"You guess right number! The number is {user_number}")
else:
    print(f"Sorry you picked wrong number. Right number was {secret}")