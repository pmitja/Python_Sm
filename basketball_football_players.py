class Player(object):
    def __init__(self, first_name, surname, height, weight):
        self.first_name = first_name
        self.surname = surname
        self.height = height
        self.weight = weight


class Basket_player(Player):
    def __init__(
        self, first_name, surname, height, weight, avg_points, avg_rebounds, avg_assists
    ):
        super().__init__(
            first_name=first_name, surname=surname, height=height, weight=weight
        )
        self.avg_points = avg_points
        self.avg_rebounds = avg_rebounds
        self.avg_assists = avg_assists


class Football_player(Player):
    def __init__(
        self, first_name, surname, height, weight, goals, yellow_cards, red_cards
    ):
        super().__init__(
            first_name=first_name, surname=surname, height=height, weight=weight
        )
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


print(f"Enter your favorite basketball player details please.")

f_name = input("First name: ")
s_name = input("Surname :")
player_height = input("Height: ")
player_weight = input("Weight: ")
player_points = input("Average points: ")
player_rebounds = input("Average rebounds: ")
player_assists = input("Average assists: ")

new_player = Basket_player(
    first_name=f_name,
    surname=s_name,
    height=player_height,
    weight=player_weight,
    avg_points=player_points,
    avg_rebounds=player_rebounds,
    avg_assists=player_assists,
)

with open("data/basketball_players.txt", "w") as player_file:
    player_file.write(str(new_player.__dict__))

print("New player is successfully in our player data base.")
print("Player's data: {0}".format(new_player.__dict__))
