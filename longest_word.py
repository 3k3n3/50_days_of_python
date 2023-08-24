"""
Write a function that has one parameter and takes a list of words 
as an argument. The function returns the longest word from the 
list. Name the function longest_word. The function should 
return the longest word and the number of letters in that word. 
"""


def longest_word(arr: list) -> list:
    x = {len(k): (k) for k in arr}
    return [sorted(x)[-1], x[sorted(x)[-1]]]


words = ["Java", "Javascript", "Python"]

print(longest_word(words))
