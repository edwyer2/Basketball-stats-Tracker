# Basketball Stat Tracker

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

    def record_stat(self, stat_type, value):
        if stat_type in self.stats:
            self.stats[stat_type] += value
        else:
            print(f"Invalid stat type: {stat_type}")

    def display_stats(self):
        print(f"Stats for {self.name}:")
        for stat, value in self.stats.items():
            print(f"  {stat}: {value}")

class Team:
    def __init__(self):
        self.players = {}

    def add_player(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
        else:
            print(f"Player {name} already exists.")

    def record_stat(self, name, stat_type, value):
        if name in self.players:
            self.players[name].record_stat(stat_type, value)
        else:
            print(f"Player {name} not found.")

    def display_player_stats(self, name):
        if name in self.players:
            self.players[name].display_stats()
        else:
            print(f"Player {name} not found.")

    def display_team_stats(self):
        print("Team Stats:")
        team_totals = {stat: 0 for stat in self.players[next(iter(self.players))].stats} if self.players else {}
        for player in self.players.values():
            for stat, value in player.stats.items():
                team_totals[stat] += value
        for stat, value in team_totals.items():
            print(f"  {stat}: {value}")

# Main Loop
team = Team()

while True:
    print("\nOptions: add, record, show, show_team, quit")
    action = input("Choose an action: ").strip().lower()
    if action == 'add':
        name = input("Enter player name: ").strip()
        team.add_player(name)
    elif action == 'record':
        name = input("Enter player name: ").strip()
        stat = input("Enter stat type: ").strip().lower()
        value = int(input("Enter value: "))
        team.record_stat(name, stat, value)
    elif action == 'show':
        name = input("Enter player name: ").strip()
        team.display_player_stats(name)
    elif action == 'show_team':
        team.display_team_stats()
    elif action == 'quit':
        print("Exiting program.")
        break
    else:
        print("Invalid option.")
