"""
You want to implement a code that will search for a number in 
a range. You have a decision to make as to whether to store the 
number in a set or a list. Your decision will be based on time. 
You have to pick a data type that executes faster. 
You have a range and you can either store it in a set or a list 
depending on which one executes faster when you are searching 
for a number in the range.

Let's say you are looking for a number 9999999 in the range 
above. Search for this number in the list and the set. Your 
challenge is to find which code executes faster. You will pick the 
one that executes quicker, lists, or sets. Run the two searches 
and time them. 
"""
import timeit


def set_or_list():
    """Test speed of execution."""

    statement1 = """
a = range(10000000)
x = set(a)

num = 9999999

if num in x:
    print(num)
"""

    statement2 = """
b = range(10000000)
y = list(b)

num = 9999999

if num in y:
    print(num)
"""

    print(timeit.timeit(statement1, number=1))
    print(timeit.timeit(statement2, number=1))


print(set_or_list())
# Lists are faster in this demo
