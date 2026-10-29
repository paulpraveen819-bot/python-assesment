
branches = [
    [1000, 2000, 1500],
    [2500, 1000, 2000],
    [1500, 1800, 1200]
]

for i in range(3):
    total = sum(branches[i])
    average = total / 3

    print("Branch", i + 1)
    print("Total expenses:", total)
    print("Average expense:", average)

print("\nHighest expense:")

highest = 0
branch_no = 0

for i in range(3):
    total = sum(branches[i])

    if total > highest:
        highest = total
        branch_no = i + 1

print("Branch", branch_no, "=", highest)
