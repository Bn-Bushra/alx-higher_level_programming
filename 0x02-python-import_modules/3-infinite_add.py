#!/usr/bin/python3
import sys
count = len(sys.argv[:-1])
sum = 0
for arg in range(count):
    args = int(sys.argv[arg + 1])
    sum += args
print(f"{sum}")
