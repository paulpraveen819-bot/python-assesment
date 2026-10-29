
appliances = ["Fan", "Light", "AC"]
total = [0, 0, 0]

limit = 100

for i in range(3):
    print("\nEnter units used by", appliances[i])

    for day in range(7):
        units = int(input("Day " + str(day + 1) + ": "))
        total[i] = total[i] + units

print("\nWeekly Appliance Totals:")

for i in range(3):
    print(appliances[i], "=", total[i], "units")

    if total[i] > limit:
        print("Consumption is high!")
    else:
        print("Consumption is normal.")

print("\nTotal Weekly Consumption =", sum(total), "units")
