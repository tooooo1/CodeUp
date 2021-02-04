a = input()
a = int(a, 16)

for i in range(1, 16):
    print("{:X}".format(a) + "*" + "{:X}".format(i)+"="+"{:X}".format(a*i))
