from datetime import datetime
import json
from pathlib import Path
from typing import List
import random

def run_game():
    if level == "easy":
        SECRET = random.randint(1, 5)
        print("Secret number is between 1 and 5. Let's begin.")
    else:
        SECRET = random.randint(1, 30)
        print("Secret number is between 1 and 30. Let's begin.")

    data_path: Path = Path(".", "data", "top_score_info.txt")
    data: List[int] = json.loads(data_path.read_text())

    attempts = 0
    now = datetime.now()

    name = input("Hello, player! Enter your name: ").capitalize()

    while True:
        guess = int(input("Your guessing number: "))
        attempts += 1

        if guess == SECRET:
            print("Yey!")
            print(f"You needed {attempts} attempts.")
            date = now.strftime("%m/%d/%Y, %H:%M")
            data.append(
                {"name": name, "attempts": attempts, "date": str(date)}
            )

            data_str = json.dumps(data)
            data_path.write_text(data_str)
            break
        elif guess > SECRET:
            print("Guessed number is too high.")
        elif guess < SECRET:
            print("Guessed number is too low.")
        else:
            print("Sorry, wrong guess. Guess again.")
def get_score():
    index = 1

    data_path: Path = Path(".", "data", "top_score_info.txt")
    data: List[int] = json.loads(data_path.read_text())

    if len(data) != 0:
        data = sorted(data, key=lambda item: item.get("attempts"))[:3]

    for score_dict in data:
        score_text = " {0}. Place is : Player {1} with {2} attempts on {3}.".format(
            index,
            score_dict.get("name"),
            str(score_dict.get("attempts")),
            score_dict.get("date"),
        )
        print(score_text)
        index += 1

while True:
    option = input(f"Welcome to guessing game!! \nWould you like to play a game? A) Play new game B) Top 3 scores of all time C) Quit :")
    if option == "a":
        level = input("Choose level (easy/hard)? : ")
        run_game()
    elif option == "b":
        get_score()
    else:
        break