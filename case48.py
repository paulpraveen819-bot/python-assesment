
shifts = [
    ("Ravi", 9, 1),
    ("Ravi", 12, 4),
    ("Ram", 10, 2)
]

for i in range(len(shifts)):
    for j in range(i + 1, len(shifts)):
        if shifts[i][0] == shifts[j][0]:
            if shifts[i][1] < shifts[j][2] and shifts[j][1] < shifts[i][2]:
                print(shifts[i][0], "has a shift conflict")
