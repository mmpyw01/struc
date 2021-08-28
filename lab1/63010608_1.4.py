print("*** Fun with Drawing ***")
num = int(input("Enter input : "))

x = 2 * num - 2
i = num

for j in range(-x, x + 1):
    for i in range(-x, x + 1):
        if abs(i) + abs(j) == abs(i) * 2 and i % 2 == 0:
            print("#", end="")
        elif abs(i) + abs(j) == abs(i) * 2 and i % 2 == 1:
            print(".", end="")
        elif abs(j) % 2 == 1 and abs(i) % 2 == 1:
            print(".", end="")
        elif abs(j) % 2 == 0 and abs(i) % 2 == 0:
            print("#", end="")
        elif abs(j) % 2 == 1 and abs(i) % 2 == 0 and abs(j) < abs(i):
            print("#", end="")
        elif abs(j) % 2 == 0 and abs(i) % 2 == 1 and abs(j) < abs(i):
            print(".", end="")
        elif abs(j) % 2 == 1 and abs(i) % 2 == 0 and abs(j) > abs(i):
            print(".", end="")
        elif abs(j) % 2 == 0 and abs(i) % 2 == 1 and abs(j) > abs(i):
            print("#", end="")
        else:
            print(" ", end="")

    print()