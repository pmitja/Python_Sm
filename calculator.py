print("@@@  Welcome to simple calculator!   @@@")
print("This simple calculator, calculate two random numbers. With +, -, * or /")

try:
    first_number = int(input("Please type first number: "))
except:
    print("Input need to be a number")
try:
    second_number = int(input("Please type second number: "))
except:
    print("Input need to be a number")

operation = input("Which operation would you like?: ")
result = 0

if operation == "+":
    result = first_number + second_number
    print(f"Result of first number and second number with operation + is: {result}")
elif operation == "-":
    result = first_number - second_number
    print(f"Result of first number and second number with operation - is: {result}")
elif operation == "*":
    result = first_number * second_number
    print(f"Result of first number and second number with operation * is: {result}")
elif operation == "/":
    result = first_number / second_number
    print(f"Result of first number and second number with operation / is: {result:.2f}")
else:
    print("Wrong operation, please try again!")
