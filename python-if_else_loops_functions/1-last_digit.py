#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# print(number)
def is_last(number: int):
    if number >= 10:
        last_digit = number % 10
        return(last_digit)
    elif number >= 0 and number < 10:
        last_digit = number
        return(last_digit)
    else:
        if number < 0:
            last_digit = number % -10
            return(last_digit)


def if_last(last_digit: str):
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit != 0 and last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
