#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1
if last_digit > 5:
    print(f"The last digit of {number:d}\
 is {last_digit:d} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"The last digit of {number:d}\
 is {last_digit:d} and is less than 6 but not 0")
elif last_digit == 0:
    print(f"The last digit of {number:d}\
 is {last_digit:d} and is 0")
