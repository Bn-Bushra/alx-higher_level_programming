#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#print(F"The last digit of {number} is")
if number < 0:
    last_digit = -(abs(number) % 10)
# last_digit = abs(number) % 10
if last_digit > 5:
    print(f"Last digit for {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit for {number} is {last_digit} and is 0")
else:
    print(f"Last digit for {number} is {last_digit} and is less 6 and not 0")
