print("Welcome to geography quiz!")
countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}

def question(object):
    count = 0
    question_count = 0
    lenght = len(countries_cities)
    while True:
        if question_count < 4:
            for i in countries_cities:
                print(f"What is capital city of {i}")
                answer = input("User: ").capitalize()
                question_count += 1
                if answer == countries_cities[i]:
                    print("Correct!")
                    count +=1
                else:
                    print("Wrong! Next question.")
        else:
            print(f"Goodbye! You manage to correctly answered: {count} of {lenght} questions. ")
            break


option = input("Would you like play quiz (Y/N): ")

if option == "y":
    question(object)
else:
    print("Maybe next time. Goodbye!")