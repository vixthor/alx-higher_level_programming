#!/usr/bin/python3
i = 0
for i in range(0, 99):
    if(i < 10):
        print("0{0}".format(i), end=', ')
        continue
    print("{0}".format(i), end=', ')
print("{}".format(i + 1))
