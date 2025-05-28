def patt_size():
    patt = int(input("Enter the seize of the pattern: "))
    row = 0
    while row < patt:
        for _ in range(patt):
            print("*", end="")
        print()
        row += 1

patt_size()