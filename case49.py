
products = [
    (101, 50, 10),
    (102, 100, 0),
    (103, -20, 5)
]

for p in products:
    if p[1] < 0 or p[2] < 0:
        print("Invalid record:", p[0])
    else:
        value = p[1] * p[2]
        print("Product ID:", p[0])
        print("Inventory value:", value)

        if p[2] < 5:
            print("Replenishment required")

    print()
