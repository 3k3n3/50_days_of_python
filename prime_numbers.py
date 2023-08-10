"""
Write a function called prime_numbers. This function asks a 
user to enter a number (integer) as an argument and returns a 
list of all the prime numbers within its range.
"""

pn = []


def is_prime(num: int) -> bool:
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        return True
    return False


def prime_numbers() -> list:
    try:
        num = int(input("Enter a number: "))
        for i in range(num):
            if is_prime(i):
                pn.append(i)
        return pn

    except ValueError:
        print("Enter Valid Number")
        prime_numbers()


print(prime_numbers())
