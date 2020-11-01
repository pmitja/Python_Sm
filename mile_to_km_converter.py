print("Hello user! Welcome to kilometers to miles converter.")


while True:
    kilometers = int(input("How many kilometers do you want to convert into miles?: "))
    miles = kilometers * 0.621371192
    print(f"You want to convert {kilometers} to miles. The result is {miles}.")
    repeat_statment = input("Do you want convert another amount of kilometers to miles? (Y/N): ")

    if repeat_statment == "y":
        continue
    else:
        break

print("Thank you for using our converter. Good bye!")

