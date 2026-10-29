
teams = ["Team A", "Team B", "Team C"]
points = [6, 6, 3]
tie_break = [10, 15, 8]

for i in range(3):
    for j in range(i + 1, 3):
        if points[i] < points[j]:
            points[i], points[j] = points[j], points[i]
            tie_break[i], tie_break[j] = tie_break[j], tie_break[i]
            teams[i], teams[j] = teams[j], teams[i]

        elif points[i] == points[j]:
            if tie_break[i] < tie_break[j]:
                tie_break[i], tie_break[j] = tie_break[j], tie_break[i]
                teams[i], teams[j] = teams[j], teams[i]

print("Tournament Rankings")

for i in range(3):
    print(i + 1, teams[i], "Points:", points[i],
          "Tie-break:", tie_break[i])
