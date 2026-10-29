
# Product quantities in two warehouses
stock = [
    [50, 20],
    [30, 60]
]

target = [40, 40]

for i in range(2):
    total = stock[0][i] + stock[1][i]

    print("Product", i + 1)
    print("Total stock:", total)

    if stock[0][i] < target[i]:
        print("Warehouse 1 has shortage")
    elif stock[0][i] > target[i]:
        print("Warehouse 1 has surplus")
    else:
        print("Warehouse 1 has correct stock")

    if stock[0][i] < target[i] and stock[1][i] > target[i]:
        transfer = target[i] - stock[0][i]
        print("Transfer", transfer, "units to Warehouse 1")

    print()
