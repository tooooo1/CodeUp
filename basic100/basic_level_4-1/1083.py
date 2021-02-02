x = int(input())

for y in range(1, x+1):
    if (y % 3) == 0:
        print("X", end=" ")
    else:
        print(y, end=" ")
