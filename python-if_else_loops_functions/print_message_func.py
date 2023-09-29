#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
def print_message(a:int, b:int):
    if b > 5:
        print(f"Last digit of {a} is {b} and is greater than 5")
    elif a == 0:
        print(f"Last digit of {a} is {b} and is 0")
    else:
        print(f"Last digit of {a} is {b} and is less than 6 and not 0")
    return 0

print(number)
end = number % 10
if number >= 10:
    print_message(number, end)
if number < 0:
    end = number % -10
    print_message(number, end)
if number >= 0 and number < 10:
    end = number
    print_message(number, end)
