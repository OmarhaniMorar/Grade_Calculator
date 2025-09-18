player_points = int(input("Enter current points: "))

def calculate_bonus(points):
    if points < 50:
        return points + 10
    elif 50 <= points <= 80:
        return points + 5
    else:
        return points + 2

def Player_status(points):
    if points < 50:
        return "loser"
    elif 50 <= points < 100:
        return "On way to victory"
    else:
        return "Winner"

points = calculate_bonus(player_points)

status = Player_status(points)

print(f"New points: {points}")
print(f"Player status: {status}")



