x = input()
num = ord(x)

for y in range(97, num+1):
    print(chr(y), end=' ')
    num -= 1
