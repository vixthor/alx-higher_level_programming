#!/usr/bin/python3
for i in range(0, 9):
    for x in range(0 + i, 10):
        print("{:d}{:d}".format(i,x), end=', ')
print("{:d}{:d}".format(i + 1, x))
