"""
Write a function called divide_or_square that takes one 
argument (a number), and returns the square root of the number 
if it is divisible by 5, returns its remainder if it is not divisible by 
5. For example, if you pass 10 as an argument, then your function 
should return 3.16 as the square root.
"""
from math import sqrt

def divide_or_square(num: int) -> int:
    if num % 5:
        return num % 5
    else:
        return sqrt(num)


print(divide_or_square(25))
print(divide_or_square(10))