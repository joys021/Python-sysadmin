#!/usr/bin/env python3

"""
#Question 1: get name and print


first_name = (input(" F name:").upper())
last_name = input(" L name:").upper()
age = input(" Age:")
birth_date = "07/08/1958"

print(f"My name is {first_name} {last_name}.")
print(f"I was born on {birth_date}, and I'm {age} years old.")

"""


"""
#Question 2: Prints the first ten digits of PI,
#if DIGIT present then print those many digits


from os import getenv
from math import pi
digits = int(getenv("DIGITS") or 10)
print("%.*f" % (digits, pi))
"""

