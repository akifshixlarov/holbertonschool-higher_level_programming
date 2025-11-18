#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0
    for val in argv[1:]:
        total += int(val)
    print(total)
