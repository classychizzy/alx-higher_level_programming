#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    str = "is greater than 5"
elif last_digit == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print("last digit of {} is {} {}".format(number, last_digit, str))
