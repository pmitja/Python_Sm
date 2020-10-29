secret = 3
number_of_tries = 3
print("Hello Holmes! Guess our secret number and win prize.")

for x in range(3):
    print(f"You will have {number_of_tries} tries. Good luck!")
    user_number = int(input("Please pick one number between 1 and 30: "))
    number_of_tries -= 1
    if 0 > user_number or user_number > 30:
        print("Number is not in range.")
        continue
    if secret == user_number:
        print(f"You guess right number! The number is {user_number}")
        break
    else:
        print(f"Sorry you picked wrong number.")


