from datetime import datetime
import json
import random

from pathlib import Path
from typing import List

SECRET = random.randint(1, 5)
now = datetime.now()
attempts = 0
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


name = input("Hello, player! Enter your name: ")
name = name.capitalize()

while True:
    guess = int(input("Guessing a number (1,5): "))
    attempts += 1

    if guess == SECRET:
        print("Yey!")
        print(f"You needed {attempts} attempts.")
        date = now.strftime("%m/%d/%Y")
        data.append(
            {"name": name, "attempts": attempts, "date": str(date)}
        )

        data_str = json.dumps(data[:])
        data_path.write_text(data_str)
        break

    elif guess > SECRET:
        print("Guessed number is too high.")
    elif guess < SECRET:
        print("Guessed number is too low.")
    else:
        print("Sorry, wrong guess. Guess again.")
