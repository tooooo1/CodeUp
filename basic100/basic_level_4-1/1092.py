one, two, three = map(int, input().split())
day = 1

while 1:
    if ((day % one == 0) and (day % two == 0) and (day % three == 0)):
        print(day)
        break
    else:
        day += 1
