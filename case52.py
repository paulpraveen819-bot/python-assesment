
teams = ["Team A", "Team B", "Team C"]
sizes = [3, 4, 2]
round1 = [80, 70, 80]
round2 = [90, 85, 75]

total = []

for i in range(3):
    score = round1[i] + round2[i]
    total.append(score)

for i in range(3):
    if sizes[i] < 3 or sizes[i] > 4:
        print(teams[i], "Invalid team size")
    else:
        print(teams[i], "Total score:", total[i])

for i in range(3):
    for j in range(i + 1, 3):
        if total[i] < total[j]:
            total[i], total[j] = total[j], total[i]
            teams[i], teams[j] = teams[j], teams[i]

print("\nTeam Rankings:")

for i in range(3):
    print(i + 1, teams[i], total[i], "points")
