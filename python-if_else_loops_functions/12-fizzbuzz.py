#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 15 == 0:
            print("Fizzbuzz", end=" ")
        elif x % 3 == 0:
            print("Fizz", end=" ")
        elif x % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{0}".format(x), end=" ")
