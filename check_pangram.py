"""
Write a function called check_pangram that takes a string 
and checks if it is a pangram. A pangram is a sentence that 
contains all the letters of the alphabet. If it is a pangram, 
the function should return True, otherwise, return False.
"""


def pangram(sentence: str) -> bool:
    check = {i.lower() for i in sentence if i.isalpha()}
    if len(check) != 26:
        return False
    return True


sentence = "the quick brown fox jumps over a lazy dog"
print(pangram(sentence))
