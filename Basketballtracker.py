#  Simple Basketball Stats Tracker

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'points': 0,
            'rebounds': 0,
            'assists': 0,
            'steals': 0,
            'blocks': 0,
            'turnovers': 0,
            'fouls': 0
        }

    def record_stat(self, stat, value):
        if stat in self.stats:
            self.stats[stat] += value
            return True
        return False

    def show_stats(self):
        print(f"Stats for {self.name}:")
        for stat, value in self.stats.items():
            print(f"  {stat}: {value}")

class Starplayer(Player):  # Inheritance
    def show_stats(self):  # Polymorphism (method override)
        print(f" Star Player Stats for {self.name}")
        for stat, value in self.stats.items():
            print(f"  {stat}: {value}")
        print("Keep up the great work!")

class Team:
    def __init__(self):
        self.players = {}

    def add_player(self, name, star=False):
        if name not in self.players:
            if star:
                self.players[name] = Starplayer(name)
                print(f"Added star player {name}.")
            else:
                self.players[name] = Player(name)
                print(f"Added player {name}.")
        else:
            print("Player already exists.")

    def record_stat(self, name, stat, value):
        if name in self.players:
            if self.players[name].record_stat(stat, value):
                print(f"Recorded {value} {stat} for {name}.")
            else:
                print("Invalid stat type.")
        else:
            print("Player not found.")

    def show_player(self, name):
        if name in self.players:
            self.players[name].show_stats()
        else:
            print("Player not found.")

    def show_team(self):
        if not self.players:
            print("No players on the team.")
            return
        team_totals = {stat: 0 for stat in self.players[next(iter(self.players))].stats}
        for player in self.players.values():
            for stat, value in player.stats.items():
                team_totals[stat] += value
        print("Team Stats:")
        for stat, value in team_totals.items():
            print(f"  {stat}: {value}")

team = Team()

while True:
    print("\nOptions: add, add_star, record, show, show_team, quit")
    action = input("Choose an action: ").strip().lower()
    if action == 'add':
        name = input("Enter player name: ").strip()
        team.add_player(name)
    elif action == 'add_star':
        name = input("Enter star player name: ").strip()
        team.add_player(name, star=True)
    elif action == 'record':
        name = input("Enter player name: ").strip()
        stat = input("Enter stat type (points, rebounds, assists, steals, blocks, turnovers, fouls): ").strip().lower()
        try:
            value = int(input("Enter value: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        team.record_stat(name, stat, value)
    elif action == 'show':
        name = input("Enter player name: ").strip()
        team.show_player(name)
    elif action == 'show_team':
        team.show_team()
    elif action == 'quit':
        print("Exiting program.")
        break
    else:
        print("Invalid option.")
