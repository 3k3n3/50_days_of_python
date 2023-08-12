"""
Your new company has a list of figures saved in a list. The issue is that
these numbers have no separator. The numbers are saved in the following
format: [1000000, 2356989, 2354672, 9878098].
You have been asked to write a code that will convert each of the numbers
in the list into a string. Your code should then add a comma on each number
as a thousand separator for readability.
"""


def thousand_separator(numbers: list) -> list:
    for n in numbers:
        print(f"{n:,}")


nums = [1000000, 2356989, 2354672, 9878098, 1000, 64538]
print(thousand_separator(numbers=nums))
