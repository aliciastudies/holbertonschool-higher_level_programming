#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def print_message(a, b):
    if b > 5:
        print(f"Last digit of {a} is {b} and is greater than 5")
    elif a == 0:
        print(f"Last digit of {a} is {b} and is 0")
    else:
        print(f"Last digit of {a} is {b} and is less than 6 and not 0")
    return 0


# print(number)
last_digit = number % 10
if number >= 10:
    print_message(number, last_digit)
if number < 0:
    last_digit = number % -10
    print_message(number, last_digit)
if number >= 0 and number < 10:
    last_digit = number
    print_message(number, last_digit)
