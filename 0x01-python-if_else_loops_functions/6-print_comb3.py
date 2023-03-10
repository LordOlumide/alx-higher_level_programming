#!/usr/bin/python3
a = 0
while a < 9:
    b = a + 1
    while b < 10:
        print(f"{a}{b}", end=', ' if (f"{a}{b}" != "89") else '\n')
        b += 1
    a += 1
