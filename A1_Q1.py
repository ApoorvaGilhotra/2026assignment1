for row in range(5):
    for column in range(5):
        if ((row == 0 or row == 4) or ((column == 3 and row == 1) or (column == 2 and row == 2) or (
                column == 1 and row == 3))):
            print("*", end="")

        else:
            print(end=" ")
    print()
