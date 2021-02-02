number = int(input())
add = 0

for x in range(1, number+1):
    if (x % 2) == 0:
        add += x

print(add)
