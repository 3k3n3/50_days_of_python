"""
Write a function called even_or_average that ask a user to input five
numbers. Once the user is done, the code should return the largest even
number in the inputted numbers. If there is no even number in the list,
the code should return the average of all the five numbers.
"""


def even_or_average() -> int:
    nums = []
    # evens = [i for i in nums if i % 2 == 0]
    while len(nums) < 5:
        try:
            num = int(input(f"({len(nums)}) - Enter a number: "))
            nums.append(num)
        except ValueError:
            print("Enter a valid number")

    evens = [i for i in nums if i % 2 == 0]
    if len(evens) > 0:
        return max(evens)
    else:
        return sum(nums) / 5


print(even_or_average())
