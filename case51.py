
capacity = 50
passengers = 0

boarding = [20, 15, 10]
alighting = [0, 5, 8]

for i in range(3):
    passengers = passengers - alighting[i]
    passengers = passengers + boarding[i]

    print("Stop", i + 1)
    print("Passengers:", passengers)

    if passengers > capacity:
        print("Capacity exceeded!")

    print()
