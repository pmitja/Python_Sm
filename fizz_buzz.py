print("Welcome to FizzBuzz program!")

number = int(input("Select a number between 1 and 100: "))

for number in range(1, number+1):
    result_for_three = (number % 3)
    result_for_five = (number % 5)
    if result_for_three == 0 and result_for_five == 0:
        print("fizzbuzz")
    elif result_for_three == 0:
        print("fizz")
    elif result_for_five == 0:
        print("buzz")
    else:
        print(f"{number}")