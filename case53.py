
prepared = [100, 120, 80]
served = [90, 100, 60]

limit = 20

for i in range(3):
    leftover = prepared[i] - served[i]
    waste = (leftover / prepared[i]) * 100

    print("Day", i + 1)
    print("Leftover meals:", leftover)
    print("Waste percentage:", waste, "%")

    if waste > limit:
        print("Wastage is high")
    else:
        print("Wastage is normal")

    print()
