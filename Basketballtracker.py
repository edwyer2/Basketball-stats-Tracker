# Very Simple Basketball Stats Tracker

# Dictionary to store player stats
players = {}

while True:
    print("\nOptions: add, record, show, show_team, quit")
    action = input("Choose an action: ").strip().lower()
    if action == 'add':
        name = input("Enter player name: ").strip()
        if name not in players:
            # Each player has stats stored in a dictionary
            players[name] = {'points': 0, 'rebounds': 0, 'assists': 0, 'steals':0, 'blocks':0, 'turnovers':0, 'fouls':0}
        else:
            print("Player already exists.")
    elif action == 'record':
        name = input("Enter player name: ").strip()
        if name in players:
            stat = input("Enter stat type (points, rebounds, assists, steals, blocks, turnovers, fouls): ").strip().lower()
            if stat in players[name]:
                value = int(input("Enter value: "))
                players[name][stat] += value
            else:
                print("Invalid stat type.")
        else:
            print("Player not found.")
    elif action == 'show':
        name = input("Enter player name: ").strip()
        if name in players:
            print(f"Stats for {name}:")
            for stat, value in players[name].items():
                print(f"  {stat}: {value}")
        else:
            print("Player not found.")
    elif action == 'show_team':
        print("Team Stats:")
        team_totals = {'points': 0, 'rebounds': 0, 'assists': 0, 'steals':0, 'blocks':0, 'turnovers':0, 'fouls':0}
        for stats in players.values():
            for stat in team_totals:
                team_totals[stat] += stats[stat]
        for stat, value in team_totals.items():
            print(f"  {stat}: {value}")
    elif action == 'quit':
        print("Exiting program.")
        break
    else:
        print("Invalid option.")
           
    

